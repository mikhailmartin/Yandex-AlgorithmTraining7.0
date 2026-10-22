import sys


def main(lines: list[str] | None = None) -> tuple[int, list[int]]:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    groups = [(i, num+1) for i, num in enumerate(map(int, lines[1].split()), 1)]
    classrooms = list(enumerate(map(int, lines[2].split()), 1))

    groups.sort(key=lambda x: x[1])
    classrooms.sort(key=lambda x: x[1])

    count = 0
    distribution = [0] * n
    g_ptr = 0
    c_ptr = 0
    while g_ptr < n and c_ptr < m:
        i, group = groups[g_ptr]
        j, classroom = classrooms[c_ptr]
        if group <= classroom:
            count += 1
            distribution[i-1] = j
            g_ptr += 1
            c_ptr += 1
        else:
            c_ptr += 1

    return count, distribution


if __name__ == "__main__":
    result = main()
    print(result[0])
    print(*result[1])
