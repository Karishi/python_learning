from card import standard_effect
from node import progress_node
from game import check_victory, my_player

def play_complete(stats, game, node):
    node_complete = progress_node(stats.value, stats.element, node)
    if node_complete:
        game.num_incomplete -= 1
        game.win_loss = check_victory(game)
        my_player.energy += 10
    else:
        game.time -= stats.cost
        
        

class Complete_Sort:
    pass

class Complete_Cut:
    pass

class Complete_Join:
    pass

class Complete_Mix:
    pass

class Complete_Arrange:
    pass

class Complete_Bind:
    pass