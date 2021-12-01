import timeit


def solution_part_1():
    solution_part_1 = 0

    with open("input_data.txt") as file:
        last_value = 9999999999999

        for line in file:
            current_value = int(line)

            if current_value > last_value:
                solution_part_1 += 1

            last_value = current_value

    return solution_part_1


def solution_part_2():
    solution_part_2 = 0

    with open("input_data.txt") as file:
        current_sum = 0

        back = int(file.readline())
        middle = int(file.readline())
        front = int(file.readline())

        last_sum = back + middle + front

        for line in file:
            new_front = int(line)

            current_sum = new_front + front + middle

            if current_sum > last_sum:
                solution_part_2 += 1

            middle = front
            front = new_front

            last_sum = current_sum

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
