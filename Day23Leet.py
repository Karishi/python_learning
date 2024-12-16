def floodFill(image, y, x, color):
    process = [(y, x)]
    seen = []
    oldColor = image[y][x]
    while len(process) > 0:
        y, x = process.pop(0)
        image[y][x] = color
        if y > 0 and image[y-1][x] == oldColor and (y-1,x) not in seen:
            process.append((y-1, x))
            seen.append((y-1, x))
        if y < len(image)-1 and image[y+1][x] == oldColor and (y+1, x) not in seen:
            process.append((y+1, x))
            seen.append((y+1, x))
        if x > 0 and image[y][x-1] == oldColor and (y, x-1) not in seen:
            process.append((y, x-1))
            seen.append((y, x-1))
        if x < len(image[y])-1 and image[y][x+1] == oldColor and (y, x+1) not in seen:
            process.append((y, x+1))
            seen.append((y, x+1))
    return image

row1 = ["C", "C", "M", "M", "Y", "K"]
row2 = ["M", "M", "M", "C", "Y", "K"]
row3 = ["M", "C", "M", "K", "Y", "C"]
row4 = ["C", "C", "K", "K", "Y", "M"]
picture = [row1, row2, row3, row4]

for row in picture:
    print(row)
print()
updatedPicture = floodFill(picture, 1, 1, "D")
for row in picture:
    print(row)