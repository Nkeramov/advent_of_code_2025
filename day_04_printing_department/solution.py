def load_data(filename: str, is_raw: bool = False) -> list[str]:
    return [line.strip("\n") if is_raw else line.strip() for line in open(filename, "r").readlines()]


def build_map(data: list[str]) -> list[list[str]]:
    width = len(data[0]) + 2
    _map = [list("." * width)] + [list("." + row + ".") for row in data] + [list("." * width)]
    return _map


def find_accessible(_map: list[list[str]]) -> list[list[int]]:
    width = len(_map[0])
    height = len(_map)
    adjacent_positions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    accessible_positions = []
    for i in range(1, height):
        for j in range(1, width):
            if _map[i][j] == "@":
                if sum(1 for _pos in adjacent_positions if _map[i + _pos[0]][j + _pos[1]] == "@") < 4:
                    accessible_positions.append([i, j])
    return accessible_positions


def solve_part_1(data: list[str]) -> int:
    _map = build_map(data)
    accessible_positions = find_accessible(_map)
    return len(accessible_positions)


def solve_part_2(data: list[str]) -> int:
    _map = build_map(data)
    ans = 0
    accessible_positions = find_accessible(_map)
    while accessible_positions:
        ans += len(accessible_positions)
        for x, y in accessible_positions:
            _map[x][y] = "."
        accessible_positions = find_accessible(_map)
    return ans


if __name__ == '__main__':
    test_data_filename = "test_input.txt"
    test_data = load_data(test_data_filename)
    test_map = build_map(test_data)
    ans_part_1 = solve_part_1(test_data)
    print(ans_part_1)
    ans_part_2 = solve_part_2(test_data)
    print(ans_part_2)
