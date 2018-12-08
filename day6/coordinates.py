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

    for point in points:
        grid[point.x][point.y] = point

    for row in grid:
        for cell in row:
            if cell.id == -1:
                min_dist = 9999999
                min_id = -1
                for point in points:
                    dist = manhattan_distance(cell, point)
                    if dist < min_dist:
                        min_dist = dist
                        min_id = point.id
                    elif dist == min_dist:
                        min_id = -1
                cell.id = min_id

    infinite = set()
    areas = [0] * len(points)
    for row in grid:
        for cell in row:
            if (cell.x == 0 or
                cell.y == 0 or
                cell.x == max_x or
                cell.y == max_y):
                infinite.add(cell.id)
                areas[cell.id] = -1
            elif cell.id != -1 and cell.id not in infinite:
                areas[cell.id] += 1

    area = max(areas)
    print(area)

if __name__ == '__main__':
    main()
