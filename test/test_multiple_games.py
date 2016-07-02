import game.main
from collections import defaultdict

"""
Tests running simulations of players against each other.
"""

win_counts = defaultdict(int)

for n in xrange(1, 101):
    print "Playing game %s of %s" % (n, 100)
    result = game.main.play_game([], ["test_player_01", "test_player_02"], False, False)
    print "Game result: %s" % result
    win_counts[result["Winner"]] += 1

print win_counts
