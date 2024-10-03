from card import standard_effect, check_victory, progress_node

def play_deductive(stats, game, node):
    is_discovered = True
    if len(node.options) == 1:
        is_discovered = False
    node_complete = progress_node(stats.value, stats.element, node)
    if node_complete:
        game.num_incomplete -= 1
        game.win_loss = check_victory(game)
    if len(node.options) != 1:
        is_discovered = False
    if is_discovered:
        loss_event.time += stats.cost
    else:
        player_turn.time += stats.cost
    


class Deductive_Sort:
    pass


class Deductive_Cut:
    pass


class Deductive_Join:
    pass


class Deductive_Mix:
    pass


class Deductive_Arrange:
    pass


class Deductive_Bind:
    pass