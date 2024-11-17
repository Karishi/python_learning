import random
import logging

node_list = []
num_incomplete = 0

class Node:
    def __init__(self, value: int, truth: str) -> None:
        self.value = value
        self.current = value
        self.true_element = truth
        self.options = ["S", "X", "A", "D", "O", "Y"]

def randomize_node(node):
    node.truth = random.choice(node.options)
    return node

def initialize_nonfinal(node, num):
    val = random.randrange(5, int(90 / (num - 1)))
    node.value = val
    return node

def initialize_full(num):
    node_val_total = 0
    num_incomplete = num

    for i in range(num-1):
        node = Node(10, "A")
        randomize_node(node)
        node_list.append(initialize_nonfinal(node, num))
        node_val_total += node.value

    node = Node(100 - node_val_total, "A")
    randomize_node(node)
    node_list.append(node)

    return node_list

def print_node(node):
    # print(f"({node.truth})", end = "")
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
    
def print_board():
    for node in node_list:
        print_node(node)

def query_node(node_list):
    node_number = 0
    for node in node_list:
        node_number += 1
        print(f"({node_number}): ", end = "")
        print_node(node)
    selected_number = input("Please select a target. > ")
    return selected_number