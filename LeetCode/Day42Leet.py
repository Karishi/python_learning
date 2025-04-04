def mergeIntervals(intervals):
    intervals.sort()
    index = 0
    while index < len(intervals):
        compare = index + 1
        while compare < len(intervals):
            if intervals[index][1] >= intervals[compare][0]:
                intervals[index][1] = intervals[compare][1]
                del intervals[compare]
            else:
                break

        index += 1
    return intervals
        

test = [[1,4],[4,5],[5,6],[7,9],[9,12],[8,10]]

print(mergeIntervals(test))