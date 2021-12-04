import timeit


def solution_part_1():
    gamma_ray_bits = ""
    eplison_rate_bits = ""

    columns = []

    for _ in range(12):
        columns.append(0)

    with open("input_data.txt") as file:
        for line in file:
            line = line.strip()

            for index, c in enumerate(line):
                columns[index] += int(c)

    for value in columns:
        if value > 500:
            gamma_ray_bits += "1"
            eplison_rate_bits += "0"
        else:
            gamma_ray_bits += "0"
            eplison_rate_bits += "1"

    answer_part_1 = int(gamma_ray_bits, 2) * int(eplison_rate_bits, 2)

    return answer_part_1 or None


def filter_list_by_bit_at_index(oxygen_list: list, co2_list: list, index: int):

    if len(oxygen_list) > 1:
        oxygen_bits = [x[index] for x in oxygen_list]
        most_popular_bit_in_oxygen = (
            "1" if oxygen_bits.count("1") >= len(oxygen_bits)/2 else "0"
        )
        oxygen_return = [
            ox for ox in oxygen_list if ox[index] == most_popular_bit_in_oxygen
        ]
    else:
        oxygen_return = oxygen_list

    if len(co2_list) > 1:
        co2_bits = [x[index] for x in co2_list]
        most_popular_bit_in_co2 = "1" if co2_bits.count("1") >= len(co2_bits)/2 else "0"

        co2_return = [c for c in co2_list if c[index] != most_popular_bit_in_co2]
    else:
        co2_return = co2_list

    return oxygen_return, co2_return


def solution_part_2():
    oxygen_lines = []
    co2_lines = []

    columns = [0 for _ in range(12)]

    with open("input_data.txt") as file:
        for line in file:
            line = line.strip()
            oxygen_lines.append(line)
            co2_lines.append(line)

    for i in range(12):
        oxygen_lines, co2_lines = filter_list_by_bit_at_index(
            oxygen_list=oxygen_lines, co2_list=co2_lines, index=i
        )

    answer_part_2 = int(oxygen_lines[0], 2) * int(co2_lines[0], 2)

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
