def load_data(filename: str) -> list[str]:
    return [line.strip() for line in open(filename, "r").readlines()]


def solve_part_1(data: list[str]) -> int:
    ranges = data[0].split(",")
    ans = 0
    for _range in ranges:
        id_start, id_end = map(int, _range.split("-"))
        for _id in range(id_start, id_end + 1):
            s = str(_id)
            if len(s) % 2 == 0 and s[: len(s) // 2] * 2 == s:
                ans += _id
    return ans


def solve_part_2(data: list[str]) -> int:
    ranges = data[0].split(",")
    ans = 0
    for _range in ranges:
        id_start, id_end = map(int, _range.split("-"))
        for _id in range(id_start, id_end + 1):
            s = str(_id)
            s_len = len(s)
            for i in range(1, s_len // 2 + 1):
                if s_len % i == 0 and s[:i] * (s_len // i) == s:
                    ans += _id
                    break
    return ans



if __name__ == '__main__':
    test_data_filename = "test_input.txt"
    test_data = load_data(test_data_filename)
    ans_part_1 = solve_part_1(test_data)
    print(ans_part_1)
    ans_part_2 = solve_part_2(test_data)
    print(ans_part_2)
