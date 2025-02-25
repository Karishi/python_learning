extends Node2D
const HAND_COUNT = 8
const CARD_SCENE_PATH = "res://draggable.tscn"
const CARD_WIDTH = 100


var player_hand = []
var center_screen_x
var hand_y_position
# Called when the node enters the scene tree for the first time.
func _ready():
	center_screen_x = get_viewport().size.x / 2
	hand_y_position = get_viewport().size.y / 1.1
	var card_scene = preload(CARD_SCENE_PATH)
	for i in range(HAND_COUNT):
		var new_card = card_scene.instantiate()
		$"../CardManager".add_child(new_card)
		new_card.name = "Card"
		add_card_to_hand(new_card)

func add_card_to_hand(card):
	player_hand.insert(0, card)
	update_hand_positions()
	
func update_hand_positions():
	for i in range(player_hand.size()):
		var new_position = Vector2(calculate_card_position(i), hand_y_position)
		var card = player_hand[i]
		animate_card_to_position(card, new_position)
		
func calculate_card_position(index):
	var x_offset = (player_hand.size() - 1) * CARD_WIDTH
	var x_position = center_screen_x + index * CARD_WIDTH - x_offset / 2
	return x_position
# Called every frame. 'delta' is the elapsed time since the previous frame.
func animate_card_to_position(card, new_position):
	var tween = get_tree().create_tween()
	tween.tween_property(card, "position", new_position, 0.1)
