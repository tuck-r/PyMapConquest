import time
import math

from game.model.map import Map
from game.model.building import Building
from game.model.move import Move


class GameState:
    def __init__(self, dict_player_info):
        # Save players info.
        self.players_dict = dict_player_info
        # Give each player some starting resources.
        for i in range(0, len(self.players_dict.keys())):
            # Initialise resources.
            self.players_dict[i]["curr_resources"] = {"Food": 200,
                                                      "Gold": 200,
                                                      "Wood": 200,
                                                      "Metal": 200}
            # Initialise map bonuses values.
            self.players_dict[i]["curr_map_bonuses"] = {"Food": 0.0,
                                                        "Gold": 0.0,
                                                        "Wood": 0.0,
                                                        "Metal": 0.0,
                                                        "Attack_Buildings": 0.0,
                                                        "Defense_Buildings": 0.0}
        # Create a new starting map.
        self.current_map_state = Map()
        # Create a record of moves that have been made.
        self.game_move_history = []
        # Track who the current active player is.
        self.active_player = 0
        # Currently while testing, we have a round limit.
        self.NUM_ROUND_LIMIT = 50
        # Track how many rounds have been played.
        self.num_rounds_played = 0
        # Initialise starting tile for each player.
        self.current_map_state.initialise_start_tiles(self.players_dict)
        # Set the allowed win types.
        self.allowed_win_conditions = {"tiles_owned": 50}

        ###
        # Options/status for current player.
        ###
        self.tiles_held = []
        self.tiles_adjacent_free = []
        self.tiles_adjacent_enemy = []
        self.valid_moves = []

    def get_player_ids(self):
        return self.players_dict.keys()

    def get_players_dict(self):
        return self.players_dict

    def start_of_player_turn(self):
        """
        :return:
        """
        # Update resources held by the active player.
        # Loop through all tiles, seeing if the active player owns it.
        resources_to_add = self.current_map_state.get_resource_update(self.active_player)
        for key_resource, value_count in resources_to_add.items():
            # Add tile values.
            self.players_dict[self.active_player]["curr_resources"][key_resource] += value_count
            # Add map bonuses.
            bonus_for_tile = self.players_dict[self.active_player]["curr_map_bonuses"][key_resource]
            rounded_addition_value = math.floor(bonus_for_tile * self.players_dict[self.active_player]["curr_resources"][key_resource])
            self.players_dict[self.active_player]["curr_resources"][key_resource] += rounded_addition_value

    def update_player_status(self):
        """
        :return:

        Updates variables storing current status/options available to the currently active player.
        """
        self.tiles_held = self.get_held_tiles(self.active_player)
        self.tiles_adjacent_free = self.get_adjacent_free_tiles(self.active_player)
        self.valid_moves = self.find_all_valid_moves()

    def update_map_bonus(self, player_id, attribute, amount):
        self.players_dict[player_id]["curr_map_bonuses"][attribute] += amount

    def update_tile_bonus(self, coords, attribute, amount):
        self.current_map_state.update_tile_bonus(coords, attribute, amount)

    def is_move_valid(self, proposed_move):
        """
        :param proposed_move: Move: Information detailing the proposed move to make.
        :return: boolean: Whether the proposed move is valid.

        Tests whether a move a player wishes to make is possible.
        Returns True if the move can be made, False otherwise.
        """
        if proposed_move == "END" or proposed_move in self.valid_moves:
            return True
        return False

    def find_all_valid_moves(self):
        """
        :return: list: List of valid moves the player can make at the current moment.

        Find all valid moves that a player could make at this moment.
        """
        moves_found = []

        # Check each tile to see which ones have room for units or buildings.
        has_room_for_unit = []
        has_room_for_building = []

        # Check held tiles for room for units and buildings.
        for a_tile in self.tiles_held:
            if a_tile.get_unit is None:
                has_room_for_unit.append(a_tile)
            if a_tile.get_building is None:
                has_room_for_building.append(a_tile)
        # Free adjacent tiles have room for buildings.
        for a_tile in self.tiles_adjacent_free:
            # Free squares should have no buildings on them and not be owned but check anyway.
            if a_tile.get_is_owned_by() is None and a_tile.get_building() is None:
                has_room_for_building.append(a_tile)

        # Check all units that could be built with current resources.
        if len(has_room_for_unit) > 0:
            pass
        # Check all buildings that could be built with current resources.
        if len(has_room_for_building) > 0:
            has_resources = self.get_player_resources(self.active_player)
            all_buildings_data = Building.get_all_buildings()
            # See which buildings they can afford.
            for key_building_name, value_building_data in all_buildings_data.items():
                building_cost = value_building_data["Cost"]
                can_afford = True
                for key_resource_name, value_cost in building_cost.items():
                    if has_resources[key_resource_name] < value_cost:
                        can_afford = False

                if can_afford is True:
                    # Generate all valid building purchase moves.
                    for a_tile in has_room_for_building:
                        move_metadata = {
                            "tile_coords": a_tile.get_coordinates(),
                            "building_name": key_building_name,
                            "building_cost": value_building_data["Cost"]
                        }
                        new_move = Move("build", move_metadata)
                        moves_found.append(new_move)
        return moves_found

    def get_valid_moves(self):
        return self.valid_moves

    def make_move(self, make_move):
        """
        :param make_move: Move: Information detailing the move to make.
        :return: None.
        """
        move_type = make_move.get_move_type()
        move_metadata = make_move.get_move_metadata()

        if move_type == "build":
            # Apply "build" type logic.
            self.current_map_state.build_on_tile(move_metadata["tile_coords"], self.active_player, move_metadata["building_name"])
            # Decrement player resources according to the cost of the building.
            for key_resource, value_cost in move_metadata["building_cost"].items():
                self.players_dict[self.active_player]["curr_resources"][key_resource] -= value_cost
            # Update player map bonuses.
            map_bonuses = self.current_map_state.get_tile(move_metadata["tile_coords"]).get_building().get_building_map_bonuses()
            if map_bonuses:
                for key_attribute, value_amount in map_bonuses.items():
                    self.update_map_bonus(self.active_player, key_attribute, value_amount)
        else:
            raise Exception("Move type \"%s\" is not valid." % move_type)

        # Add move to the log.
        add_to_game_log = [self.active_player, make_move.format_move()]
        self.game_move_history.append(add_to_game_log)

    def end_current_turn(self):
        """
        :return self.active_player: int: dict index of the new active player.

        Ends the turn for the current active player,
        and switches to the next player.
        """
        # Update turn logs.
        self.game_move_history.append([self.active_player, "END"])
        # Update the active player.
        self.active_player += 1
        if self.active_player >= len(self.players_dict.keys()):
            self.active_player = 0
            # Have looped through all players in the game - update round counter.
            self.num_rounds_played += 1
        return self.active_player

    def has_game_ended(self):
        """
        :return: dict: dict containing winning player id and the type of win
        they achieved.
        Returns None if the game is still ongoing.

        For current testing purposes, a max number of rounds has been set.
        """
        # Check if we have reached the max number of rounds to play.
        if self.num_rounds_played >= self.NUM_ROUND_LIMIT:
            return {"Winner": None, "Win_Type": "round_limited"}
        # Check if a win condition has been met.
        winning_player, win_by_type = self.check_if_win_condition()
        if winning_player and win_by_type:
            return {"Winner": winning_player, "Win_Type": win_by_type}
        # Game is still in progress since all checks have found nothing.
        return None

    def check_if_win_condition(self):
        """
        :return: winning_player: int: dict index of the winning player.
        :return: win_type: string: Type of win the player has achieved.
        Valid win types:
            - tiles_owned: First player to own a specified number of tiles.

        The win type may be specified when setting up a game so that it is an
        allowed or disallowed way of winning the game.

        Returns None, None if a win condition has been met by none of the players.
        """
        if "tiles_owned" in self.allowed_win_conditions:
            # Only need to check the number of tiles owned by the active player.
            if len(self.tiles_held) >= self.allowed_win_conditions["tiles_owned"]:
                return self.active_player, "tiles_owned"
        return None, None

    def print_end_game_stats(self):
        """
        :return: None.

        Prints end game information.
        """
        pass

    def get_held_tile_ids(self, player_id):
        return self.current_map_state.find_owned_tile_ids(player_id)

    def get_held_tiles(self, player_id):
        return self.current_map_state.find_owned_tiles(player_id)

    def get_adjacent_free_tiles(self, player_id):
        return self.current_map_state.find_adjacent_free_tiles(player_id)

    def get_player_resources(self, player_id):
        return self.players_dict[player_id]["curr_resources"]

    def get_map_size(self):
        return self.current_map_state.get_map_size()

    def get_map_tile_array(self):
        return self.current_map_state.get_map_tile_array()

    def get_player_map_bonuses(self, player_id):
        return self.players_dict[player_id]["curr_map_bonuses"]

    def write_game_log(self):
        log_file_name = "log_%s.txt" % time.time()
        open_log_file = open(log_file_name, "wb")
        for a_move in self.game_move_history:
            open_log_file.write(str(a_move)+"\n")
        open_log_file.close()

    def main_game_loop(self):
        pass
