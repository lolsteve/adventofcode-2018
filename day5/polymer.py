DIST_BETWEEN_LOWER_AND_UPPER = abs(ord('a') - ord('A'))

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

if __name__ == '__main__':
    main()
