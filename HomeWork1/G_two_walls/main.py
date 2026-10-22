import sys


def main(lines: list[str] | None = None) -> None:

    lines = lines or sys.stdin.read().splitlines()

    n, height = map(int, lines[0].split())
    wall = [[] for _ in range(height)]
    bricks = [0]
    for i in range(1, n+1):
        length, color = map(int, lines[1+i].split())
        bricks.append(length)
        wall[color - 1].append((i, length))

    options = build_options(wall)

    common_splits = has_solution(options)
    has_solution_flag = bool(common_splits)
    print("YES" if has_solution_flag else "NO")
    if solution := build_solution(common_splits, options, bricks):
        print(*solution)


def build_options(wall) -> list:

    wall_length = sum([brick[1] for brick in wall[-1]])

    options = []
    for layer in wall:
        option = [0] + [-1] * wall_length
        for brick in layer:
            i, length = brick
            for j in reversed(range(wall_length - length + 1)):
                if option[j] != -1 and option[j + length] == -1:
                    option[j + length] = i
        options.append(option)

    return options


def has_solution(options):

    splits = []
    for option in options:
        current_splits = {
            split for split, i in enumerate(option[1:-1], 1) if i != -1
        }
        splits.append(current_splits)

    common_splits = set.intersection(*splits)

    return common_splits


def build_solution(common_splits, options, bricks) -> list[int] | None:

    if not common_splits:
        return None

    common_split = next(iter(common_splits))  # достаём любой split

    solution: list[int] = []
    for option in options:
        current_length = common_split
        while current_length != 0:
            i = option[current_length]
            solution.append(i)
            current_length -= bricks[i]

    return solution


if __name__ == "__main__":
    main()
