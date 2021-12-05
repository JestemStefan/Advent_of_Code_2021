import timeit

def mark_number_in_grid_if_exist(grid: dict, number: int):
    for row in grid:
        if number in grid[row]:
            grid[row][number] = True
            return


def check_grid_completeness(grid: dict):
    for row in grid:
        if all(list(grid[row].values())):
            return True

    for i in range(5):
        if all([grid[row][list(grid[row].keys())[i]] for row in grid]):
            return True

    return False

def get_grid_sum_times_number(grid: dict, number: int):

    return sum([sum([x for x in grid[r] if not grid[r][x]]) for r in grid]) * number

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
                if number in all_grids[grid][row]:
                    all_grids[grid][row][number] = True

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
        scan_grids = [x for x in list_of_uncomplate_grids]
        for grid_index in scan_grids:
            mark_number_in_grid_if_exist(all_grids[grid_index], number)

            if check_grid_completeness(all_grids[grid_index]):
                if len(list_of_uncomplate_grids) == 1:
                    return get_grid_sum_times_number(all_grids[list_of_uncomplate_grids[0]], number)

                list_of_uncomplate_grids.remove(grid_index)


if __name__ == "__main__":
    print(
        f"Solution = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=100)/100}s'
    )
    print(
        f"Solution = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=100)/100}s'
    )
