def roman_to_int(roman):
    total = 0
    for digit in range(len(roman)):
        if roman[digit] == "I":
            if digit < len(roman)-1:
                if roman[digit+1] == "V":
                    digit += 1
                    total += 4
                elif roman[digit+1] == "X":
                    digit += 1
                    total += 9
                else:
                    total += 1
            else: 
                total += 1
        if roman[digit] == "X":
            if digit < len(roman)-1:
                if roman[digit+1] == "L":
                    digit += 1
                    total += 40
                elif roman[digit+1] == "C":
                    digit += 1
                    total += 90
                else:
                    total += 10
            else:
                total += 10
        elif roman[digit] == "C":
            if digit < len(roman)-1:
                if roman[digit+1] == "D":
                    digit += 1
                    total += 400
                elif roman[digit+1] == "M":
                    digit += 1
                    total += 900
                else:
                    total += 100
            else: total += 100
        elif roman[digit] == "M":
            total += 1000
        elif roman[digit] == "D":
            total += 500
        elif roman[digit] == "L":
            total += 50
        elif roman[digit] == "V":
            total += 5
    return total

test = "MCM"

print(roman_to_int(test))