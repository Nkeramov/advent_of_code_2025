def load_data(filename: str) -> list[str]:
    return [line.strip() for line in open(filename, "r").readlines()]


def solve_part_1(data: list[str]) -> int:
    position = 50
    zero_counter = 0
    for line in data:
        direction, clicks = line[0], int(line[1:])
        sign = [-1, 1]["LR".index(direction)]
        r = clicks % 100
        position = (position + sign * r + 100) % 100
        if position == 0:
            zero_counter += 1
    return zero_counter


def solve_part_2(data: list[str]) -> int:
    position = 50
    zero_counter = 0
    for line in data:
        direction, clicks = line[0], int(line[1:])
        sign = [-1, 1]["LR".index(direction)]
        r = clicks % 100
        zero_counter += clicks // 100
        if r > 0:
            new_position = position + sign * r
            if sign > 0 and new_position >= 100 or sign < 0 and position > 0 and new_position <= 0:
                zero_counter += 1
            position = (new_position + 100) % 100
    return zero_counter


if __name__ == '__main__':
    test_data_filename = "test_input.txt"
    test_data = load_data(test_data_filename)
    ans_part_1 = solve_part_1(test_data)
    print(ans_part_1)
    ans_part_2 = solve_part_2(test_data)
    print(ans_part_2)
