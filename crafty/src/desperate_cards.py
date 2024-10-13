from card import standard_effect, Card
from game import my_game, my_player
from node import node_list
from event import Event
from player import Player

""" Desperate: Desperate cards increase in effect the less time you have left. They have a weak effect when the attempt starts, but increase in impact to a maximum value at 50%. At the same time, when you hit 50%, they switch from targeting a single node to hitting all of them. Desperate cards have no Bonus effect, but cause you to gain 1 energy for every 5 time you've spent. """

def play_desperate(stats, game, node):
    time_used = min(my_game.time, 50)
    if my_player.energy >= 6:
        time_used *= 2
        my_player.energy -= 6
    stats.impact = stats.impact + int(stats.impact * (time_used/100))
    standard_effect(stats, game, node)


class Desperate_Sort:
    stats = Card("Desperate Sort", 12, 8, "O", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_desperate(stats, game, node)


class Desperate_Cut:
    stats = Card("Desperate Cut", 12, 8, "X", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_desperate(stats, game, node)


class Desperate_Join:
    stats = Card("Desperate Join", 12, 8, "D", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_desperate(stats, game, node)


class Desperate_Mix:
    stats = Card("Desperate Mix", 12, 8, "S", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_desperate(stats, game, node)


class Desperate_Arrange:
    stats = Card("Desperate Arrange", 12, 8, "A", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_desperate(stats, game, node)


class Desperate_Bind:
    stats = Card("Desperate Bind", 12, 8, "Y", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_desperate(stats, game, node)