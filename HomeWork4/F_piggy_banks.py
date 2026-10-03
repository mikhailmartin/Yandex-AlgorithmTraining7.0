"""
Свинки-копилки

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

У Васи есть N свинок-копилок, свинки занумерованы числами от 1 до N. Каждая
копилка может быть открыта единственным соответствующим ей ключом или разбита.

Вася положил ключи в некоторые из копилок (он помнит, какой ключ лежит в какой
из копилок). Теперь Вася собрался купить машину, а для этого ему нужно достать
деньги из всех копилок. При этом он хочет разбить как можно меньшее количество
копилок (ведь ему ещё нужно копить деньги на квартиру, дачу, вертолёт…).
Помогите Васе определить, какое минимальное количество копилок нужно разбить.


Формат ввода:
В первой строке содержится число N — количество свинок-копилок (1 ≤ N ≤ 100000).
Далее идёт N строк с описанием того, где лежит ключ от какой копилки: в i-ой из
этих строк записан номер копилки, в которой находится ключ от i-ой копилки.


Формат вывода:
Выведите единственное число: минимальное количество копилок, которые необходимо
разбить.


Пример
input: 4
input: 2
input: 1
input: 2
input: 4
output: 2


Примечания:
Ключи от первой и третьей копилки лежат в копилке 2, ключ от второй — в первой,
а от четвертой — в ней самой.

Чтобы открыть все копилки, достаточно разбить, например, копилки с номерами 1 и 4.
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
    keys: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(sys.stdin.readline().strip())
        keys = []
        for _ in range(n):
            key = int(sys.stdin.readline().strip())
            keys.append(key)
        return cls(ProblemInput(n, keys))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        keys = []
        for i in range(n):
            key = int(lines[i+1])
            keys.append(key)
        return cls(ProblemInput(n, keys))

    def solve(self) -> int:

        union_find = UnionFind(self.data.n)
        for i, key in enumerate(self.data.keys):
            union_find.union(i, key-1)

        return union_find.components


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
