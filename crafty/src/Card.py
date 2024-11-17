from node import progress_node, num_incomplete

class Card:
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int) -> None:
        self.title = title
        self.cost = time_cost
        self.impact = impact
        self.element = element
        self.bonus = bonus_energy_cost
        self.target = target
        self.description = ""


def standard_effect(card, player, node):
    player.time += card.cost
    node_complete = progress_node(card.value, card.element, node)
    if node_complete:
        num_incomplete -= 1
    


def draw(hand, deck):
    hand.append(deck.pop(0))


def draw_hand(hand, deck, hand_size):
    for i in range(hand_size):
        draw(hand, deck)



def print_card(card):
    print(f"{card.title} ({card.cost}) [{card.element}]")
    print(card.description)

def append_element_match(type, element):
        if element == "O":
            element_name = " Sort"
        elif element == "X":
            element_name = " Cut"
        elif element == "D":
            element_name = " Join"
        elif element == "S":
            element_name = " Mix"
        elif element == "A":
            element_name = " Arrange"
        elif element == "Y":
            element_name = " Bind"
        type += element_name
        return type