def load_data(filename: str) -> list[str]:
    return [line.strip() for line in open(filename, "r").readlines()]


def solve_part_1(data: list[str]) -> int:
    total_joltage = 0
    for line in data:
        mx1 = mx2 = 0
        imx1 = 0
        nums = list(map(int, line))
        for i, m in enumerate(nums):
            if m > mx1:
                mx2 = mx1
                mx1 = m
                imx1 = i
            elif m > mx2:
                mx2 = m
        if imx1 < len(line) - 1:
            joltage = mx1 * 10 + max(nums[imx1 + 1:])
        else:
            joltage = mx2 * 10 + mx1
        total_joltage += joltage
    return total_joltage


def solve_part_2(data: list[str]) -> int:
    total_joltage = 0
    for line in data:
        joltage = 0
        nums = list(map(int, line))
        for i in range(11, -1, -1):
            jmx = mx = 0
            for j in range(len(nums) - i):
                if nums[j] > mx:
                    mx = nums[j]
                    jmx = j
            nums = nums[jmx + 1:]
            joltage = joltage * 10 + mx
        total_joltage += joltage
    return total_joltage


if __name__ == '__main__':
    test_data_filename = "test_input.txt"
    test_data = load_data(test_data_filename)
    ans_part_1 = solve_part_1(test_data)
    print(ans_part_1)
    ans_part_2 = solve_part_2(test_data)
    print(ans_part_2)
