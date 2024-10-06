from card import standard_effect, progress_node
from game import my_player

def play_thorough(stats, game, node):
# This happens regardless of the rest.    
    node.value -= stats.value
    player_turn.time_value += stats.cost

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
        return True

    if node_complete:
        game.num_incomplete -= 1
        game.win_loss = check_victory(game)    


class Thorough_Sort:
    pass

class Thorough_Cut:
    pass

class Thorough_Join:
    pass

class Thorough_Mix:
    pass

class Thorough_Arrange:
    pass

class Thorough_Bind:
    pass