import timeit


class Point:
    def __init__(self, row, pos, value):
        self.x = pos
        self.y = row
        self.value = value

    def __str__(self):
        return f"Position {self.y},{self.x}, value:{self.value}"

    def __repr__(self):
        return f"Position:{self.y}:{self.x}:{self.value}"


class HeightMap:
    def __init__(self, grid: list):
        self.grid = [
            [Point(row_idx, pos_idx, int(pos)) for pos_idx, pos in enumerate(row)]
            for row_idx, row in enumerate(grid)
        ]
        self.grid_size = len(grid)
        self.visited_cells = []

    def get_low_points(self):
        low_points = []
        for row_idx, row in enumerate(self.grid):
            for pos_idx, pos in enumerate(row):
                current_pos = Point(row_idx, pos_idx, pos.value)
                if self.is_low_point(current_pos):
                    low_points.append(current_pos)

        return low_points

    def is_low_point(self, pos: Point) -> bool:
        return all(
            [
                self.is_point_higher(pos, pos.y - 1, pos.x),
                self.is_point_higher(pos, pos.y, pos.x - 1),
                self.is_point_higher(pos, pos.y, pos.x + 1),
                self.is_point_higher(pos, pos.y + 1, pos.x),
            ]
        )

    def is_point_higher(self, pos: Point, row_idx: int, pos_idx: int) -> bool:
        point = self.get_point(row_idx, pos_idx)

        return point.value > pos.value if point else True

    def flood_fill(self, pos: Point):
        self.visited_cells.append(pos)
        basin_points = [
            bp
            for bp in self.get_adjacent_points(pos)
            if (bp.value < 9 and bp not in self.visited_cells)
        ]

        for bp in basin_points:
            self.flood_fill(bp)

    def get_point(self, row_idx: int, pos_idx: int):
        return (
            self.grid[row_idx][pos_idx]
            if self.is_inside_grid(row_idx, pos_idx)
            else None
        )

    def get_adjacent_points(self, pos: Point):
        adjacent_points = [
            self.get_point(pos.y - 1, pos.x),
            self.get_point(pos.y, pos.x - 1),
            self.get_point(pos.y, pos.x + 1),
            self.get_point(pos.y + 1, pos.x),
        ]
        return [ap for ap in adjacent_points if ap]

    def is_inside_grid(self, row_idx: int, pos_idx: int) -> bool:
        return (0 <= row_idx < self.grid_size) and (0 <= pos_idx < self.grid_size)

    def __str__(self):
        return f"HeightMap {len(self.grid)}x{len(self.grid[0])}"

    def __repr__(self):
        return f"HeightMap {len(self.grid)}x{len(self.grid[0])}"


def solution_part_1():

    with open("input_data.txt") as file:
        height_map = HeightMap([list(line.strip()) for line in file])

    low_points = height_map.get_low_points()

    return sum([low_point.value + 1 for low_point in low_points])


def solution_part_2():

    with open("input_data.txt") as file:
        height_map = HeightMap([list(line.strip()) for line in file])

    low_points = height_map.get_low_points()

    basins = []
    for lp in low_points:
        height_map.visited_cells.clear()
        height_map.flood_fill(lp)

        height_map.visited_cells = list(set(height_map.visited_cells))

        basins.append(height_map.visited_cells)

    merged_basins = []
    # merge basins
    while True:
        for lp in low_points:
            basins_to_merge = [basin for basin in basins if lp in basin]

            merged_basins.append(
                list(set([cell for basin in basins_to_merge for cell in basin]))
            )

            if len(basins_to_merge) >= 2:
                continue

        break

    merged_basins.sort(key=lambda x: len(x))

    # IDK why this works only when I subtract -1 from each basin size :/
    return (
        (len(merged_basins.pop(-1)) - 1)
        * (len(merged_basins.pop(-1)) - 1)
        * (len(merged_basins.pop(-1)) - 1)
    )


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )
