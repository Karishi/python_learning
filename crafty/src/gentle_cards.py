from node import progress_node, node_list
from game import check_victory, my_game, my_player
from card import standard_effect, Card

class Gentle_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int, description: str) -> None:
        super().__init__(title, time_cost, impact, element, bonus_energy_cost, target, description)

    def play_card(self, game, node):
# If the player has the energy cost, this card is instant and removes Relaxed status.
        if my_player.energy >= self.bonus:
            my_player.energy -= self.bonus
            if my_player.status.contains("Relaxed"):
                my_player.status.remove("Relaxed")
            temp_cost = self.cost
            self.cost = 0
            standard_effect(self, game, node)
            self.cost = temp_cost
        else:
# Every even time a card of the Gentle type is used the player loses the Relaxed status.
            if my_player.status.contains("Relaxed"):
                my_player.status.remove("Relaxed")
                standard_effect(self, game, node)
# Every odd time a card of Gentle type is used it costs no time and the player gains "Relaxed."
            else:
                my_player.status.append("Relaxed")
                temp_cost = self.cost
                self.cost = 0
                standard_effect(self, game, node)
                self.cost = temp_cost


class Gentle_Cut:
    stats = Card("Gentle Cut", 3, 5, "X", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)


class Gentle_Join:
    stats = Card("Gentle Join", 3, 5, "D", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)


class Gentle_Mix:
    stats = Card("Gentle Mix", 3, 5, "S", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)


class Gentle_Arrange:
    stats = Card("Gentle Arrange", 3, 5, "A", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)


class Gentle_Bind:
    stats = Card("Gentle Bind", 3, 5, "Y", 0)
    game = my_game
    node = node_list[stats.target]
    play_gentle(stats, game, node)