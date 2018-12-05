def main():
    frequencies = []
    frequency = 0
    seen = set([0])

    with open('input.txt') as file:
        for line in file:
            change = int(line.strip())
            frequencies.append(change)

    for change in frequencies:
        frequency += change
        seen.add(frequency)
    print('Sum of frequencies: {}'.format(frequency))

    while True:
        for change in frequencies:
            frequency += change
            if frequency in seen:
                print('First repeated frequency: {}'.format(frequency))
                return
            seen.add(frequency)

if __name__ == '__main__':
    main()
