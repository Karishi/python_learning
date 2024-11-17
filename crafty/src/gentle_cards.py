from node import progress_node, node_list, query_node
from card import standard_effect, Card

class Gentle_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int) -> None:
        super().__init__(title, time_cost, impact, element, bonus_energy_cost, target = 0)
        self.description = f"({time_cost}) {title} ({element}): Has {impact} impact. Costs no Time each odd time you play Gentle, giving you Relaxed instead. If you pay {bonus_energy_cost} Energy you lose relaxed AND it costs no Time."

    def play_card(card, player, node, game):
        node = query_node(node_list)
# If the player has the energy cost, this card is instant and removes Relaxed status.
        if player.energy >= card.bonus:
            player.energy -= card.bonus
            if player.status.contains("Relaxed"):
                player.status.remove("Relaxed")
            temp_cost = card.cost
            card.cost = 0
            standard_effect(card, game, node)
            card.cost = temp_cost
        else:
# Every even time a card of the Gentle type is used the player loses the Relaxed status.
            if player.status.contains("Relaxed"):
                player.status.remove("Relaxed")
                standard_effect(card, game, node)
# Every odd time a card of Gentle type is used it costs no time and the player gains "Relaxed."
            else:
                player.status.append("Relaxed")
                temp_cost = card.cost
                card.cost = 0
                standard_effect(card, game, node)
                card.cost = temp_cost



# stats = Card("Gentle Cut", 3, 5, "X", 0)
