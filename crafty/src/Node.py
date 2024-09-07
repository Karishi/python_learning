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
    val = int(90 / (num - 1))
    node.value = val
    return node

def print_node(node):
    print(f"({node.value})", end = " ")
    print(" ".join(node.options))
    return True

my_node = Node(10, "A")
my_node = randomize_node(my_node)
my_node = initialize_nonfinal(my_node, 4)
print_node(my_node)
