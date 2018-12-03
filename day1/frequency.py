frequency = 0

with open('input.txt') as file:
    for line in file:
        sign = line[:1]
        number = int(line[1:])
        if sign is '+':
            frequency += number
        else:
            frequency -= number

print(frequency)
