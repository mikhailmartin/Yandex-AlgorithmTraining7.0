import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    x1, y1 = map(int, lines[0].split())
    x2, c2 = map(int, lines[1].split())

    return x1 ^ y1, x2 ^ c2


if __name__ == "__main__":
    result = main()
    print(result[0])
    print(result[1])
