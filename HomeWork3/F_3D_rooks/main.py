import sys
from itertools import product


def main(lines: list[str] | None = None) -> tuple[bool, tuple[int, int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    coords = []
    for i in range(k):
        x, y, z = map(int, lines[i+1].split())
        coords.append((x, y, z))

    xy = [[False] * n for _ in range(n)]
    xz = [0] * n
    yz = [0] * n

    for x, y, z in coords:
        xy[x - 1][y - 1] = True
        z_bit = 1 << (z - 1)
        xz[x - 1] |= z_bit
        yz[y - 1] |= z_bit

    ref = (1 << n) - 1
    for x, y in product(range(n), range(n)):
        if not xy[x][y]:
            union = xz[x] | yz[y]
            if union != ref:
                for i in range(n):
                    bit = 1 << i
                    if union & bit == 0:
                        return False, (x + 1, y + 1, i + 1)

    return True, (1, 1, 1)


if __name__ == "__main__":
    result = main()
    if not result[0]:
        print("NO")
        print(*result[1])
    else:
        print("YES")
