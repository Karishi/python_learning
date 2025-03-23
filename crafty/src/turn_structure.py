def turn(board, cards, game):
    # 'board' consists of all board-state information
    # 'cards' consists of all cards in deck, hand, discard, collection, and cardbase - a dict of 5 lists
    # 'game' is a collection of fundamental actions - odds are it'll be removed from this function
    # and this function will be put into it instead.
    # 'player' may eventually be introduced but not before there is more than 1 player.
    
# Show the node list from the board, ask the player to select one.
    count = 0
    for node in board.nodes:
        count += 1
        print(f"{count} - {node}")
    targetChoice = input("Select a target for your card. > ")
    chosen_node = board[targetChoice - 1]
# Show the player their hand, ask them to select a card to target the node.
    count = 0
    for card in cards.hand:
        count += 1
        print(f"{count} - {card}")
    cardChoice = input("Select a card to use on the node. > ")
    chosen_card = cards.hand[cardChoice - 1]

# Perform the basic effects all cards share. 
# Should make cards perform individual effects through ducktyping.
    chosen_node.requirement -= chosen_card.impact
    # If the card newly reduces a node to 0, mark it complete and check for victory.
    if chosen_node.requirement <= 0 and not chosen_node.complete:
        chosen_node.complete = True
        board.complete += 1
        if board.complete >= len(board.nodes):
            game.win()
    # If the player hasn't won, check whether they ran out of time and lost instead.
    board.time -= chosen_card.timeCost
    if board.time <= 0:
        game.lose()
    # Finally, discard the hand and draw a new hand of cards.
    game.discard()
    game.draw()
    