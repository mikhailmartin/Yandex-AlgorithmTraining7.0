import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    matrix = []
    for i in range(n):
        line = list(map(int, lines[i+1].split()))
        matrix.append(line)

    a = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            m = matrix[i][j]
            # выставляем 1
            a[i] |= m
            a[j] |= m
            # выставляем 0
            a[i] = (m & a[j]) | a[i]
            a[j] = (m & a[i]) | a[j]

    return a


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
