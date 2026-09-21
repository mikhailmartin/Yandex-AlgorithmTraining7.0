"""
Присваивание на отрезке, сравнение подотрезков*

Ограничение времени - 12.001 секунда
Ограничение памяти - 1024Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Реализуйте структуру данных, которая позволяет выполнять две операции:
- Присвоить всем элементам на отрезке от L до R значение K;
- Поэлементно сравнить все числа на отрезках длины K, начинающихся с позиций L и R.


Формат ввода:
В первой строке записано число N (1 ≤ N ≤ 100_000) — количество элементов
в последовательности.

Во второй строке записано N целых чисел — начальные значения последовательности,
все числа имеют значения от 1 до 100_000.

В третьей строке записано число Q (1 ≤ Q ≤ 100_000) — количество операций
сравнения и присваивания.

Следующие Q строк содержат описания операций: четыре числа T, L, R и K.

Если T = 0, то необходимо всем числам с индексами с L до R включительно присвоить
значение K (1 ≤ L ≤ R ≤ N, 1 ≤ K ≤ 100_000).

Если T = 1, то необходимо сравнить подотрезки, начинающиеся с позиций L и R и
имеющие длину K (1 ≤ L, R ≤ N − K + 1, K > 0).


Формат вывода:
Для каждого запроса сравнения подстрок выведите ’+’, если подотрезки совпадают
и ’-’ в противном случае в одну строку без пробелов.


Пример
input: 5
input: 1 2 1 2 1
input: 4
input: 1 2 4 2
input: 0 3 5 2
input: 1 1 3 2
input: 1 2 3 3
output: +-+
"""
from dataclasses import dataclass
from typing import Self


MASK = (1 << 64) - 1

# Нечётные основания для двух независимых полиномиальных хешей.
BASE1 = 911382323
BASE2 = 972663749


@dataclass
class ProblemInput:
    n: int
    arr: list[int]
    q: int
    operations: list[tuple[int, int, int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

        n = data.n
        arr = data.arr

        self.n = n

        # pow[i] = BASE^i mod 2^64
        # geo[i] = 1 + BASE + ... + BASE^(i-1) mod 2^64
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        geo1 = [0] * (n + 1)
        geo2 = [0] * (n + 1)

        mask = MASK

        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * BASE1) & mask
            pow2[i] = (pow2[i - 1] * BASE2) & mask
            geo1[i] = (geo1[i - 1] + pow1[i - 1]) & mask
            geo2[i] = (geo2[i - 1] + pow2[i - 1]) & mask

        self.pow1 = pow1
        self.pow2 = pow2
        self.geo1 = geo1
        self.geo2 = geo2

        size = 1
        while size < n:
            size <<= 1

        self.size = size
        self.log = size.bit_length() - 1

        # Вспомогательные порядки обхода для итеративного lazy segment tree.
        self.down = tuple(range(self.log, 0, -1))
        self.up = tuple(range(1, self.log + 1))

        # length[v] -- количество реальных элементов в узле.
        # Листья, выходящие за пределы n, имеют длину 0.
        self.length = [0] * (size << 1)

        for i in range(n):
            self.length[size + i] = 1

        for i in range(size - 1, 0, -1):
            self.length[i] = self.length[i << 1] + self.length[i << 1 | 1]

        # Хеши узлов.
        self.h1 = [0] * (size << 1)
        self.h2 = [0] * (size << 1)

        for i, value in enumerate(arr):
            self.h1[size + i] = value & mask
            self.h2[size + i] = value & mask

        for i in range(size - 1, 0, -1):
            left = i << 1
            right = left | 1
            left_len = self.length[left]

            self.h1[i] = (self.h1[left] + self.h1[right] * self.pow1[left_len]) & mask
            self.h2[i] = (self.h2[left] + self.h2[right] * self.pow2[left_len]) & mask

        # lazy[v] = -1, если отложенного присваивания нет.
        self.lazy = [-1] * (size << 1)

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        arr = list(map(int, input().split()))
        q = int(input())
        operations = []
        for _ in range(q):
            t, l, r, k = map(int, input().split())
            operations.append((t, l, r, k))
        return cls(ProblemInput(n, arr, q, operations))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        q = int(lines[2])
        operations = []
        for i in range(q):
            t, l, r, k = map(int, lines[i+3].split())
            operations.append((t, l, r, k))
        return cls(ProblemInput(n, arr, q, operations))

    def solve(self) -> list:

        result = []

        append = result.append
        range_assign = self._range_assign
        range_hash = self._range_hash

        for t, l, r, k in self.data.operations:
            if t == 0:
                # Присваивание на отрезке [l, r] включительно.
                range_assign(l - 1, r, k)
            else:
                # Сравнение подотрезков длины k, начинающихся с l и r.
                if l == r:
                    append("+")
                else:
                    left_start = l - 1
                    right_start = r - 1

                    left_hash = range_hash(left_start, left_start + k)
                    right_hash = range_hash(right_start, right_start + k)

                    append("+" if left_hash == right_hash else "-")

        return result

    def _apply(self, v: int, value: int) -> None:
        """Присвоить всему узлу v значение value."""
        ln = self.length[v]
        if ln == 0:
            return

        mask = MASK

        self.h1[v] = (value * self.geo1[ln]) & mask
        self.h2[v] = (value * self.geo2[ln]) & mask

        if v < self.size:
            self.lazy[v] = value

    def _push(self, v: int) -> None:
        """Протолкнуть отложенное присваивание из узла v в детей."""
        value = self.lazy[v]

        if value == -1 or v >= self.size:
            return

        size = self.size
        length = self.length
        h1 = self.h1
        h2 = self.h2
        lazy = self.lazy
        geo1 = self.geo1
        geo2 = self.geo2
        mask = MASK

        left = v << 1
        right = left | 1

        left_len = length[left]
        if left_len:
            h1[left] = (value * geo1[left_len]) & mask
            h2[left] = (value * geo2[left_len]) & mask
            if left < size:
                lazy[left] = value

        right_len = length[right]
        if right_len:
            h1[right] = (value * geo1[right_len]) & mask
            h2[right] = (value * geo2[right_len]) & mask
            if right < size:
                lazy[right] = value

        lazy[v] = -1

    def _pull(self, v: int) -> None:
        """Пересчитать хеш узла v по его детям."""
        left = v << 1
        right = left | 1
        left_len = self.length[left]
        mask = MASK

        self.h1[v] = (self.h1[left] + self.h1[right] * self.pow1[left_len]) & mask
        self.h2[v] = (self.h2[left] + self.h2[right] * self.pow2[left_len]) & mask

    def _range_assign(self, l: int, r: int, value: int) -> None:
        """
        Присвоить значение value всем элементам на полуинтервале [l, r).
        Индексация 0-based.
        """
        size = self.size

        l += size
        r += size

        l0 = l
        r0 = r

        lazy = self.lazy
        push = self._push

        # Спускаем отложенные операции на путях к границам отрезка.
        for i in self.down:
            if ((l0 >> i) << i) != l0:
                v = l0 >> i
                if lazy[v] != -1:
                    push(v)

            if ((r0 >> i) << i) != r0:
                v = (r0 - 1) >> i
                if lazy[v] != -1:
                    push(v)

        apply = self._apply

        # Итеративное обновление стандартным набором узлов.
        while l < r:
            if l & 1:
                apply(l, value)
                l += 1

            if r & 1:
                r -= 1
                apply(r, value)

            l >>= 1
            r >>= 1

        pull = self._pull

        # Поднимаем изменения обратно.
        for i in self.up:
            if ((l0 >> i) << i) != l0:
                v = l0 >> i
                if lazy[v] == -1:
                    pull(v)

            if ((r0 >> i) << i) != r0:
                v = (r0 - 1) >> i
                if lazy[v] == -1:
                    pull(v)

    def _range_hash(self, l: int, r: int) -> tuple[int, int]:
        """
        Вернуть нормализованный двойной хеш полуинтервала [l, r).
        Индексация 0-based.
        """
        size = self.size

        l += size
        r += size

        l0 = l
        r0 = r

        lazy = self.lazy
        push = self._push

        # Перед частичными запросами проталкиваем отложенные присваивания.
        for i in self.down:
            if ((l0 >> i) << i) != l0:
                v = l0 >> i
                if lazy[v] != -1:
                    push(v)

            if ((r0 >> i) << i) != r0:
                v = (r0 - 1) >> i
                if lazy[v] != -1:
                    push(v)

        h1 = self.h1
        h2 = self.h2
        length = self.length
        pow1 = self.pow1
        pow2 = self.pow2
        mask = MASK

        left_h1 = 0
        left_h2 = 0
        left_len = 0

        right_h1 = 0
        right_h2 = 0

        while l < r:
            if l & 1:
                ln = length[l]

                left_h1 = (left_h1 + h1[l] * pow1[left_len]) & mask
                left_h2 = (left_h2 + h2[l] * pow2[left_len]) & mask

                left_len += ln
                l += 1

            if r & 1:
                r -= 1
                ln = length[r]

                # Добавляем узел слева от уже накопленного правого куска.
                right_h1 = (h1[r] + right_h1 * pow1[ln]) & mask
                right_h2 = (h2[r] + right_h2 * pow2[ln]) & mask

            l >>= 1
            r >>= 1

        return (
            (left_h1 + right_h1 * pow1[left_len]) & mask,
            (left_h2 + right_h2 * pow2[left_len]) & mask,
        )


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("".join(result))


if __name__ == "__main__":
    main()
