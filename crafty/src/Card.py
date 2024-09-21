from node import progress_node
from game import check_victory, my_game, node_list

class Card:
    def __init__(self, title: str, cost: int, impact: int, element: str, bonus: int) -> None:
        self.title = title
        self.cost = cost
        self.impact = impact
        self.element = element
        self.bonus = bonus

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

class Gentle_Sort:
    stats = Card("Gentle Sort", 3, 5, "O")
    game = my_game
    node = node_list[input("Which node will you target? > ")]
    play_gentle(stats, game, node)

class Gentle_Cut:
    stats = Card()


