import random

class Node:
    def __init__(self, value, truth) -> None:
        self.value = value
        self.truth = truth
        self.options = ["S", "X", "A", "D", "O", "Y"]

def randomize_node(node):
    node.truth = random.choice(node.options)
    return node

def initialize_nonfinal(node, num):
    val = random.randrange(5, int(90 / (num - 1)))
    node.value = val
    return node

def print_node(node):
    print(f"({node.truth})", end = "")
    print(f"({node.value}) ", " ".join(node.options))
    return True

def progress_node(value, element, node):
    if element == node.truth:
        node.options = [node.truth]
        node.value -= value * 2
    else:
        node.options.remove(element)
        node.value -= value
    if node.value <= 0:
        node.value = 0
        return True
    else:
        return False

my_node = Node(10, "A")
my_node = randomize_node(my_node)
my_node = initialize_nonfinal(my_node, 4)
print_node(my_node)
progress_node(8, "A", my_node)
print_node(my_node)
