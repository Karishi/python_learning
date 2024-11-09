from card import standard_effect, Card, append_element_match
from node import progress_node, node_list
from game import check_victory, player, my_game, query_node




class Complete_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int) -> None:
        super().__init__(title, time_cost, impact, element, bonus_energy_cost, target = 0)
        title = append_element_match(title, element)
        self.description = f"({time_cost}) {title} ({element}): Has {impact} impact. Gains 10 energy and costs no time if it completes a node."

    def play_card(card, game = my_game):
        node = query_node(node_list)
        node_complete = progress_node(card.value, card.element, node)
        if node_complete:
            game.num_incomplete -= 1
            game.win_loss = check_victory(game)
            player.energy += 10
        else:
            player.time += card.cost
    
    

class Complete_Cut:
    stats = Card("Complete Cut", 8, 8, "X", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_complete(stats, game, node)

