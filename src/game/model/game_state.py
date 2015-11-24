from game.model.map import Map

class GameState:
    def __init__(self, dict_player_info):
        # Save players info.
        self.players_dict = dict_player_info
        # Give each player some starting resources.
        for i in range(0, len(self.players_dict.keys())):
            self.players_dict[i]["curr_resources"] = {"Food": 500,
                                                      "Gold": 500,
                                                      "Wood": 500,
                                                      "Metal": 500}
        # Create a new starting map.
        self.current_map_state = Map()
        # Create a record of moves that have been made.
        self.game_move_history = []
        # Track who the current active player is.
        self.active_player = 0
        # Currently while testing, we have a round limit.
        self.NUM_ROUND_LIMIT = 10
        # Track how many rounds have been played.
        self.num_rounds_played = 0
        # Initialise starting tile for each player.
        self.current_map_state.initialise_start_tiles(self.players_dict)

    def start_of_player_turn(self):
        """
        :return:
        """
        # Update resources held by the active player.
        # Loop through all tiles, seeing if the active player owns it.
        resources_to_add = self.current_map_state.get_resource_update(self.active_player)
        for key_resource, value_count in resources_to_add.items():
            self.players_dict[self.active_player]["curr_resources"][key_resource] += value_count

    def is_move_valid(self, proposed_move):
        """
        :param proposed_move: Move: Information detailing the proposed move to make.
        :return: boolean: Whether the proposed move is valid.

        Tests whether a move a player wishes to make is possible.
        Returns True if the move can be made, False otherwise.
        """
        # TODO: Actual valid move logic.
        if proposed_move == "END":
            return True
        return False

    def make_move(self, make_move):
        """
        :param make_move: Move: Information detailing the move to make.
        :return: None.
        """
        pass

    def end_current_turn(self):
        """
        :return self.active_player: int: dict index of the new active player.

        Ends the turn for the current active player,
        and switches to the next player.
        """
        # TODO: Update turn logs.
        # Update the active player.
        self.active_player += 1
        if self.active_player >= len(self.players_dict.keys()):
            self.active_player = 0
            # Have looped through all players in the game - update round counter.
            self.num_rounds_played += 1
        return self.active_player

    def has_game_ended(self):
        """
        :return: boolean: Whether or not the game has reached an end game state.

        TODO: For current testing purposes, max number of rounds has been set to 10.
        """
        if self.num_rounds_played >= self.NUM_ROUND_LIMIT:
            return True
        return False

    def print_end_game_stats(self):
        """
        :return: None.

        Prints end game information.
        """
        pass

    def get_held_tiles(self, player_id):
        return self.current_map_state.find_owned_tiles(player_id)

    def get_player_resources(self, player_id):
        return self.players_dict[player_id]["curr_resources"]

    def main_game_loop(self):
        pass
