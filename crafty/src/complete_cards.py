from card import standard_effect, Card
from node import progress_node, node_list
from game import check_victory, my_player, my_game

def play_complete(stats, game, node):
    node_complete = progress_node(stats.value, stats.element, node)
    if node_complete:
        game.num_incomplete -= 1
        game.win_loss = check_victory(game)
        my_player.energy += 10
    else:
        game.time -= stats.cost
        
        

class Complete_Sort:
    stats = Card("Complete Sort", 8, 8, "O", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_complete(stats, game, node)

class Complete_Cut:
    stats = Card("Complete Cut", 8, 8, "X", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_complete(stats, game, node)

class Complete_Join:
    stats = Card("Complete Join", 8, 8, "D", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_complete(stats, game, node)

class Complete_Mix:
    stats = Card("Complete Mix", 8, 8, "S", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_complete(stats, game, node)

class Complete_Arrange:
    stats = Card("Complete Arrange", 8, 8, "A", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_complete(stats, game, node)

class Complete_Bind:
    stats = Card("Complete Bind", 8, 8, "Y", 6, 0)
    game = my_game
    node = node_list[stats.target]
    play_complete(stats, game, node)