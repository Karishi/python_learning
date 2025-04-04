def rotateImage(array):
    processed = []
    to_do = []
    for i in array:
        for j in i:
            while len(to_do) > 0 and (i,j) not in processed:
                