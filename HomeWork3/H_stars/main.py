import sys
from itertools import product
from typing import Self


class BinaryIndexedTree2D:
    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.tree: list[int] = [0] * (n * m)

    @classmethod
    def from_matrix(cls, matrix: list[list[int]]) -> Self:
        n = len(matrix)
        m = len(matrix[0])
        bit2d = cls(n, m)
        for x, y in product(range(n), range(m)):
            xe = x
            xs = x & (x + 1)

            ye = y
            ys = y & (y + 1)

            bit2d.tree[x * n + y] = sum(
                sum(matrix[x_][ys:ye + 1]) for x_ in range(xs, xe + 1)
            )
        return bit2d

    def add(self, x: int, y: int, value: int) -> None:

        n = self.n
        m = self.m
        tree = self.tree

        origin_y = y
        while x < n:
            y = origin_y
            while y < m:
                tree[x * n + y] += value
                y = y | (y + 1)
            x = x | (x + 1)

    def get(self, xs: int, ys: int, xe: int, ye: int) -> int:

        n = self.n
        tree = self.tree

        def _get(x: int, y: int) -> int:
            origin_y = y
            result = 0
            while x >= 0:
                y = origin_y
                while y >= 0:
                    result += tree[x * n + y]
                    y = (y & (y + 1)) - 1
                x = (x & (x + 1)) - 1
            return result

        return _get(xe, ye) - _get(xs - 1, ye) - _get(xe, ys - 1) + _get(xs - 1, ys - 1)


class BinaryIndexedTree3D:
    def __init__(self, n: int, m: int, k: int) -> None:
        self.n = n
        self.m = m
        self.k = k
        self.tree: list[list[list[int]]] = [
            [[0] * k for _ in range(m)] for _ in range(n)
        ]

    @classmethod
    def from_tensor(cls, tensor: list[list[list[int]]]) -> Self:
        n = len(tensor)
        m = len(tensor[0])
        k = len(tensor[0][0])
        bit3d = cls(n, m, k)
        for x, y, z in product(range(n), range(m), range(k)):
            xe = x
            xs = x & (x + 1)

            ye = y
            ys = y & (y + 1)

            ze = z
            zs = z & (z + 1)

            bit3d.tree[x][y][z] = sum(
                sum(
                    sum(tensor[x_][y_][zs:ze + 1])
                    for y_ in range(ys, ye + 1)
                )
                for x_ in range(xs, xe + 1)
            )
        return bit3d

    def add(self, x: int, y: int, z: int, value: int) -> None:

        tree = self.tree

        yo = y
        zo = z
        while x < self.n:
            y = yo
            while y < self.m:
                z = zo
                while z < self.k:
                    tree[x][y][z] += value
                    z = z | (z + 1)
                y = y | (y + 1)
            x = x | (x + 1)

    def get(self, xs: int, ys: int, zs: int, xe: int, ye: int, ze: int) -> int:
        return (
            self._get(xe, ye, ze)
            - self._get(xs - 1, ye, ze)
            - self._get(xe, ys - 1, ze)
            - self._get(xe, ye, zs - 1)
            + self._get(xs - 1, ys - 1, ze)
            + self._get(xs - 1, ye, zs - 1)
            + self._get(xe, ys - 1, zs - 1)
            - self._get(xs - 1, ys - 1, zs - 1)
        )

    def _get(self, x: int, y: int, z: int) -> int:

        tree = self.tree

        yo = y
        zo = z
        res = 0
        while x >= 0:
            y = yo
            while y >= 0:
                z = zo
                while z >= 0:
                    res += tree[x][y][z]
                    z = (z & (z + 1)) - 1
                y = (y & (y + 1)) - 1
            x = (x & (x + 1)) - 1
        return res


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    queries = []
    i = 1
    while True:
        query = list(map(int, lines[i].split()))
        m = query[0]
        if m != 3:
            queries.append(query)
        else:
            break
        i += 1

    bit3d = BinaryIndexedTree3D(n, n, n)

    res = []
    for query in queries:
        m = query[0]
        if m == 1:
            _, x, y, z, k = query
            bit3d.add(x, y, z, k)
        elif m == 2:
            _, x1, y1, z1, x2, y2, z2 = query
            answer = bit3d.get(x1, y1, z1, x2, y2, z2)
            res.append(answer)

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
