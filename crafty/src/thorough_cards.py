from card import standard_effect, progress_node
from game import my_player

def play_thorough(stats, game, node):
    player_turn.time_value += stats.cost

    if stats.element == node.truth:
        node.options = [node.truth]
        node.value -= stats.value * 2
        my_player.energy += 3
    elif len(node.options) == 2:
        node.options.remove(stats.element)
        node.value -= stats.value
    else:
        pass #FIX THIS

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