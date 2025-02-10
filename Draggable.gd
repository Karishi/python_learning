extends Node2D
var selected = false
var returning = false
var lastPosition
var dropZones = []

# Called when the node enters the scene tree for the first time.
func _ready():
	dropZones = get_tree().get_nodes_in_group("dropzone")
	lastPosition = dropZones[0].global_position
	dropZones[0].select()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _physics_process(delta):
	if global_position == lastPosition:
		returning = false
	if returning:
		global_position = lerp(global_position, lastPosition, 50 * delta)
	if selected:
		global_position = get_global_mouse_position()

func _on_area_2d_mouse_entered():
	scale.x = 1.05
	scale.y = 1.05

func _on_area_2d_mouse_exited():
	scale.x = 1
	scale.y = 1

func _on_area_2d_input_event(viewport, event, shape_idx):
	if Input.is_action_just_pressed("Click"):
		if !selected:
			selected = true
		else:
			returning = true
			selected = false
