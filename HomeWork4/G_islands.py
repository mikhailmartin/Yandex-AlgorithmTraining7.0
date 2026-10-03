"""
Острова

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Одно разбросанное на островах Океании государство решило создать сеть
автомобильных дорог (вернее, мостов). По каждому мосту можно перемещаться в обе
стороны. Был разработан план очерёдности строительства мостов, и известно, что
после постройки всех мостов можно будет проехать по ним с каждого острова на
каждый (возможно, через некоторые промежуточные острова).

Однако этот момент может наступить до того, как будут построены все мосты. Вам
необходимо определить такое минимальное количество мостов, после строительства
которых (в порядке, определённом планом) можно будет попасть с любого острова на
любой другой.


Формат ввода:
Первая строка содержит два числа: число островов N (1 ≤ N ≤ 10_000) и количество
мостов в плане M (1 ≤ M ≤ 50_000). Далее идёт M строк, каждая содержит два числа
x и y (1 ≤ x, y ≤ N) — номера островов, которые соединяет очередной мост в плане.


Формат вывода:
Программа должна вывести единственное число — минимальное количество построенных
мостов, после которого можно будет попасть с любого острова на любой другой.


Пример
input: 4 5
input: 1 2
input: 1 3
input: 2 3
input: 3 4
input: 4 1
output: 4
"""
import sys
from dataclasses import dataclass
from typing import Self


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


@dataclass
class ProblemInput:
    n: int
    m: int
    bridges: list[tuple[int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n, m = map(int, sys.stdin.readline().strip().split())
        bridges = []
        for _ in range(m):
            x, y = map(int, sys.stdin.readline().strip().split())
            bridges.append((x, y))
        return cls(ProblemInput(n, m, bridges))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, m = map(int, lines[0].split())
        bridges = []
        for i in range(m):
            x, y = map(int, lines[i+1].split())
            bridges.append((x, y))
        return cls(ProblemInput(n, m, bridges))

    def solve(self) -> int:

        union_find = UnionFind(self.data.n)

        for count, (x, y) in enumerate(self.data.bridges, 1):
            union_find.union(x-1, y-1)
            if union_find.components == 1:
                return count


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
