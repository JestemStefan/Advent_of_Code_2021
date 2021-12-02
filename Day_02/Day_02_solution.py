import timeit


def solution_part_1():
    horizontal_pos = 0
    depth = 0

    with open("input_data.txt") as file:
        for line in file:
            command, magnitude = line.strip().split()
            magnitude = int(magnitude)

            match command:
                case "forward":
                    horizontal_pos += magnitude

                case "up":
                    depth -= magnitude

                case "down":
                    depth += magnitude

    answer_part_1 = horizontal_pos * depth

    return answer_part_1


def solution_part_2():
    horizontal_pos = 0
    depth = 0
    aim = 0

    with open("input_data.txt") as file:
        for line in file:
            command, magnitude = line.strip().split()
            magnitude = int(magnitude)

            match command:
                case "forward":
                    horizontal_pos += magnitude
                    depth += aim * magnitude

                case "up":
                    aim -= magnitude

                case "down":
                    aim += magnitude

    answer_part_2 = horizontal_pos * depth

    return answer_part_2


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=1000)/1000}s'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=1000)/1000}s'
    )