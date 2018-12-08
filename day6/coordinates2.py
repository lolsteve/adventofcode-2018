import operator

class Point():
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

def manhattan_distance(p1, p2):
    return (abs(p1.x - p2.x) + abs(p1.y - p2.y))

def parse_line(string):
    x, y = string.strip().split(', ')
    return (int(x), int(y))

def main():
    points = []
    with open('input.txt') as file:
        for i, line in enumerate(file):
            x, y = parse_line(line)
            points.append(Point(x, y, i))

    max_x = max(points, key=operator.attrgetter('x')).x
    max_y = max(points, key=operator.attrgetter('y')).y

    grid = [None] * (max_x+1)
    for i in range(max_x+1):
        grid[i] = [None] * (max_y+1)
        for j in range(max_y+1):
            grid[i][j] = Point(i, j, -1)

    #for point in points:
    #    grid[point.x][point.y] = point

    max_dist = 10000
    region_size = 0
    for row in grid:
        for cell in row:
            total_dist = 0
            for point in points:
                total_dist += manhattan_distance(cell, point)
            if total_dist < max_dist:
                region_size += 1

    print(region_size)

if __name__ == '__main__':
    main()
