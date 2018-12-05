DIST_BETWEEN_LOWER_AND_UPPER = abs(ord('A') - ord('a'))

def do_react(a, b):
    return abs(ord(a) - ord(b)) == DIST_BETWEEN_LOWER_AND_UPPER

def run_polymer(polymer):
    i = 1
    while i < len(polymer):
        a = polymer[i-1]
        b = polymer[i]
        if do_react(a, b):
            del polymer[i]
            del polymer[i-1]
            i -= 1
        else:
            i += 1
    return polymer

def main():
    polymer = ""

    with open('input.txt') as file:
        polymer = list(file.read().strip())

    reacted_polymer = run_polymer(polymer[:])

    print('Reacted polymer length: {}'.format(len(reacted_polymer)))

    shortest = len(polymer)
    for i in range(ord('A'), ord('Z')+1):
        upper_case = chr(i)
        lower_case = chr(i + DIST_BETWEEN_LOWER_AND_UPPER)

        filtered_polymer = [unit for unit in polymer if not (unit == lower_case or unit == upper_case)]

        reacted_filtered_polymer = run_polymer(filtered_polymer[:])
        if len(reacted_filtered_polymer) < shortest:
            shortest = len(reacted_filtered_polymer)

    print('Shortest filtered polymer: {}'.format(shortest))

if __name__ == '__main__':
    main()
