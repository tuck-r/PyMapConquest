import pstats
import cProfile

from game.main import play_game

cProfile.runctx("play_game([], [\"test_player_01\", \"test_player_02\"])", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
