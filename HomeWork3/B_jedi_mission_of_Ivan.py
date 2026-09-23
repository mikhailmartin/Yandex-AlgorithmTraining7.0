"""
Миссия джедая Ивана

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Юный джедай Иван был заброшен на Звезду Смерти с заданием уничтожить её. Для
того, чтобы уничтожить Звезду Смерти, ему требуется массив неотрицательных целых
чисел a_i длины N. К сожалению, у Ивана нет этого массива, но есть секретный
документ с требованиями к этому массиву, который ему передал его старый друг
Дарт Вейдер.

В этом документе содержится квадратная матрица m размера N, где элемент в
i-й строке в j-м столбце равен побитовому "И" чисел a_i и a_j. Для повышения
безопасности главная диагональ матрицы была уничтожена и вместо чисел на ней
были записаны нули. Помогите Ивану восстановить массив a и выполнить свою
миссию.

Гарантируется, что решение всегда существует. Если решений несколько, выведите
любое.


Формат ввода:
В первой строке содержится число N (1 ≤ N ≤ 1000) — размер матрицы.

Каждая из последующих N строк содержит по N целых чисел m_{ij} (0 ≤ m_{ij} ≤ 9)
— элементы матрицы.


Формат вывода:
В единственной строке выведите N целых неотрицательных чисел, не превышающих
100 — требуемый массив a.


Пример 1
input: 3
input: 0 1 1
input: 1 0 1
input: 1 1 0
output: 1 1 1

Пример 2
input: 5
input: 0 0 1 1 1
input: 0 0 2 0 2
input: 1 2 0 1 3
input: 1 0 1 0 1
input: 1 2 3 1 0
output: 1 2 3 1 3
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    matrix: list[list[int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        matrix = []
        for _ in range(n):
            line = list(map(int, input().split()))
            matrix.append(line)
        return cls(ProblemInput(n, matrix))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        matrix = []
        for i in range(n):
            line = list(map(int, lines[i+1].split()))
            matrix.append(line)
        return cls(ProblemInput(n, matrix))

    def solve(self) -> list[int]:

        n = self.data.n
        matrix = self.data.matrix

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


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(*result)


if __name__ == "__main__":
    main()
