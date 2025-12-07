def load_data(filename: str, is_raw: bool = False) -> list[str]:
    return [line.strip("\n") if is_raw else line.strip() for line in open(filename, "r").readlines()]


def solve_part_1(data: list[str]) -> int:
    operations = data[-1].split()
    column_result = [1 if operation == '*' else 0 for operation in operations]
    for line in data[:-1]:
        nums = map(int, line.split())
        for i, num in enumerate(nums):
            if operations[i] == "*":
                column_result[i] *= num
            else:
                column_result[i] += num
    ans = sum(column_result)
    return ans


def solve_part_2(data: list[str]) -> int:
    operations = data[-1][::-1].split()
    column_result = [1 if operation == '*' else 0 for operation in operations]
    data = zip(*[line[::-1] for line in data[:-1]])
    i = 0
    for line in data:
        if all(c == " " for c in line):
            i += 1
        else:
            num = int(''.join(line))
            if operations[i] == "*":
                column_result[i] *= num
            else:
                column_result[i] += num
    ans = sum(column_result)
    return ans


if __name__ == '__main__':
    test_data_filename = "test_input.txt"
    test_data = load_data(test_data_filename, True)
    ans_part_1 = solve_part_1(test_data)
    print(ans_part_1)
    ans_part_2 = solve_part_2(test_data)
    print(ans_part_2)
