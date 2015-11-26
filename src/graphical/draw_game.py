import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOURS = {(255, 0, 0), (0, 255, 0), (0, 0, 255)}

class DrawGame:
    def __init__(self, game_state):
        # Figure out what size each tile should be and the window size.
        self.map_size = game_state.get_map_size()
        self.tile_dims = 30
        self.window_height = self.map_size * self.tile_dims
        self.window_width = self.map_size * self.tile_dims * 2
        self.window_size = (self.window_width, self.window_height)

        # Select a tile colour for each player.
        self.player_colours = {}
        for a_player in game_state.get_player_ids():
            self.player_colours[a_player] = COLOURS.pop()
        self.player_colours[None] = WHITE

        # Initialise drawing surface window.
        self.window_dimensions = self.window_size

        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode(self.window_dimensions)
        pygame.display.set_caption("PyMapConquest")

        # Create game fonts.
        self.font_resources = pygame.font.SysFont("Ariel", 15)
        self.font_player_resources = pygame.font.SysFont("Ariel", 25)

    def draw_game_state(self, game_state):
        tile_array = game_state.get_map_tile_array()
        # Iterate through every tile to draw the game map.
        for a_row in tile_array:
            for a_tile in a_row:
                coords = a_tile.get_coordinates()
                held_by = a_tile.get_is_owned_by()
                # Draw background colour rectangle.
                rect_coords = (coords[0] * self.tile_dims, coords[1] * self.tile_dims, self.tile_dims, self.tile_dims)
                pygame.draw.rect(self.DISPLAYSURF, self.player_colours[held_by], rect_coords)
                # Draw resource numbers in the corners
                # Corners are: {Top Left: Food, Top Right: Wood, Bottom Left: Gold, Bottom Right: Metal}
                resource_vals = a_tile.get_resources()
                label_food = self.font_resources.render(str(resource_vals["Food"]), 1, BLACK)
                self.DISPLAYSURF.blit(label_food,
                                      ((coords[0] * self.tile_dims) + 2,
                                       (coords[1] * self.tile_dims) + 2))
                label_wood = self.font_resources.render(str(resource_vals["Wood"]), 1, BLACK)
                self.DISPLAYSURF.blit(label_wood,
                                      (((coords[0] + 1) * self.tile_dims) - 8,
                                       (coords[1] * self.tile_dims) + 2))
                label_gold = self.font_resources.render(str(resource_vals["Gold"]), 1, BLACK)
                self.DISPLAYSURF.blit(label_gold,
                                      ((coords[0] * self.tile_dims) + 2,
                                       ((coords[1] + 1) * self.tile_dims) - 10))
                label_metal = self.font_resources.render(str(resource_vals["Metal"]), 1, BLACK)
                self.DISPLAYSURF.blit(label_metal,
                                      (((coords[0] + 1) * self.tile_dims) - 8,
                                       ((coords[1] + 1) * self.tile_dims) - 10))

        # Draw black lines to form a grid over the map tiles.
        for i in range(0, self.map_size + 1):
            start_point_vert = (i * self.tile_dims, 0)
            start_point_horz = (0, i * self.tile_dims)
            end_point_vert = (i * self.tile_dims, self.map_size * self.tile_dims)
            end_point_horz = (self.map_size * self.tile_dims, i * self.tile_dims)
            pygame.draw.line(self.DISPLAYSURF, BLACK, start_point_vert, end_point_vert, 1)
            pygame.draw.line(self.DISPLAYSURF, BLACK, start_point_horz, end_point_horz, 1)

        # Draw player status/resources.
        players_resources = game_state.get_players_dict()
        for key_player_id, value_resources in players_resources.items():
            # Get number of tiles held.
            num_tiles_held = len(game_state.get_held_tile_ids(key_player_id))
            # Calculate how wide the status area is on the screen.
            width_of_status_area = self.window_width / 2
            # Divide into a number of segments.
            number_of_segs_needed = 6
            seg_width = width_of_status_area / number_of_segs_needed
            # Write text on the screen.
            # Height will stay the same, width will vary depending on what label is being displayed.
            pos_height = key_player_id * self.tile_dims
            pos_width = self.map_size * self.tile_dims
            # Write player label.
            label_player = self.font_player_resources.render("Player %s" % key_player_id, 1, BLACK)
            self.DISPLAYSURF.blit(label_player, (pos_width, pos_height))
            # Write tiles held label.
            pos_width += seg_width
            label_tiles_held = self.font_player_resources.render("Tiles %s" % num_tiles_held, 1, BLACK)
            self.DISPLAYSURF.blit(label_tiles_held, (pos_width, pos_height))
            # Write resource labels.
            pos_width += seg_width
            label_player_food = self.font_player_resources.render("Food %s" % value_resources["curr_resources"]["Food"],
                                                                  1, BLACK)
            self.DISPLAYSURF.blit(label_player_food, (pos_width, pos_height))
            pos_width += seg_width
            label_player_wood = self.font_player_resources.render("Wood %s" % value_resources["curr_resources"]["Wood"],
                                                                  1, BLACK)
            self.DISPLAYSURF.blit(label_player_wood, (pos_width, pos_height))
            pos_width += seg_width
            label_player_gold = self.font_player_resources.render("Gold %s" % value_resources["curr_resources"]["Gold"],
                                                                  1, BLACK)
            self.DISPLAYSURF.blit(label_player_gold, (pos_width, pos_height))
            pos_width += seg_width
            label_player_metal = self.font_player_resources.render("Metal %s" % value_resources["curr_resources"]["Metal"],
                                                                   1, BLACK)
            self.DISPLAYSURF.blit(label_player_metal, (pos_width, pos_height))

    def update_screen(self, game_state):
        # Clear drawing surface.
        self.DISPLAYSURF.fill(WHITE)
        # Draw game state.
        self.draw_game_state(game_state)
        # Update screen.
        pygame.display.update()

    def quit_game(self):
        pygame.quit()
