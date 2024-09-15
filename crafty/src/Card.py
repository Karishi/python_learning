class Card:
    def __init__(self, title, cost, impact, element) -> None:
        self.title = title
        self.cost = cost
        self.impact = impact
        self.element = element

def standard_effect(card, game, node):
    game.time -= card.cost
    node_complete = progress_node(card.value, card.element, node)
    if node_complete:
        game.num_incomplete -= 1
        check_victory(game)
    

class Gentle_Sort:
    stats = Card("Gentle Sort", 3, 5, "O")
    def play(self, game, node):
        if game.time > 50:
            standard_effect(self, game, node)
        else:
            if game.status.contains("Relaxed"):
                game.status.remove("Relaxed")
                standard_effect(self, game, node)
            else:
                game.status.append("Relaxed")


