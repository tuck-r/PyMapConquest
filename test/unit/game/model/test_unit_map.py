import unittest

from game.model.map import Map

class TestMap(unittest.TestCase):
    def test_basic_build_01(self):
        # Create empty map.
        test_map = Map()
        # Build on a square.
        test_coords = (4, 10)
        test_player_id = 0
        test_building_name = "Food Mill"
        test_map.build_on_tile(test_coords, test_player_id, test_building_name)
        # Assert the tiles that the player should own.
        self.assertEqual(test_map.find_owned_tile_ids(test_player_id), [test_coords])

if __name__ == "__main__":
    unittest.main(verbosity=5)
