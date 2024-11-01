from card import standard_effect, Card, append_element_match
from node import progress_node, node_list
from game import check_victory, my_player, my_game




class Complete_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int, description: str) -> None:
        super().__init__(title, time_cost, impact, element, bonus_energy_cost, target, description)
        title = append_element_match(title, element)
        self.description = f"({time_cost}) {title} ({element}): Has {impact} impact. Gains 10 energy and costs no time if it completes a node."

    def play_card(stats, game, node):
        node_complete = progress_node(stats.value, stats.element, node)
        if node_complete:
            game.num_incomplete -= 1
            game.win_loss = check_victory(game)
            my_player.energy += 10
        else:
            my_player.time += stats.cost
    
    

class Complete_Cut:
    stats = Card("Complete Cut", 8, 8, "X", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_complete(stats, game, node)

