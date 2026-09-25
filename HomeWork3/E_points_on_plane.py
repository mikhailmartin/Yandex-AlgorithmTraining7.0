"""
Точки на плоскости

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Точки с целочисленными координатами из 1-го квадранта помечаются числами 0, 1, 2, …
слева направо и снизу вверх таким образом, что очередной точке приписывается
минимальное число, отсутствующее в вертикали и горизонтали, проходящей через
точку. Первой помечается точка (0, 0).

Допустим, мы хотим пометить точку (i, j). Это значит, что все точки, находящиеся
ниже и левее относительно неё, уже помечены. Тогда рассмотрим набор из чисел в
i-й строке и j-м столбце (вместе). Отметкой точки (i, j) будет минимальное
неотрицательное число, которое не содержится в этом наборе.

Написать программу, которая:
1. По заданным координатам x и y, x ≥ 0, y ≥ 0, x, y — целые, определяет пометку
   точки.
2. По заданной координате x и пометке точки c, x ≥ 0, y ≥ 0, x, y — целые,
   определяет вторую координату точки.


Формат ввода:
В первой строке даются два числа x и y для первой части задачи (0 ≤ x, y ≤ 10^9).
Во второй строке даются два числа x и c для второй части задачи (0 ≤ x ≤ 10^9, 0 ≤ c ≤ 2⋅10^9).


Пример
input: 3 4
input: 5 23
output: 7
output: 18
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    x1: int
    y1: int
    x2: int
    c2: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        x1, y1 = map(int, input().split())
        x2, c2 = map(int, input().split())
        return cls(ProblemInput(x1, y1, x2, c2))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        x1, y1 = map(int, lines[0].split())
        x2, c2 = map(int, lines[1].split())
        return cls(ProblemInput(x1, y1, x2, c2))

    def solve(self) -> tuple[int, int]:
        return self.data.x1 ^ self.data.y1, self.data.x2 ^ self.data.c2


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result[0])
    print(result[1])


if __name__ == "__main__":
    main()
