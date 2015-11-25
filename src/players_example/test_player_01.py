"""
Example player - used mainly for testing code.

Chooses a random move from a list of valid moves.
"""
import random

from api import helpers

# A future update may make older scripts incompatible with new versions of the game.
# You shouldn't need to change this value yourself.
VERSION_COMPATIBLE = "0.1"

# Give your ai player a name to use in-game.
PLAYER_NAME = "Random Tester One"

def return_move(game_state):
    moves_could_make = helpers.get_all_valid_moves(game_state)
    if len(moves_could_make) == 0:
        return "END"
    else:
        # Pick a random valid move.
        random_select = random.randint(0, len(moves_could_make) - 1)
        return moves_could_make[random_select]
