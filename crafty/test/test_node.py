from src.node import Node, initialize_nonfinal

def test_initialize_nonfinal():
    my_node = Node(4, "O")
    my_node = initialize_nonfinal(my_node, 4)
    assert my_node.value != 4


