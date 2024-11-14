from card import standard_effect, progress_node, Card, append_element_match
from game import check_victory, my_game, query_node
from event import player_turn
from node import node_list


class Thorough_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int) -> None:
        super().__init__(time_cost, impact, element, bonus_energy_cost, target = 0, title = "Thorough ")
        title = append_element_match(title, element)
        self.description = f"({time_cost}) {title} ({element}): Has {impact} impact. If the node is {element} gain 3 Energy. If there are two incorrect elements and the node is not {element}, eliminate an extra element."

    def play_card(card, player, game = my_game):
        node = query_node(node_list)

    # This happens regardless of the rest.    
        node.value -= card.value
        player_turn.time_value += card.cost
        node_complete = False

    # If the element matches, Thorough cards gain energy for the player.
        if card.element == node.truth:
            node.options = [node.truth]
            node.value -= card.value
            player.energy += 3
    # If there are exactly 2 options - correct and incorrect - Thorough is the wrong card to play and does nothing special.
        elif len(node.options) == 2:
            node.options.remove(card.element)
    # If there are 3+ options left, guessing the incorrect element clears an extra wrong answer.
        else:
            node.options.remove(card.element)
            for node in node.options:
                if node.element != node.truth:
                    node.options.remove(node.element)
                    break

        if node.value <= 0:
            node.value = 0
            node_complete = True

        if node_complete:
            game.num_incomplete -= 1
            game.win_loss = check_victory(game)  



# stats = Card("Thorough Cut", 3, 5, "X", 0)
