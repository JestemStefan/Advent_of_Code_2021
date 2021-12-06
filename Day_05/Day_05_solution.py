import timeit


class Position:
    def __init__(self, coordinates):
        self.x = int(coordinates[0])
        self.y = int(coordinates[1])


class Map:
    def __init__(self):
        self.map = [[0 for x in range(1000)] for y in range(1000)]

    def travel_horizontal(self, start_pos: Position, end_pos: Position):
        sign = 1 if start_pos.x <= end_pos.x else -1
        x_coord = start_pos.x
        y_coord = start_pos.y
        steps = abs(start_pos.x - end_pos.x) + 1

        for _ in range(steps):
            self.map[y_coord][x_coord] += 1
            x_coord += sign

    def travel_vertical(self, start_pos: Position, end_pos: Position):
        sign = 1 if start_pos.y <= end_pos.y else -1
        x_coord = start_pos.x
        y_coord = start_pos.y
        steps = abs(start_pos.y - end_pos.y) + 1

        for _ in range(steps):
            self.map[y_coord][x_coord] += 1
            y_coord += sign




    def travel_diagonal(self, start_pos: Position, end_pos: Position):
        steps = abs(start_pos.x - end_pos.x)
        x_coord = start_pos.x
        y_coord = start_pos.y

        sign_h = 1 if start_pos.x <= end_pos.x else -1
        sign_v = 1 if start_pos.y <= end_pos.y else -1

        self.map[y_coord][x_coord] += 1  # UGH!

        for _ in range(steps):
            y_coord = y_coord + sign_v
            x_coord = x_coord + sign_h

            self.map[y_coord][x_coord] += 1

    def travel(self, start_pos: Position, end_pos: Position):
        if start_pos.y == end_pos.y:
            self.travel_horizontal(start_pos, end_pos)

        elif start_pos.x == end_pos.x:
            self.travel_vertical(start_pos, end_pos)

    def travel_with_diagonals(self, start_pos: Position, end_pos: Position):
        self.travel(start_pos, end_pos)

        if abs(start_pos.x - end_pos.x) == abs(start_pos.y - end_pos.y):
            self.travel_diagonal(start_pos, end_pos)


def solution_part_1():
    solution_part_1 = 0

    map_2d = Map()

    with open("input_data.txt") as file:
        for line in file:
            start_pos, end_pos = line.strip().split(" -> ")

            start_pos = Position(start_pos.split(","))
            end_pos = Position(end_pos.split(","))

            map_2d.travel(start_pos, end_pos)

    for row in map_2d.map:
        for e in row:
            if e >= 2:
                solution_part_1 += 1

    return solution_part_1


def solution_part_2():
    solution_part_2 = 0

    map_2d = Map()

    with open("input_data.txt") as file:
        for line in file:
            start_pos, end_pos = line.strip().split(" -> ")

            start_pos = Position(start_pos.split(","))
            end_pos = Position(end_pos.split(","))

            map_2d.travel_with_diagonals(start_pos, end_pos)

    for row in map_2d.map:
        for e in row:
            if e >= 2:
                solution_part_2 += 1

    return solution_part_2


if __name__ == "__main__":
    print(
        f"Solution = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
    print(
        f"Solution = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )
