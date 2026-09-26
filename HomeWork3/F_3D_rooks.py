"""
Трёхмерные ладьи

Ограничение времени - 3 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Игра в трёхмерные шахматы ведётся на кубическом поле N × N × N. Трёхмерная ладья
может ходить на любое число клеток по прямой в любом из шести направлений
(в любую сторону в каждом из трёх направлений).

На таком поле расставлены K ладей. Напишите программу, которая определит, бьют
они всё поле или нет.


Формат ввода:
В первой строке входного файла записано натуральное число N (1 ≤ N ≤ 1000),
задающее размеры игрового куба, и количество ладей K (0 ≤ K ≤ 10^6). Далее
записано K троек чисел, задающих координаты ладей (координата по каждому
измерению — натуральное число от 1 до N).


Формат вывода:
Выведите в выходной файл слово YES, если эти ладьи бьют весь куб, и слово NO в
противном случае. В случае NO выведите во второй строке координаты какой-нибудь
клетки, которая не бьётся ни одной из ладей.


Пример 1
input: 2 2
input: 1 1 1
input: 2 2 2
output: YES

Пример 2
input: 2 2
input: 1 1 1
input: 1 1 2
output: NO
output: 2 2 1
"""
from dataclasses import dataclass
from itertools import product
from typing import Self


@dataclass
class ProblemInput:
    n: int
    k: int
    coords: list[tuple[int, int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n, k = map(int, input().split())
        coords = []
        for _ in range(k):
            x, y, z = map(int, input().split())
            coords.append((x, y, z))
        return cls(ProblemInput(n, k, coords))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, k = map(int, lines[0].split())
        coords = []
        for i in range(k):
            x, y, z = map(int, lines[i+1].split())
            coords.append((x, y, z))
        return cls(ProblemInput(n, k, coords))

    def solve(self) -> tuple[bool, tuple[int, int, int]]:

        n = self.data.n
        coords = self.data.coords

        xy = [[False] * n for _ in range(n)]
        xz = [0] * n
        yz = [0] * n

        for x, y, z in coords:
            xy[x-1][y-1] = True
            z_bit = 1 << (z - 1)
            xz[x-1] |= z_bit
            yz[y-1] |= z_bit

        ref = (1 << n) - 1
        for x, y in product(range(n), range(n)):
            if not xy[x][y]:
                union = xz[x] | yz[y]
                if union != ref:
                    for i in range(n):
                        bit = 1 << i
                        if union & bit == 0:
                            return False, (x+1, y+1, i+1)

        return True, (1, 1, 1)


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    if not result[0]:
        print("NO")
        print(*result[1])
    else:
        print("YES")


if __name__ == "__main__":
    main()
