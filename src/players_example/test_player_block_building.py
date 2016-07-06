"""
This is the boilerplate file you start with when you create a new ai player.
"""
from api import helpers
import random
from collections import defaultdict

# A future update may make older scripts incompatible with new versions of the game.
# You shouldn't need to change this value yourself.
VERSION_COMPATIBLE = "0.1"

# Give your ai player a name to use in-game.
PLAYER_NAME = "Building Blocker"

"""
Strategy:
    - Build in horizontal and vertical patterns to 'trap' the other player and
    prevent them from grabbing more land.
"""


def return_move(game_state, player_number):
    # Find tiles owned and valid moves that could be made.
    moves_could_make = helpers.get_all_valid_moves(game_state)

    # Sort list of moves.
    if len(moves_could_make) > 0:
        moves_set = set([])
        move_coords_lookup = defaultdict(list)
        shuffled_moves = []
        for a_move in moves_could_make:
            coords = helpers.get_move_coordinates(a_move)
            move_coords_lookup[coords].append(a_move)
            shuffled_moves.append(coords)
        shuffled_moves.sort(key=lambda x: (x[0]))
        shuffled_moves.sort(key=lambda x: (x[1]))
        moves_set.add(shuffled_moves[0])
        moves_set.add(shuffled_moves[len(shuffled_moves)-1])
        shuffled_moves.sort(key=lambda x: (x[1]))
        shuffled_moves.sort(key=lambda x: (x[0]))
        moves_set.add(shuffled_moves[0])
        moves_set.add(shuffled_moves[len(shuffled_moves) - 1])
        # Select a random move from the set of valid options.
        random_select = random.randint(0, len(moves_set) - 1)
        selected_coord = list(moves_set)[random_select]
        return move_coords_lookup[selected_coord].pop()

    # When you have run out of valid moves to make, or have otherwise finished your turn
    # return the string "END" to signal that you are done making moves.
    return "END"
