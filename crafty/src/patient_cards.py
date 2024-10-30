from card import progress_node, check_victory, Card
from node import node_list
from event import player_turn
from game import my_game


def play_patient(stats, game):
    player_turn.time_value += stats.cost

    for node in node_list:
        if node.true_element == stats.element:
            player_turn.time_value -= int(stats.cost/4)
        node_complete = progress_node(stats.value, stats.element, node)
        if node_complete:
            game.num_incomplete -= 1
            game.win_loss = check_victory(game)

class Patient_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int, description: str) -> None:
        super().__init__(title, time_cost, impact, element, bonus_energy_cost, target, description)

# Affects every node in the challenge at once.
    def play_patient(stats, game):
        player_turn.time_value += stats.cost

        for node in node_list:
            if node.true_element == stats.element:
                player_turn.time_value -= int(stats.cost/4)
            node_complete = progress_node(stats.value, stats.element, node)
            if node_complete:
                game.num_incomplete -= 1

class Patient_Cut:
    stats = Card("Patient Cut", 8, 5, "X", 0)
    game = my_game
    node = node_list[stats.target]
    play_patient(stats, game, node)


class Patient_Join:
    stats = Card("Patient Join", 8, 5, "D", 0)
    game = my_game
    node = node_list[stats.target]
    play_patient(stats, game, node)


class Patient_Mix:
    stats = Card("Patient Mix", 8, 5, "S", 0)
    game = my_game
    node = node_list[stats.target]
    play_patient(stats, game, node)


class Patient_Arrange:
    stats = Card("Patient Arrange", 8, 5, "A", 0)
    game = my_game
    node = node_list[stats.target]
    play_patient(stats, game, node)


class Patient_Bind:
    stats = Card("Patient Bind", 8, 5, "Y", 0)
    game = my_game
    node = node_list[stats.target]
    play_patient(stats, game, node)
