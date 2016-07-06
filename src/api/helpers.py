
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


def get_owned_tiles(game_state, player_id):
    """
    :param game_state: GameState: Current state of the game.
    :param player_id: int: Player ID of the player you wish to find all tiles
    belonging to.
    :return: list(Tile): All the tiles held by the specified player.
    """
    owned_tiles = game_state.get_held_tiles(player_id)
    return owned_tiles


def get_move_coordinates(move):
    """
    :param move: Move: Object containing data about the move.
    :return: tuple: Coordinates of the tile relating to the move.
    """
    return move.get_move_metadata()["tile_coords"]
