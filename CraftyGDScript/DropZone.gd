extends Area2D
var cardInSlot = false

func select():
	for child in get_tree().get_nodes_in_group("dropzone"):
		modulate = Color.RED

func deselect():
	modulate = Color.WHITE
	
