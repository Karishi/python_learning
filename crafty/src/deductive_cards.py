from card import standard_effect, check_victory, progress_node, Card
from game import my_game
from node import node_list

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
    stats = Card("Deductive Sort", 7, 7, "O", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_deductive(stats, game, node)


class Deductive_Cut:
    stats = Card("Deductive Cut", 7, 7, "X", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_deductive(stats, game, node)


class Deductive_Join:
    stats = Card("Deductive Join", 7, 7, "D", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_deductive(stats, game, node)


class Deductive_Mix:
    stats = Card("Deductive Mix", 7, 7, "S", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_deductive(stats, game, node)


class Deductive_Arrange:
    stats = Card("Deductive Arrange", 7, 7, "A", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_deductive(stats, game, node)


class Deductive_Bind:
    stats = Card("Deductive Bind", 7, 7, "Y", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_deductive(stats, game, node)