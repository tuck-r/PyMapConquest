
class Move:
    def __init__(self, move_type, move_metadata):
        self.move_type = move_type
        self.move_metadata = move_metadata

    def get_move_type(self):
        return self.move_type

    def get_move_metadata(self):
        """
        :return: dict: Data about the move.

        Valid fields:
            - tile_coords
            - building_cost
            - building_name
        """
        return self.move_metadata

    def print_move(self):
        print [self.move_type, self.move_metadata]

    def format_move(self):
        return [self.move_type, self.move_metadata]