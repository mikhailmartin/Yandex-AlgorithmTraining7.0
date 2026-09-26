"""
Сумма на отрезке

Ограничение времени - 2 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Дан массив из N элементов, нужно научиться находить сумму чисел на отрезке.


Формат ввода:
Первая строка входного файла содержит два целых числа N и K — количество чисел в
массиве и количество запросов (1 ⩽ N ⩽ 100_000, 0 ⩽ K ⩽ 100_000). Следующие K
строк содержат следующие запросы:
1. A i x — присвоить i-му элементу массива значение x (1 ⩽ i ⩽ n, 0 ⩽ x ⩽ 10^9);
2. Q l r — найти сумму чисел в массиве на позициях от l до r (1 ⩽ l ⩽ r ⩽ n).
Изначально в массиве живут нули.


Формат вывода:
На каждый запрос вида Q l r нужно вывести единственное число — сумму на отрезке.


Пример
input: 5 9
input: A 2 2
input: A 3 1
input: A 4 2
input: Q 1 1
input: Q 2 2
input: Q 3 3
input: Q 4 4
input: Q 5 5
input: Q 1 5
output: 0
output: 2
output: 1
output: 2
output: 0
output: 5
"""
from dataclasses import dataclass
from typing import Self


class FenwickTree:
    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        self.tree: list[int] = [0] * n
        for i in range(n):
            end = i
            start = i & (i + 1)
            self.tree[i] = sum(arr[start:end + 1])

    def update(self, idx: int, value: int) -> None:
        diff = value - self.get(idx, idx)
        while idx < len(self.tree):
            self.tree[idx] += diff
            idx = idx | (idx + 1)

    def get(self, start: int, end: int) -> int:
        return self._get(end) - self._get(start-1)

    def _get(self, idx: int) -> int:
        result = 0
        while idx >= 0:
            result += self.tree[idx]
            idx = (idx & (idx + 1)) - 1
        return result


@dataclass
class ProblemInput:
    n: int
    k: int
    queries: list[tuple[str, int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n, k = map(int, input().split())
        queries = []
        for _ in range(k):
            query_type, i, x = input().split()
            i = int(i)
            x = int(x)
            queries.append((query_type, i, x))
        return cls(ProblemInput(n, k, queries))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, k = map(int, lines[0].split())
        queries = []
        for i in range(k):
            query_type, i, x = lines[i+1].split()
            i = int(i)
            x = int(x)
            queries.append((query_type, i, x))
        return cls(ProblemInput(n, k, queries))

    def solve(self) -> list[int]:

        fenwick_tree = FenwickTree([0] * self.data.n)

        result = []
        for query in self.data.queries:
            if query[0] == "A":
                i, x = query[1], query[2]
                fenwick_tree.update(i-1, x)
            elif query[0] == "Q":
                l, r = query[1], query[2]
                answer = fenwick_tree.get(l-1, r-1)
                result.append(answer)

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
