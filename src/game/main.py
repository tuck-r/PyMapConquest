from pydoc import locate
import argparse

from game.model.game_state import GameState

# Import path to where user made players are stored and loaded from.
_PLAYERS_PATH = "players"
# Import path to where example players are stored and loaded from.
_PLAYERS_EXAMPLE_PATH = "players_example"

# Limit to the number of invalid moves a player can propose before the game will end their turn for them.
_INVALID_MOVE_LIMIT = 3

def play_game(player_list, player_example_list):
    # Import all player classes that have been added to the game.
    # Each entry in the player_classes list is an instance of that class.
    player_classes = []
    for named_player in player_list:
        player_classes.append(locate(".".join([_PLAYERS_PATH, named_player])))
    for named_player in player_example_list:
        player_classes.append(locate(".".join([_PLAYERS_EXAMPLE_PATH, named_player])))

    # Create a dict of player information.
    dict_players = {}
    player_number = 0
    for a_player in player_classes:
        dict_players[player_number] = {"print_name": a_player.PLAYER_NAME, "class_defs": a_player}
        player_number += 1

    # Cleanup.
    del player_classes
    del player_number

    # Create a new instance of the game state.
    curr_game_state = GameState(dict_players)

    # Used for tracking current players and turn actions.
    curr_player_index = 0
    start_of_turn = True
    count_invalid_moves = 0

    # Start game loop.
    # TODO: Move the game loop logic somewhere else.
    while not curr_game_state.has_game_ended():
        # If it is the start of their turn, update all resources.
        if start_of_turn is True:
            print "Player " + str(curr_player_index) + "'s turn is beginning."
            curr_game_state.start_of_player_turn()
            start_of_turn = False
            print "Player resources updated."

        # Update the player status/options.
        curr_game_state.update_player_status()

        print curr_game_state.get_held_tile_ids(curr_player_index)
        print curr_game_state.get_player_resources(curr_player_index)

        # Select a move.
        proposed_move = dict_players[curr_player_index]["class_defs"].return_move(curr_game_state)

        # Check if move is valid.
        is_move_valid = curr_game_state.is_move_valid(proposed_move)
        if not is_move_valid:
            print "Error: Move selected is not valid."
            count_invalid_moves += 1
        # Player has chosen to end turn or has proposed too many invalid moves.
        if proposed_move == "END" or count_invalid_moves >= _INVALID_MOVE_LIMIT:
            print "Player " + str(curr_player_index) + "'s turn has ended."
            curr_player_index = curr_game_state.end_current_turn()
            start_of_turn = True
            count_invalid_moves = 0
            continue
        # Otherwise if the move is allowed, update the game state with it.
        if is_move_valid:
            print "Player " + str(curr_player_index) + " is making move:"
            print str(proposed_move)
            curr_game_state.make_move(proposed_move)
            count_invalid_moves = 0

    # Game has ended, print end game info.


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--players", help="Players to add to the game.", nargs="*")
    parser.add_argument("--players_example", help="Example players to add to the game.", nargs="*")
    args = parser.parse_args()

    play_game(args.players, args.players_example)
