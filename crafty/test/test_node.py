from src.Node import *

def test_initialize_nonfinal():
    my_node = Node(4, "O")
    my_node = initialize_nonfinal(my_node)
    assert my_node.value != 4