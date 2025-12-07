def load_data(filename: str, is_raw: bool = False) -> list[str]:
    return [line.strip("\n") if is_raw else line.strip() for line in open(filename, "r").readlines()]


def solve_part_1(data: list[str]) -> int:
    fresh_ingredient_ranges = []
    i = 0
    while data[i] != '':
        _start, _end = map(int, data[i].split('-'))
        fresh_ingredient_ranges.append([_start, _end])
        i += 1
    i += 1
    ans = 0
    while i < len(data):
        _id = int(data[i])
        if any(_start <=_id <= _end for _start, _end in fresh_ingredient_ranges):
            ans += 1
        i += 1
    return ans


def solve_part_2(data: list[str]) -> int:
    fresh_ingredient_ranges = []
    i = 0
    while data[i] != '':
        _start, _end = map(int, data[i].split('-'))
        fresh_ingredient_ranges.append([_start, _end])
        i += 1
    fresh_ingredient_ranges.sort()
    ranges = fresh_ingredient_ranges
    unique_ranges = []
    current_start, current_end = ranges[0]
    for i in range(1, len(ranges)):
        next_start, next_end = ranges[i]
        if current_end >= next_start:
            current_end = max(current_end, next_end)
        else:
            unique_ranges.append([current_start, current_end])
            current_start, current_end = next_start, next_end
    unique_ranges.append([current_start, current_end])
    ans = sum(_end - _start + 1 for _start, _end in unique_ranges)
    return ans


if __name__ == '__main__':
    test_data_filename = "test_input.txt"
    test_data = load_data(test_data_filename)
    ans_part_1 = solve_part_1(test_data)
    print(ans_part_1)
    ans_part_2 = solve_part_2(test_data)
    print(ans_part_2)
