def letterCombinations(digits):
    phoneDict = {
        2: ["a","b","c"],
        3: ["d","e","f"],
        4: ["g","h","i"],
        5: ["j","k","l"],
        6: ["m","n","o"],
        7: ["p","q","r","s"],
        8: ["t","u","v"],
        9: ["w","x","y","z"]
        }
    combinations = set()

    def recursiveAdd(string = "", index = 0, letter = 0):
        if len(string) == len(digits):
            combinations.add(string)
            string = ""
            return

        for i in range(len(phoneDict[digits[index]])):
            recursiveAdd(string + phoneDict[digits[index]][letter+i], index + 1, letter)   
    
    recursiveAdd()
    return combinations

test = [2,3]

print(letterCombinations(test))