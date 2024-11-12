from card import progress_node, check_victory, Card
from node import node_list
from event import player_turn
from game import my_game


class Patient_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int) -> None:
        super().__init__(title, time_cost, impact, element, bonus_energy_cost, target = 0)
        self.description = f"({time_cost}) {title} ({element}): Has {impact} impact on all nodes. If you pay {bonus_energy_cost} energy the time cost reduces by 3 for each element match."

# Affects every node in the challenge at once.
    def play_card(card, player, game = my_game):
        player_turn.time_value += card.cost

        for node in node_list:
            if node.true_element == card.element:
                player_turn.time_value -= int(card.cost/4)
            node_complete = progress_node(card.value, card.element, node)
            if node_complete:
                game.num_incomplete -= 1


# stats = Card("Patient Cut", 8, 5, "X", 0)