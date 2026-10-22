import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    x = int(lines[0])

    res = 0
    k = 1
    while k <= x:
        if x & k:
            res += 1
        k <<= 1

    return res


if __name__ == "__main__":
    result = main()
    print(result)
