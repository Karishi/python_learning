def getHint(secret, guess):
    bulls = 0
    cows = 0
    altered = True
    while altered:
        altered = False
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                altered = True
                bulls += 1
                secret = secret[:i] + secret[i+1:]
                guess = guess[:i] + guess[i+1:]
                break
    for i in range(len(guess)):
        if guess[i] in secret:
            cows += 1
            secret = secret[:secret.find(guess[i])] + secret[secret.find(guess[i])+1:]

    return f"{bulls}A{cows}B"

secret = "1123"
guess = "0111"

print(getHint(secret, guess))