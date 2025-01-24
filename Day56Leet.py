def combinationSum(candidates, target):

    def recurse(answerSet = [], comb = [], can = 0, sum = 0):
        if sum > target or can == len(candidates):
            if len(comb) > 0:
                comb.pop()
            return answerSet
        
        if sum == target and comb not in answerSet:
            new = []
            for val in comb:
                new.append(val)
            answerSet.append(new)
        
        comb.append(candidates[can])
        recurse(answerSet, comb, can, sum+candidates[can])
        recurse(answerSet, comb, can+1, sum)
        return answerSet
    answerSet = recurse()
    return answerSet

test = [2, 3, 6, 7]

print(combinationSum(test, 7))