import random
from collections import defaultdict

class Map:
    def __init__(self):
        # Set number of tiles on map in x and x direction.
        self.map_size = 20
        # Initialise map with empty tiles.
        self.map_tile_array = [[Tile() for x in range(0, self.map_size)] for y in range(0, self.map_size)]

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


class Tile:
    def __init__(self):
        # Which unit is currently on the tile.
        self.unit = None
        # Which building is currently on the tile.
        self.building = None
        # Which player currently holds the tile (i.e. whoever owns the building).
        self.held_by_player = None
        # Resources that the tile holds.
        self.resources = None
        self.initialise_resources()

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

    def get_is_owned_by(self):
        return self.held_by_player

    def get_resources(self):
        return self.resources
