from card import standard_effect, Card
from node import node_list, query_node
from event import Loss_Event



class Desperate_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int) -> None:
        super().__init__(title, time_cost, impact, element, bonus_energy_cost, target = 0)
        self.description = f"({time_cost}) {title} ({element}): Has {impact} impact. The less Time is remaining the more Impact this has, to a max of 50% (doubled if you pay {bonus_energy_cost})."

# Increases in power the more time has already been spent, to a maximum of +50% at 50% of time being spent.
    def play_card(card, player, node, game):
        node = query_node(node_list)
        for item in game.timeline:
            if isinstance(item, Loss_Event):
                halfway_point = int(item.time_value/2)

        # Sets the maximum value to +50%
        time_used = min(player.time, halfway_point)
        
        # If energy is spent, the bonus doubles (+100% value at 50% or lower remaining time)
        if player.energy >= 6:
            time_used *= 2
            player.energy -= 6
        
        # Sets the impact of the card to the new value.
        placeholder = card.impact        
        card.impact = card.impact + int(card.impact * (time_used/100))
        
        # Performs the normal reduction of Node value by card Impact value
        game.win_loss = standard_effect(card, game, node)

        # Returns the card to its normal state in case you draw it again in the same game.
        card.impact = placeholder


# stats = Card("Desperate Cut", 12, 8, "X", 6, 0)
