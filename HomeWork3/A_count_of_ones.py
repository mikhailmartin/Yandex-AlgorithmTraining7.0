"""
Количество единиц

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Подсчитайте количество единиц в двоичной записи числа.


Формат ввода:
Дано целое число x (0 ≤ x ≤ 4 × 10^18), записанное в десятичной системе счисления.


Формат вывода:
Вывести количество единиц в двоичной записи числа x.


Пример
input: 9
output: 2
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    x: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        x = int(input())
        return cls(ProblemInput(x))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        x = int(lines[0])
        return cls(ProblemInput(x))

    def solve(self) -> int:

        x = self.data.x

        result = 0
        k = 1
        while k <= x:
            if x & k:
                result += 1
            k <<= 1

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
