from card import standard_effect, check_victory, progress_node, Card
from game import my_game, my_player
from node import node_list
from event import Loss_Event

class Deductive_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int, description: str) -> None:
        super().__init__(title, time_cost, impact, element, bonus_energy_cost, target, description)
        self.description = f"({time_cost}) {title} ({element}): Has {impact} impact. If this reveals a Node's element, gain time instead of expending it. If you spend ({bonus_energy_cost}) energy this happens even if the Node's element was already revealed."

    def play_card(stats, game, node):
        is_discovered = True

    # No bonus if the node is already revealed
        if len(node.options) == 1:
            is_discovered = False
        
    # Unless you pay the bonus cost with Energy.
        if my_player.energy >= stats.bonus:
            my_player.energy -= stats.bonus
            is_discovered = True

        node_complete = progress_node(stats.value, stats.element, node)
        
        if node_complete:
            game.num_incomplete -= 1
            game.win_loss = check_victory(game)
        
    # No bonus if the node isn't revealed by this card.
        if len(node.options) != 1:
            is_discovered = False

    # Bonus if this card reveals the node's element: It gains time instead of spending it.
        if is_discovered:
            for item in my_game.timeline:
                if isinstance(item, Loss_Event):
                    time = item.time
            time += stats.cost
        else:
            my_player.time += stats.cost


class Deductive_Cut:
    stats = Card("Deductive Cut", 7, 7, "X", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_deductive(stats, game, node)


