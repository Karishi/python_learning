import math

def findLadders(beginWord, endWord, wordList):
    if endWord not in wordList:
        return []
    
    pathList = []

    def recurse(currentWord, path = []):
        if currentWord == endWord:
            pathList.append(path)
            return 
        elif oneOff(currentWord) == []:
            return 
        
        for word in oneOff(currentWord):
            if word not in path:
                path.append(word)
                print(path)
                recurse(word, path)
        

    def oneOff(currentWord):
        differences = 0
        options = []
        
        for word in wordList:
            for letter in range(len(currentWord)):
                if currentWord[letter] != word[letter]:
                    differences += 1
                    if differences > 1:
                        differences = 0
                        break
            if differences == 1:
                options.append(word)
        return options
    
    recurse(beginWord)

    minLength = math.inf
    shortlist = []
    for path in pathList:
        if len(path) < minLength:
            minLength = len(path)
    for path in pathList:
        if len(path) == minLength:
            shortlist.append(path)
    return shortlist

wordList = ["hot","dot","dog","lot","log","cog"]
start = "hit"
end = "cog"

print(findLadders(start, end, wordList))