def getPermutation(n, k):
    nstring = ""
    for i in range(n):
        nstring += str(i+1)
    
    def buildup(index, nstring, full_list):
        if index == len(nstring):
            full_list.append("".join(nstring))

        for i in range(index, len(nstring)):
            nstring[index], nstring[i] = nstring[i], nstring[index]
            buildup(index+1, nstring, full_list)
            nstring[index], nstring[i] = nstring[i], nstring[index]
    
    def listPermutations(nstring):
        full_list = []

        buildup(0, list(nstring), full_list)

        full_list.sort()

        return full_list
    
    return listPermutations(nstring)[k-1]

testN = 8
testK = 70

print(getPermutation(testN, testK))