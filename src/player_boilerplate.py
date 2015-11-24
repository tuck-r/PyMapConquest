"""
This is the boilerplate file you start with when you create a new ai player.
"""
from api import helpers

# A future update may make older scripts incompatible with new versions of the game.
# You shouldn't need to change this value yourself.
VERSION_COMPATIBLE = "0.1"

# Give your ai player a name to use in-game.
PLAYER_NAME = "Some One"

def return_move(game_state, player_number):
    # When you have run out of valid moves to make, or have otherwise finished your turn
    # return the string "END" to signal that you are done making moves.
    return "END"
