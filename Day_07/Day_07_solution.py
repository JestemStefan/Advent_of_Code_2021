import timeit

def solution_part_1():

    with open("input_data.txt") as file:
        # load input
        crabs_h_positions = list(map(int, file.readline().strip().split(",")))

        # sort list so we can get the middle element
        line = sorted(crabs_h_positions)

        middle_position = line[len(line)//2]

        # calculate cost
        return sum([abs(x - middle_position) for x in line])


def solution_part_2():

    with open("input_data.txt") as file:
        # load input
        crabs_h_positions = list(map(int, file.readline().strip().split(",")))

        average_h = sum(crabs_h_positions)//len(crabs_h_positions)

        total_cost = 0
        for pos in crabs_h_positions:
            n_of_changes = abs(pos - average_h)
            cost = (n_of_changes * (n_of_changes + 1))/2
            total_cost += cost

        return total_cost

if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=1000)/1000}s'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=1000)/1000}s'
    )