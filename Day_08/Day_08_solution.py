import timeit


def get_encoded_number(line):
    input_data, output_data = line.strip().split(" | ")
    input_data = input_data.split()
    output_data = output_data.split()

    input_data.sort(key=lambda x: len(x))

    mapping = {
        0: [0, 1, 2, 4, 5, 6],
        1: [2, 5],
        2: [0, 2, 3, 4, 6],
        3: [0, 2, 3, 5, 6],
        4: [1, 2, 3, 5],
        5: [0, 1, 3, 5, 6],
        6: [0, 1, 3, 4, 5, 6],
        7: [0, 2, 5],
        8: [0, 1, 2, 3, 4, 5, 6],
        9: [0, 1, 2, 3, 5, 6],
    }

    possible_values = ["abcdefg"] * 7

    mapped_values = {}
    mapped_values[1] = "".join(sorted(input_data.pop(0)))
    mapped_values[7] = "".join(sorted(input_data.pop(0)))
    mapped_values[4] = "".join(sorted(input_data.pop(0)))
    mapped_values[8] = "".join(sorted(input_data.pop(-1)))

    def collapse_for_value(v: int):
        for idx, pos_value in enumerate(possible_values):
            if idx in mapping[v]:
                possible_values[idx] = "".join(
                    [c for c in possible_values[idx] if c in mapped_values[v]]
                )
            else:
                possible_values[idx] = "".join(
                    [c for c in possible_values[idx] if c not in mapped_values[v]]
                )

    for value in mapped_values:
        collapse_for_value(value)

    pass
    # get 3
    for i, seg in enumerate(input_data):
        if len(seg) == 5:
            if all([c in seg for c in mapped_values[1]]):
                mapped_values[3] = "".join(sorted(input_data.pop(i)))
                break

    collapse_for_value(3)

    # get 5
    for i, seg in enumerate(input_data):
        if len(seg) == 5:
            seg = seg.replace(possible_values[0], "")
            seg = seg.replace(possible_values[6], "")
            if len([c for c in mapped_values[4] if c not in seg]) == 1:
                mapped_values[5] = "".join(sorted(input_data.pop(i)))
                break

    collapse_for_value(5)

    # decode all digits
    for digit in mapping:
        code = ""
        for map_segment in mapping[digit]:
            code += possible_values[map_segment]

        mapped_values[digit] = "".join(sorted(code))

    number = 0
    for output in output_data:

        for encoded_num in mapped_values:
            if mapped_values[encoded_num] == "".join(sorted(output)):
                number = number * 10 + encoded_num
                break

    return number


def solution_part_1():
    solution_part_1 = 0

    with open("input_data.txt") as file:
        for line in file:
            _, output = line.strip().split(" | ")
            output = output.split()

            for segment in output:
                if len(segment) in (2, 3, 4, 7):
                    solution_part_1 += 1

    return solution_part_1


#    0000
#   1    2
#   1    2
#    3333      index of each segment
#   4    5
#   4    5
#    6666


def solution_part_2():
    return sum([get_encoded_number(line) for line in open("input_data.txt")])


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=1000)/1000}s'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=1000)/1000}s'
    )
