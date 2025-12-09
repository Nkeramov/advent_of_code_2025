from collections import defaultdict


def load_data(filename: str, is_raw: bool = False) -> list[str]:
    return [line.strip("\n") if is_raw else line.strip() for line in open(filename, "r").readlines()]


def solve_part_1(data: list[str]) -> int:
    ans = 0
    _map = [list(line) for line in data]
    for i in range(len(_map) - 1):
        for j in range(len(_map[i])):
            if _map[i][j] == 'S':
                _map[i + 1][j] = '|'
            elif _map[i][j] == '|':
                if _map[i + 1][j] == '^':
                    if j > 0:
                        _map[i + 1][j - 1] = '|'
                        ans += 1
                    if j + 1 < len(_map[i]):
                        _map[i + 1][j + 1] = '|'
                        ans += 1
                elif _map[i + 1][j] == '.':
                    _map[i + 1][j] = '|'
    return ans // 2


def solve_part_2(data: list[str]) -> int:
    _map = [list(line) for line in data]
    d = defaultdict(int)
    for i in range(len(_map) - 1):
        for j in range(len(_map[i])):
            if _map[i][j] == 'S':
                _map[i + 1][j] = '|'
                d[(i + 1, j)] = 1
            elif _map[i][j] == '|':
                d[(i + 1, j)] += d[(i, j)]
                if _map[i + 1][j] == '^':
                    if j > 0:
                        _map[i + 1][j - 1] = '|'
                        d[(i + 1, j - 1)] += d[(i, j)]
                    if j + 1 < len(_map[i]):
                        _map[i + 1][j + 1] = '|'
                        d[(i + 1, j + 1)] += d[(i, j)]
                elif _map[i + 1][j] == '.':
                    _map[i + 1][j] = '|'
    ans = 0
    for k, v in d.items():
        if k[0] == len(_map) - 1:
            ans += v
    return ans


if __name__ == '__main__':
    test_data_filename = "test_input.txt"
    data = load_data(test_data_filename)
    ans_part_1 = solve_part_1(data)
    print(ans_part_1)
    ans_part_2 = solve_part_2(data)
    print(ans_part_2)
