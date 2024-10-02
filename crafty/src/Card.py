from node import progress_node, node_list
from game import check_victory, my_game

class Card:
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int) -> None:
        self.title = title
        self.cost = time_cost
        self.impact = impact
        self.element = element
        self.bonus = bonus_energy_cost
        self.target = target


def standard_effect(card, game, node):
    game.time -= card.cost
    node_complete = progress_node(card.value, card.element, node)
    if node_complete:
        game.num_incomplete -= 1
        game.win_loss = check_victory(game)


def play_gentle(self, game, node):
    if game.status.contains("Relaxed"):
        game.status.remove("Relaxed")
        standard_effect(self, game, node)
    else:
        game.status.append("Relaxed")
        temp_cost = self.cost
        self.cost = 0
        standard_effect(self, game, node)
        self.cost = temp_cost


def draw(hand, deck):
    hand.append(deck.pop(0))


def draw_hand(hand, deck, hand_size):
    for i in range(hand_size):
        draw(hand, deck)


class Gentle_Sort:
    stats = Card("Gentle Sort", 3, 5, "O", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)


class Gentle_Cut:
    stats = Card("Gentle Cut", 3, 5, "X", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)


class Gentle_Join:
    stats = Card("Gentle Join", 3, 5, "D", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)


class Gentle_Mix:
    stats = Card("Gentle Mix", 3, 5, "S", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)


class Gentle_Arrange:
    stats = Card("Gentle Arrange", 3, 5, "A", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)


class Gentle_Bind:
    stats = Card("Gentle Bind", 3, 5, "Y", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)