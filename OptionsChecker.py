sudokuOptions = {(0,0): [1,2,3,4,5,6,7,8,9]}


for key in sudokuOptions:
    sudokuOptions[key] = [x for x in sudokuOptions[key] if x != sudokuOptions[(0, 0)]]