"""
This is the boilerplate file you start with when you create a new ai player.
"""
from api import helpers

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
    tiles_owned = helpers.get_owned_tiles(game_state, player_number)
    moves_could_make = helpers.get_all_valid_moves(game_state)

    # Sort list of moves.
    shuffled_moves = [[a_move, a_move.get_move_metadata()] for a_move in moves_could_make]
    shuffled_moves.sort(key=lambda x: x[0])
    if len(shuffled_moves) > 0:
        return shuffled_moves[0][0]

    # When you have run out of valid moves to make, or have otherwise finished your turn
    # return the string "END" to signal that you are done making moves.
    return "END"
