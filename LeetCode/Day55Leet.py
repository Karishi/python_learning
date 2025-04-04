def countAndSay(n):
    said = "1"
    
    if n == 1:
        return said

    for i in range(n-1):
        index = 0
        newSaid = ""

        print(said)
        
        count = 0
        

        for x in range(len(said)):
            curr = said[x]
            count += 1
            if x == len(said) -1:
                newSaid += str(count) + curr
            elif curr != said[x+1]:
                newSaid += str(count) + curr
                count = 0

        said = newSaid
                

    return said

print(countAndSay(6))