"""
Снеговики

Ограничение времени - 4 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Зима. 2012 год. На фоне грядущего Апокалипсиса и конца света незамеченной прошла
новость об очередном прорыве в областях клонирования и снеговиков: клонирования
снеговиков. Вы конечно знаете, но мы вам напомним, что снеговик состоит из нуля
или более вертикально поставленных друг на друга шаров, а клонирование — это
процесс создания идентичной копии (клона).

В местечке Местячково учитель Андрей Сергеевич Учитель купил через
интернет-магазин «Интернет-магазин аппаратов клонирования» аппарат для
клонирования снеговиков. Теперь дети могут играть и даже играют во дворе в
следующую игру. Время от времени один из них выбирает понравившегося снеговика,
клонирует его и:
- либо добавляет ему сверху один шар;
- либо удаляет из него верхний шар (если снеговик не пустой).
Учитель Андрей Сергеевич Учитель записал последовательность действий и теперь
хочет узнать суммарную массу всех построенных снеговиков.


Формат ввода:
Первая строка содержит количество действий n (1 ≤ n ≤ 200_000). В строке номер
i+1 содержится описание действия i:
- t m — клонировать снеговика номер t (0 ≤ t < i) и добавить сверху шар массой
  m (0 < m ≤ 1000);
- t 0 — клонировать снеговика номер t (0 ≤ t < i) и удалить верхний шар.
  Гарантируется, что снеговик t не пустой.
В результате действия i, описанного в строке i+1 создаётся снеговик номер i.
Изначально имеется пустой снеговик с номером ноль.

Все числа во входном файле целые.


Формат вывода:
Выведите суммарную массу построенных снеговиков.


Пример
input: 8
input: 0 1
input: 1 5
input: 2 4
input: 3 2
input: 4 3
input: 5 0
input: 6 6
input: 1 0
output: 74
"""
import sys
from dataclasses import dataclass
from typing import Self


class PersistentStack:
    def __init__(self) -> None:
        self.versions = [(-1, 0)]

    def push(self, value: int, version: int) -> None:
        _, prev_value  = self.versions[version]
        self.versions.append((version, prev_value + value))

    def pop(self, version: int) -> None:
        prev_version, _ = self.versions[version]
        self.versions.append(self.versions[prev_version])


@dataclass
class ProblemInput:
    n: int
    actions: list[tuple[int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(sys.stdin.readline().strip())
        actions = []
        for _ in range(n):
            t, m = map(int, sys.stdin.readline().strip().split())
            actions.append((t, m))
        return cls(ProblemInput(n, actions))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0].strip())
        actions = []
        for i in range(n):
            t, m = map(int, lines[i+1].split())
            actions.append((t, m))
        return cls(ProblemInput(n, actions))

    def solve(self) -> int:

        persistent_stack = PersistentStack()
        for t, m in self.data.actions:
            if m == 0:
                persistent_stack.pop(t)
            else:
                persistent_stack.push(m, t)

        return sum(node[1] for node in persistent_stack.versions)


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
