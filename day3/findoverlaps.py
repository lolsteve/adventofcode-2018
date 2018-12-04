class Claim:
    def __init__(self, id, dist_from_left, dist_from_top, width, height):
        self.id = int(id)
        self.dist_from_left = int(dist_from_left)
        self.dist_from_top = int(dist_from_top)
        self.width = int(width)
        self.height = int(height)

    def __str__(self):
        return 'id: {},\ndist_from_left: {},\ndist_from_top: {},\nwidth: {},\nheight: {}'.format(self.id, self. dist_from_left, self.dist_from_top, self.width, self.height)

def read_claim_from_line(string):
    data = string.split(' ')
    id = data[0][1:]
    (dist_from_left, dist_from_top) = data[2].split(',')
    dist_from_top = dist_from_top[:-1]
    (width, height) = data[3].split('x')
    return Claim(id, dist_from_left, dist_from_top, width, height)

def main():
    sheet = [ [0] * 1000 for _ in range(1000)]
    claims = []

    with open('input.txt') as file:
        for line in file:
            claim = read_claim_from_line(line)
            claims.append(claim)

    for claim in claims:
        for i in range(claim.dist_from_left, claim.dist_from_left + claim.width):
            for j in range(claim.dist_from_top, claim.dist_from_top + claim.height):
                sheet[i][j] += 1

    overlaps = 0
    for row in sheet:
        for square in row:
            if square >= 2:
                overlaps += 1

    print(overlaps)

if __name__ == '__main__':
    main()
