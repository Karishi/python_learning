from card import progress_node, check_victory
from node import node_list


def play_patient(stats, game):
    player_turn.time_value += stats.cost

    for node in node_list:
        if node.true_element == stats.element:
            player_turn.time_value -= int(stats.cost/4)
        node_complete = progress_node(stats.value, stats.element, node)
        if node_complete:
            game.num_incomplete -= 1
            game.win_loss = check_victory(game)

class Patient_Sort:
    pass

class Patient_Cut:
    pass

class Patient_Join:
    pass

class Patient_Mix:
    pass

class Patient_Arrange:
    pass

class Patient_Bind:
    pass