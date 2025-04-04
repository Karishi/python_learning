def hIndex(citations):
    # citations.sort()
    # best = 0
    # for i in range(len(citations)):
    #     if len(citations[-(i+1):]) <= citations[-(i+1)]:
    #         best = min(len(citations[-(i+1):]), citations[-(i+1)])
    #     else:
    #         return best
    # return best
    best = 0
    listed = [0 for x in range(len(citations))]
    for i in range(len(citations)):
        if citations[i] > best:
            for j in range(min(citations[i], len(citations)+1)):
                print(listed, best)
                listed[j] += 1
                if listed[j] > j:
                    best = min(listed[j], j+1)
    return best

citations = [3,1,1,3]

print(hIndex(citations))