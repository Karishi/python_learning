def hIndex(citations):
    citations.sort()
    best = 0
    for i in range(len(citations)):
        if len(citations[i:]) >= citations[i]:
            best = min(len(citations[i:]), citations[i])
    return best

citations = [3,0,6,1,5]

print(hIndex(citations))