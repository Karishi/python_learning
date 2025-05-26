def canConstruct(ransomNote, magazine):
    for letter in ransomNote:
        if letter not in magazine:
            return False
        else:
            magazine = magazine[:magazine.index(letter)] + magazine[magazine.index(letter)+1:]
    return True

ransom = "Dollar"
mag = "Dola store"

print(canConstruct(ransom, mag))