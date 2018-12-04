def drop_char_at_index(index):
    def drop_char(string):
        chars = list(string)
        del chars[index]
        return ''.join(chars)
    return drop_char

def check_for_dups(ids):
    return len(ids) != len(set(ids))

def find_duplicates(ids):
    seen = set()
    for id in ids:
        if id in seen:
            return id
        seen.add(id)

def main():
    with open('input.txt') as file:
        ids = [x.strip() for x in file.readlines()]
        for i in range(len(ids[0])):
            dropped = list(map(drop_char_at_index(i), ids))
            if check_for_dups(dropped):
                print(find_duplicates(dropped))
                return
        print('not found')

if __name__ == "__main__":
    main()
