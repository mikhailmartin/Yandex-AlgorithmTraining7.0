import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    weights = list(map(int, lines[1].split()))

    options = set()
    options.add(0)
    for weight in weights:
        buffer = set()
        for option in options:
            remaining = m - option
            if remaining >= weight:
                buffer.add(option + weight)
        options |= buffer

    return max(options)


if __name__ == "__main__":
    result = main()
    print(result)
