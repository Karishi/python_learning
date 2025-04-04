def pascals_triangle(numRows):
    list_of_lists = []
    for count in range(1, numRows+1):
        if count == 1:
            list_of_lists.append([1])
        
        else:
            vals = []
            vals.append(1)
            i = 0
            while i < len(list_of_lists[count-2])-1:
                vals.append(list_of_lists[count-2][i] + list_of_lists[count-2][i+1])
                i += 1
            vals.append(1)
            list_of_lists.append(vals)

    return list_of_lists

print(pascals_triangle(5))