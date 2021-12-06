import timeit

def solution_part_1():
    solution_part_1 = 0
    fish_list = [0 for x in range(9)]
    with open("input_data.txt") as file:
        line = list((map(int, file.readline().strip().split(","))))

        for fish_idx in line:
            fish_list[fish_idx] += 1

    for _ in range(80):
        fish_zero = fish_list.pop(0)
        fish_list.append(fish_zero)
        fish_list[6] += fish_zero

    solution_part_1 = sum(fish_list)

    return solution_part_1


def solution_part_2():
    fish_list = [0 for x in range(9)]
    with open("input_data.txt") as file:
        line = list((map(int, file.readline().strip().split(","))))

        for fish_idx in line:
            fish_list[fish_idx] += 1

    for _ in range(256):
        fish_zero = fish_list.pop(0)
        fish_list.append(fish_zero)
        fish_list[6] += fish_zero

    return sum(fish_list)


if __name__ == "__main__":
    print(
        f"Solution = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=1000)/1000}s'
    )
    print(
        f"Solution = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=1000)/1000}s'
    )