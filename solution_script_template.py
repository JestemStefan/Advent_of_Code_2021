import timeit

def solution_part_1():
    solution_part_1 = 0

    with open("input_data.txt") as file:
        for line in file:
            pass

    return solution_part_1


def solution_part_2():
    solution_part_2 = 0

    with open("input_data.txt") as file:
        for line in file:
            pass


    return solution_part_2


if __name__ == "__main__":
    print(
        f"Solution = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=1000)/1000}s'
    )
    print(
        f"Solution = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=1000)/1000}s'
    )