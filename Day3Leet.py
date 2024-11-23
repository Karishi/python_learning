# Assignment: Convert an integer into what the corresponding column letter-sequence would be on a spreadsheet (1: A, 28: AB, etc)

def numberToColumnCode(num: int):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    over26 = True
    while over26:
        letter = num % 26
        output = alphabet[letter-1] + output
        num = num // 26
        if num == 0:
            over26 = False
    return output

print("Input: 29")
num = 29
output = numberToColumnCode(num)
print("Output: " + output)