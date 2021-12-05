import timeit

def mark_number_in_grid_if_exist(grid: dict, number: int):
    for row in grid:
        for e in grid[row]:
            if number == e:
                grid[row][e] = True
                if number == 59:
                    pass


def check_grid_completeness(grid: dict):
    rows_in_grid = [[grid[row][e] for e in grid[row]] for row in grid]
    columns_in_grid = [[grid[row][list(grid[row].keys())[i]] for row in grid] for i in range(5)]

    if any([all(row) for row in rows_in_grid]) or any([all(column) for column in columns_in_grid]):
        return True

    return False

def get_grid_sum_times_number(grid: dict, number: int):
    sum_of_grid = 0
    for r in grid:
        sum_of_grid += sum([x for x in grid[r] if not grid[r][x]])

    return sum_of_grid * number

def solution_part_1():
    solution_part_1 = 0

    drawn_numbers = []

    all_grids = {}

    with open("input_data.txt") as file:

        drawn_numbers = file.readline().strip().split(",")
        drawn_numbers = list(map(int, drawn_numbers))

        file.readline()  # empty line skip

        grid = {}
        grid_idx = 0
        row_idx = 0

        for line in file:
            line = list(map(int, line.strip().split()))

            if not line:
                all_grids[grid_idx] = grid
                grid = {}
                grid_idx += 1
                row_idx = 0
            else:
                grid[row_idx] = {
                    line[0]: False,
                    line[1]: False,
                    line[2]: False,
                    line[3]: False,
                    line[4]: False,
                }
                row_idx += 1


    for number in drawn_numbers:

        for grid in all_grids:
            for row in all_grids[grid]:
                for e in all_grids[grid][row]:

                    if number == e:
                        all_grids[grid][row][e] = True

                        if all([all_grids[grid][row][x] for x in all_grids[grid][row]]):

                            return get_grid_sum_times_number(all_grids[grid], number)



def solution_part_2():
    solution_part_2 = 0

    drawn_numbers = []

    all_grids = {}

    with open("input_data.txt") as file:

        drawn_numbers = file.readline().strip().split(",")
        drawn_numbers = list(map(int, drawn_numbers))

        file.readline()  # empty line skip

        grid = {}
        grid_idx = 0
        row_idx = 0

        for line in file:
            line = list(map(int, line.strip().split()))

            if not line:
                all_grids[grid_idx] = grid
                grid = {}
                grid_idx += 1
                row_idx = 0
            else:
                grid[row_idx] = {
                    line[0]: False,
                    line[1]: False,
                    line[2]: False,
                    line[3]: False,
                    line[4]: False,
                }
                row_idx += 1

    list_of_uncomplate_grids = [x for x in range(100)]

    for number in drawn_numbers:

        for grid_index in all_grids:
            if grid_index in list_of_uncomplate_grids:
                mark_number_in_grid_if_exist(all_grids[grid_index], number)

                if check_grid_completeness(all_grids[grid_index]):
                    if grid_index in list_of_uncomplate_grids:
                        if len(list_of_uncomplate_grids) == 1:
                            return get_grid_sum_times_number(all_grids[list_of_uncomplate_grids[0]], number)

                        list_of_uncomplate_grids.remove(grid_index)


if __name__ == "__main__":
    print(
        f"Solution = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
    print(
        f"Solution = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )
