
def get_all_valid_moves(game_state):
    """
    :param game_state: GameState: Current state of the game.
    :return: list(Move): A list of valid moves you could make.

    Figures out all the valid moves a player could make at this moment in time.
    """
    valid_moves = game_state.get_valid_moves()
    #for a_move in valid_moves:
    #    a_move.print_move()
    return valid_moves
