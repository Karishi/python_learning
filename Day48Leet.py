# find max "water" area between any pair of lines on a bar graph
# water area is defined as later-earlier for width * the shorter of the two for height,
# as if they were the two sides of a container
def maxArea(height):
    index = 0 # For testing all options on the left side
    heightMax = 0
    while index < len(height):
        for i in range(index+1, len(height)):
            value = (i - index) * min(height[i], height[index])
            if value > heightMax:
                heightMax = value
        index += 1
    return heightMax

test = [1,8,6,2,5,4,8,3,7]

print(f"For this graph, {maxArea(test)} is the biggest container possible.")