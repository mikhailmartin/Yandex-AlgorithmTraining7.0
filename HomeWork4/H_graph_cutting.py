"""
Разрезание графа

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Дан неориентированный граф. Над ним в заданном порядке производят операции
следующих двух типов:
- cut — разрезать граф, то есть удалить из него ребро;
- ask — проверить, лежат ли две вершины графа в одной компоненте связности.
Известно, что после выполнения всех операций типа cut рёбер в графе не осталось.
Найдите результат выполнения каждой из операций типа ask.


Формат ввода:
Первая строка входного файла содержит три целых числа, разделённые пробелами —
количество вершин графа n, количество рёбер m и количество операций k
(1 ≤ n ≤ 50_000, 0 ≤ m ≤ 100_000, m ≤ k ≤ 150_000).

Следующие m строк задают рёбра графа; i-ая из этих строк содержит два числа u_i
и v_i (1 ≤ u_i, v_i ≤ n), разделённые пробелами — номера концов i-го ребра.
Вершины нумеруются с единицы; граф не содержит петель и кратных рёбер.

Далее следуют k строк, описывающих операции. Операция типа cut задаётся строкой
"cut u v" (1 ≤ u, v ≤ n), которая означает, что из графа удаляют ребро между
вершинами u и v. Операция типа ask задаётся строкой "ask u v" (1 ≤ u, v ≤ n),
которая означает, что необходимо узнать, лежат ли в данный момент вершины u и v
в одной компоненте связности. Гарантируется, что каждое ребро графа встретится в
операциях типа cut ровно один раз.


Формат вывода:
Для каждой операции ask во входном файле выведите на отдельной строке слово
"YES", если две указанные вершины лежат в одной компоненте связности, и "NO" в
противном случае. Порядок ответов должен соответствовать порядку операций ask во
входном файле.


Пример
input: 3 3 7
input: 1 2
input: 2 3
input: 3 1
input: ask 3 3
input: cut 1 2
input: ask 1 2
input: cut 1 3
input: ask 2 1
input: cut 2 3
input: ask 3 1
output: YES
output: YES
output: NO
output: NO
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
            return True
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
    k: int
    edges: list[tuple[int, int]]
    operations: list[str]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n, m, k = map(int, sys.stdin.readline().strip().split())

        edges = []
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().strip().split())
            edges.append((u, v))

        operations = []
        for _ in range(k):
            operations.append(sys.stdin.readline().strip())

        return cls(ProblemInput(n, m, k, edges, operations))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, m, k = map(int, lines[0].split())

        edges = []
        for i in range(m):
            u, v = map(int, lines[i+1].split())
            edges.append((u, v))

        operations = []
        for j in range(k):
            operations.append(lines[1+m+j].strip())

        return cls(ProblemInput(n, m, k, edges, operations))

    def solve(self) -> list[str]:

        union_find = UnionFind(self.data.n)

        result = []
        for operation in reversed(self.data.operations):
            operation, u, v = operation.split()
            u = int(u)
            v = int(v)
            if operation == "cut":
                union_find.union(u-1, v-1)
            elif operation == "ask":
                if union_find.connected(u-1, v-1):
                    result.append("YES")
                else:
                    result.append("NO")

        return list(reversed(result))


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(result))


if __name__ == "__main__":
    main()
