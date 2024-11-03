from card import standard_effect, progress_node, Card
from game import my_player, check_victory, my_game
from event import player_turn
from node import node_list


class Thorough_Card(Card):
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int, description: str) -> None:
        super().__init__(title, time_cost, impact, element, bonus_energy_cost, target, description)
        self.description = f"({time_cost}) {title} ({element}): Has {impact} impact. If the node is {element} gain 3 Energy. If there are two incorrect elements and the node is not {element}, eliminate an extra element."

    def play_card(stats, game, node):
    # This happens regardless of the rest.    
        node.value -= stats.value
        player_turn.time_value += stats.cost
        node_complete = False

    # If the element matches, Thorough cards gain energy for the player.
        if stats.element == node.truth:
            node.options = [node.truth]
            node.value -= stats.value
            my_player.energy += 3
    # If there are exactly 2 options - correct and incorrect - Thorough is the wrong card to play and does nothing special.
        elif len(node.options) == 2:
            node.options.remove(stats.element)
    # If there are 3+ options left, guessing the incorrect element clears an extra wrong answer.
        else:
            node.options.remove(stats.element)
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


class Thorough_Cut:
    stats = Card("Thorough Cut", 3, 5, "X", 0)
    game = my_game
    node = node_list[stats.target]
    play_thorough(stats, game, node)


class Thorough_Join:
    stats = Card("Thorough Join", 3, 5, "D", 0)
    game = my_game
    node = node_list[stats.target]
    play_thorough(stats, game, node)


class Thorough_Mix:
    stats = Card("Thorough Mix", 3, 5, "S", 0)
    game = my_game
    node = node_list[stats.target]
    play_thorough(stats, game, node)


class Thorough_Arrange:
    stats = Card("Thorough Arrange", 3, 5, "A", 0)
    game = my_game
    node = node_list[stats.target]
    play_thorough(stats, game, node)


class Thorough_Bind:
    stats = Card("Thorough Bind", 3, 5, "Y", 0)
    game = my_game
    node = node_list[stats.target]
    play_thorough(stats, game, node)