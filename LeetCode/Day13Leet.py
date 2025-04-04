# For a list of numbers, find the highest positive disparity between
# any number and those to its right.

list = [7,1,5,3,6,4,9]


def buyLowSellHigh2(list):
    stock = None
    total = 0

    for i in range(len(list)):
        if list[i] < list[i+1] and stock == None:
            # Buy!
            stock = list[i]
            if i+1 == len(list)-1:
                sale = list[i+1] - stock
                total += sale
                return total
        if list[i] > list[i+1] and stock != None:
            # Sell!
            sale = list[i] - stock
            total += sale
            stock = None
            if i+1 == len(list)-1:
                return total
        if list[i] == list[i+1] and i+1 == len(list)-1:
            return total

                
        
print(buyLowSellHigh2(list))