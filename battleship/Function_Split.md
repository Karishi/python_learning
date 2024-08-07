Planning document for keeping my thoughts straight as I split out each of the functions into subfiles. For instance, does the thing that places Ships on the Board go into Ship or Board? I include reasoning when I feel the answer isn't immediately obvious.

Make Board (Board): Makes a board of size width x height.

Print Board (Board): Draws the board for the user. During testing will be for showing where ships are but in the final product will draw the visible board with guesses and their results, instead of the secret board where the ships are.

Alph to Num (Game): Takes a letter and turns it into the matching number of the alphabet -1, ranging from 0-25. Is Game because it's there to enable a during-play behavior (the player writing inputs like "G7" and have them translate into dual-integer coordinates).

Split Coordinates (Game): Slices a string into its first character - the letter, representing the Y axis - and its second and possibly third character(s), the number, representing the X axis. Is Game for the same reason as Alph to Num.

Check Against Unused (Ship): While it does a lot with the board, this is specifically for the ship placement process.

Place Ship (Ship): Places a ship on the board.

Random Direction (Ship): This refers to which way a ship will be pointing from a starting coordinate when placed on the board.

Translate Direction (Ship): This is a helper function that turns the letter "N" or "S" or "E" or "W" into a corresponding coordinate translate (1,0 for "E", for instance).

Randomize Ship Start (Ship - DEPRECATED): Chooses a set of starting coordinates for a ship at random. I believe this will be rewritten to simply grab a random value from the board.unused list of coordinate-pair tuples.

Edge Check (Ship): Safe-checks whether a ship will go off the edge of the board, to avoid crashing.

Random Ships (Game): Bonus feature, introduces the potential for players to add extra ships of various randomized kinds for a longer game/bigger board. Is in Game because its use would be an interactive feature.

Name Ship (Game): A helper function for Random Ships to apply letters to each kind of ship that gets randomly generated.

Place Basic Ships (Game): Initialize the game, placing the typical 5 ships (Destroyer, Cruiser, Submarine, Battleship, and Carrier) on the board.