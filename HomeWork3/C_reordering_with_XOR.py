"""
Переупорядочивание с XOR

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Задано несколько целых чисел a_1, a_2, ⋯, a_n. Запишем их в двоичной системе
счисления, дополним меньшие из них ведущими нулями так, чтобы количество цифр в
них стало таким же, как в максимальном числе. Требуется переупорядочить биты в
них, получив новые числа b_1, b_2, ⋯, b_n, так что b_1 ⨁ b_2 ⨁ ⋯ ⨁ b_n = 0.
Операция ⨁ обозначает побитовое исключающее или (xor).


Формат ввода:
В первой строке записано число n (2 ≤ n ≤ 50).
Во второй строке записаны числа a_1, a_2, ⋯, a_n (1 ≤ a_i ≤ 10^18).


Формат вывода:
Выведите набор чисел b_1, b_2, ⋯, b_n.
Если подходящих наборов несколько — выведите любой из них.

Если составить такой набор невозможно, выведите слово ”impossible”.


Пример 1
input: 3
input: 7 10 11
output: 14 9 7

Пример 2
input: 3
input: 7 10 3
output: impossible


Примечания:
В первом примере a_1 = 7 = 0111_2, a_2 = 10 = 1010_2, a_3 = 11 = 1011_2.
Переупорядочим биты следующим образом: b_1 = 7 = 0111_2, b_2 = 12 = 1100_2,
b_3 = 11 = 1011_2. После этого b_1 ⨁ b_2 ⨁ b_3 = 0.
"""
import bisect
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    nums: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        nums = list(map(int, input().split()))
        return cls(ProblemInput(n, nums))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        return cls(ProblemInput(n, nums))

    def solve(self) -> tuple[bool, list[int]]:

        n = self.data.n
        nums = self.data.nums

        L = max(num.bit_length() for num in nums)
        counts = [num.bit_count() for num in nums]
        total = sum(counts)

        if total & 1:
            return False, []

        max_pairs_per_column = n // 2
        pairs = total // 2

        if pairs > L * max_pairs_per_column:
            return False, []

        base, rem = divmod(pairs, L)
        columns = [2 * (base + 1)] * rem + [2 * base] * (L - rem)

        counter = []
        for i, count in enumerate(counts):
            if count > 0:
                bisect.insort(counter, (count, i))

        answer = [0] * n

        for bit_pos, column_size in enumerate(columns):
            if column_size == 0:
                continue

            if len(counter) < column_size:
                return False, []

            taken = []

            for _ in range(column_size):
                count, idx = counter.pop()

                if count <= 0:
                    return False, []

                answer[idx] |= 1 << bit_pos
                taken.append((count - 1, idx))

            for count, idx in taken:
                if count > 0:
                    bisect.insort(counter, (count, idx))

        if counter:
            return False, []

        return True, answer


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    if not result[0]:
        print("impossible")
    else:
        print(*result[1])


if __name__ == "__main__":
    main()
