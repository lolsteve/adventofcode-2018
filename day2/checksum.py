hasTwo = 0
hasThree = 0

with open('input.txt') as file:
    for line in file:
        localOnes = []
        localTwos = []
        localThrees = []
        localMore = []
        for letter in line:
            if letter in localOnes:
                localTwos.append(letter)
                localOnes.remove(letter)
            elif letter in localTwos:
                localThrees.append(letter)
                localTwos.remove(letter)
            elif letter in localThrees:
                localMore.append(letter)
                localThrees.remove(letter)
            elif letter not in localMore:
                localOnes.append(letter)
        if len(localTwos) > 0:
            hasTwo += 1
        if len(localThrees) > 0:
            hasThree += 1

print(hasTwo*hasThree)
