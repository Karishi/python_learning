import random

def counted_roses():
    rose_cards = [1,2,3,4,5,6,7,8,9]
    left_cards = []
    right_cards = []
    
    def move_cards(target, number):
        for i in range(number):
            pick = random.choice(rose_cards)
            target.append(pick)
            rose_cards.remove(pick)
    
    move_cards(left_cards, 3)
    move_cards(right_cards, 4)

    for i in range(2):
        print(f"The left side reveals a {left_cards[i]}")
    print("One card remains unknown.")
    for i in range(2):
        print(f"The right side reveals a {right_cards[i]}")
    print("Two cards remain unknown.")
    guess = input("Which side do you think has a higher score? Left, or Right? ")
    print(f"The sum of the left side is {sum(left_cards)}. The sum of the right side is {sum(right_cards)}.")
    winner = "tie"
    if sum(left_cards) > sum(right_cards):
        winner = "left"
        print("Left wins!")
    if sum(right_cards) > sum(left_cards):
        winner = "right"
        print("Right wins!")
    if winner == guess.lower():
        print("You guessed it!")
    else:
        print("Sorry, you got it wrong.")

counted_roses()