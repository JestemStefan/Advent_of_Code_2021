import timeit


def solution_part_1():
    gamma_ray_bits = ""
    eplison_rate_bits = ""

    

    with open("input_data.txt") as file:
        n_of_rows = len(file)
        print(n_of_rows)
        for line in file:
            line.strip()

            for index, c in enumerate(line):
                pass

    return answer_part_1 or None


def solution_part_2():
    with open("input_data.txt") as file:
        pass

    return answer_part_2 or None


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=1000)/1000}s'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=1000)/1000}s'
    )