from card import standard_effect, check_victory, progress_node

def play_deductive(stats, game, node):
    is_discovered = True

# No bonus if the node is already revealed
    if len(node.options) == 1:
        is_discovered = False
    
    node_complete = progress_node(stats.value, stats.element, node)
    
    if node_complete:
        game.num_incomplete -= 1
        game.win_loss = check_victory(game)
    
# No bonus if the node isn't revealed by this card.
    if len(node.options) != 1:
        is_discovered = False

# Bonus if this card reveals the node's element: It gains time instead of spending it.
    if is_discovered:
        loss_event.time_value += stats.cost
    else:
        player_turn.time_value += stats.cost
    


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