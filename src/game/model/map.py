import random
from collections import defaultdict

class Map:
    def __init__(self):
        # Set number of tiles on map in x and x direction.
        self.map_size = 20
        # Initialise map with empty tiles.
        self.map_tile_array = [[Tile(x, y) for x in range(0, self.map_size)] for y in range(0, self.map_size)]

    def initialise_start_tiles(self, players_info_dict):
        """
        :return: None.

        Assigns a tile to each player at the start of the game.
        """
        # Loop through each player id and find them a tile that is not currently owned for them to start on.
        for a_player_id in players_info_dict.keys():
            found_empty_tile = False
            # Find a tile that is not currently owned.
            while not found_empty_tile:
                # Generate random i,j map coordinates.
                try_i = random.randint(0, self.map_size-1)
                try_j = random.randint(0, self.map_size-1)
                if self.map_tile_array[try_i][try_j].get_is_owned_by() is None:
                    self.map_tile_array[try_i][try_j].set_is_owned_by(a_player_id)
                    found_empty_tile = True

    def get_resource_update(self, player_index):
        """
        :param player_index: int: Index of the player to count up new resources for.
        :return: dict: dict containing new resources to give the player.

        Given the index of a player, tallies up the new resources to be given to them at the start of their turn.
        """
        new_resources = defaultdict(int)
        for selected_row in self.map_tile_array:
            for selected_tile in selected_row:
                if player_index == selected_tile.get_is_owned_by():
                    # Get resources on tile.
                    found_on_tile = selected_tile.get_resources()
                    for key_resource, count in found_on_tile.items():
                        new_resources[key_resource] += count
        return new_resources

    def find_owned_tiles(self, player_id):
        """
        :param player_id: int: Index of the player to find the tiles belonging to.
        :return: list: List of coordinates of tiles held by player.

        Find all tiles held by a player.
        """
        owned_tiles = []
        for selected_row in self.map_tile_array:
            for selected_tile in selected_row:
                if player_id == selected_tile.get_is_owned_by():
                    owned_tiles.append(selected_tile.get_coordinates())
        return owned_tiles

class Tile:
    def __init__(self, i, j):
        # Which unit is currently on the tile.
        self.unit = None
        # Which building is currently on the tile.
        self.building = None
        # Which player currently holds the tile (i.e. whoever owns the building).
        self.held_by_player = None
        # Resources that the tile holds.
        self.resources = None
        self.initialise_resources()
        # i,j coordinates for this tile.
        self.coordinates = [i, j]

    def initialise_resources(self):
        """
        :return: dict: dict containing resources.

        Generates random resources to be placed on the tile.
        """
        self.resources = dict()
        self.resources["Food"] = random.randint(0, 10)
        self.resources["Gold"] = random.randint(0, 10)
        self.resources["Wood"] = random.randint(0, 10)
        self.resources["Metal"] = random.randint(0, 10)

    def get_coordinates(self):
        return self.coordinates

    def get_is_owned_by(self):
        return self.held_by_player

    def set_is_owned_by(self, player_id):
        self.held_by_player = player_id

    def get_resources(self):
        return self.resources
