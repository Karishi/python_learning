Game Initializaiton requires a few things.
Board is an object represented by rows and columns.
You start with a homogeneous value, and maintain one character per space, and it works without any fancy formatting.
This may require extra work if it's preferred that I include formatting for extendability - for instance if it needs to be scrollable because 25x25 boards are desirable.
There will actually be 2 boards in the final product: The visible and the hidden/mechanical. During initial testing I'll be working with the hidden, and I'll add the visible as what the player sees once I know coordinates are being correctly identified.

Ship is an object represented based on what I use it for:
Size is an Int used for looping purposes.
Coordinate is a Tuple holding x,y coordinates of the "front" end of the ship. We don't care which end is the front, but the point is it's the side the rest of the ship gets generated from.
Direction is one of 4 values: +x, -x, +y, and -y. I expect for logic-use and ease-of-generalization purposes it'll end up as sets of pairs: (+x,+0) (-x,+0) (+0,+y) (+0,-y)
State is a dictionary, with the segments of the ship as the keys and the binary of "is it okay" as the values.

One of the game values should just be a List of chosen moves. This will allow for a quick check of whether a move is legal. The only illegal moves are "off the edge of the board" and "spaces you've already picked."

Starting from the largest ship, it'll pick a random value on the x and y axes and compare it with a List we make of used spaces. If it's not in there, that'll be the provisional Coordinate value for the ship.
Then it'll pick a direction at random from the 4 options. It'll run a for loop for (Size - 1) spaces offset in that direction or until it hits an illegal space. If it hits an illegal space it'll try the next direction in line until it's tried all 4 or has looped the full Size without hitting anything.
If it is able to find the full size of the ship worth of contiguous empty spaces that are all on the board, it'll put the ship there for real, changing the letters of the hidden board to the ship's representative letter and creating a Ship object containing the size, coordinate, direction, and state information.
There will be a List used for initialization, with coordinates of unused spaces. If a space is found to be unusable it'll be set aside from the list until you change to a smaller ship size. (Game Theory suggests it's more likely you'll get illegal placements and have to repeat work if you start from smaller ships, which in my mind outweighs the value of being able to declare that any space found unusable is permanently unusable)