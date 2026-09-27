"""
Звёзды

Ограничение времени - 2 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Вася любит наблюдать за звёздами. Но следить за всем небом сразу ему тяжело.
Поэтому он наблюдает только за частью пространства, ограниченной кубом размером
n×n×n. Этот куб поделён на маленькие кубики размером 1×1×1. Во время его
наблюдений могут происходить следующие события:
1. В каком-то кубике появляются или исчезают несколько звёзд.
2. К нему может заглянуть его друг Петя и поинтересоваться, сколько видно звёзд
   в части пространства, состоящей из нескольких кубиков.


Формат ввода:
Первая строка входного файла содержит натуральное число 1 ≤ n ≤ 128. Координаты
кубиков — целые числа от 0 до n−1. Далее следуют записи о происходивших событиях
по одной в строке. В начале строки записано число m. Если m равно:
1, то за ним следуют 4 числа — x, y, z (0 ≤ x, y, z < N) и
   k (−20_000 ≤ k ≤ 20_000) — координаты кубика и величина, на которую в нём
   изменилось количество видимых звёзд;
2, то за ним следуют 6 чисел — x_1, y_1, z_1, x_2, y_2, z_2 (0 ≤ x_1 ≤ x_2 < N,
   0 ≤ y_1 ≤ y_2 < N, 0 ≤ z_1 ≤ z_2 < N), которые означают, что Петя попросил
   подсчитать количество звёзд в кубиках (x, y, z) из области: x_1 ≤ x ≤ x_2,
   y_1 ≤ y ≤ y_2, z_1 ≤ z ≤ z_2;
3, то это означает, что Васе надоело наблюдать за звёздами и отвечать на вопросы
   Пети. Эта запись встречается во входном файле только один раз и будет
   последней.
Количество записей во входном файле не больше 100_002.


Формат вывода:
Для каждого Петиного вопроса выведите искомое количество звёзд.


Пример
input: 2
input: 2 1 1 1 1 1 1
input: 1 0 0 0 1
input: 1 0 1 0 3
input: 2 0 0 0 0 0 0
input: 2 0 0 0 0 1 0
input: 1 0 1 0 -2
input: 2 0 0 0 1 1 1
input: 3
output: 0
output: 1
output: 4
output: 2
"""
import sys
from dataclasses import dataclass
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
        result = 0
        while x >= 0:
            y = yo
            while y >= 0:
                z = zo
                while z >= 0:
                    result += tree[x][y][z]
                    z = (z & (z + 1)) - 1
                y = (y & (y + 1)) - 1
            x = (x & (x + 1)) - 1
        return result


@dataclass
class ProblemInput:
    n: int
    queries: list[list[int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(sys.stdin.readline())
        queries = []
        while True:
            query = list(map(int, sys.stdin.readline().split()))
            m = query[0]
            if m != 3:
                queries.append(query)
            else:
                break
        return cls(ProblemInput(n, queries))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
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
        return cls(ProblemInput(n, queries))

    def solve(self) -> list[int]:

        n = self.data.n
        bit3d = BinaryIndexedTree3D(n, n, n)

        result = []
        for query in self.data.queries:
            m = query[0]
            if m == 1:
                _, x, y, z, k = query
                bit3d.add(x, y, z, k)
            elif m == 2:
                _, x1, y1, z1, x2, y2, z2 = query
                answer = bit3d.get(x1, y1, z1, x2, y2, z2)
                result.append(answer)

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
