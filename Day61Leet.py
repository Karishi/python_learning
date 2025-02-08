def candy(ratings):
    candies = []
    for num in range(len(ratings)):
        candies.append(1)
    
    altered = True
    while altered:
        altered = False
        for num in range(len(ratings)):
            if num > 0 and ratings[num] > ratings[num-1] and candies[num] == candies[num-1]:
                    altered = True
                    candies[num] += 1
            if num < len(ratings)-1 and ratings[num+1] < ratings[num] and candies[num] == candies[num+1]:
                    altered = True
                    candies[num] += 1
    print(candies)
    return sum(candies)

test = [1, 0, 2]

print(candy(test))