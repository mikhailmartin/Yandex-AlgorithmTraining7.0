"""
Простая река

Ограничение времени - 2 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Во Флатландии протекает богатая рыбой река Большой Флат. Много лет назад река
была поделена между n рыболовными предприятиями, каждое из которых получило
непрерывный отрезок реки. При этом i-е предприятие, если рассматривать их по
порядку, начиная от истока, изначально получило отрезок реки длиной a_i.

С тех пор с рыболовными предприятиями во Флатландии k раз происходили различные
события. Каждое из событий было одного из двух типов: банкротство некоторого
предприятия или разделение некоторого предприятия на два.

При некоторых событиях отрезок реки, принадлежащий предприятию, с которым это
событие происходит, делится на две части. Каждый такой отрезок имеет длину
большую или равную 2. Деление происходит по следующему правилу. Если отрезок
имеет чётную длину, то он делится на две равные части. Иначе он делится на две
части, длины которых различаются ровно на единицу, при этом часть, которая ближе
к истоку реки, имеет меньшую длину.

При банкротстве предприятия происходит следующее. Отрезок реки, принадлежавший
обанкротившемуся предприятию, переходит к его соседям. Если у обанкротившегося
предприятия один сосед, то этому соседу целиком передаётся отрезок реки
обанкротившегося предприятия. Если же соседей двое, то отрезок реки делится на
две части описанным выше способом, после чего каждый из соседей присоединяет к
своему отрезку ближайшую к нему часть.

При разделении предприятия отрезок реки, принадлежавший разделяемому
предприятию, всегда делится на две части описанным выше способом. Разделившееся
предприятие ликвидируется, и образуются два новых предприятия. Таким образом,
после каждого события каждое предприятие владеет некоторым отрезком реки.

Министерство финансов Флатландии предлагает ввести налог на рыболовные
предприятия, пропорциональный квадрату длины отрезка реки, принадлежащего
соответствующему предприятию. Чтобы проанализировать, как будет работать этот
налог, министр хочет по имеющимся данным узнать, как изменялась величина, равная
сумме квадратов длин отрезков реки, принадлежащих предприятиям, после каждого
произошедшего события.

Требуется написать программу, которая по заданному начальному разделению реки
между предприятиями и списку событий, происходивших с предприятиями, определит,
чему равна сумма квадратов длин отрезков реки, принадлежащих предприятиям, в
начальный момент времени и после каждого события.


Формат ввода:
Первая строка ввода содержит число n — исходное количество предприятий
(2 ≤ n ≤ 100_000).

Вторая строка входного файла содержит n целых чисел a_1, a_2, ..., a_n — длины
исходных отрезков реки.

Третья строка входного файла содержит целое число k — количество событий,
происходивших с предприятиями (1 ≤ k ≤ 100_000).

Последующие k строк содержат описания событий, i-я строка содержит два целых
числа: e_i и v_i — тип события и номер предприятия, с которым оно произошло.
Значение e_i = 1 означает, что предприятие, которое после всех предыдущих
событий является v_i-м по порядку, если считать с единицы от истока реки,
обанкротилось, а значение e_i = 2 означает, что это предприятие разделилось на
два.

Гарантируется, что значение v_i не превышает текущее количество предприятий.
Гарантируется, что если отрезок предприятия при банкротстве или разделении
требуется поделить на две части, то он имеет длину большую или равную 2.
Гарантируется, что если на реке осталось единственное предприятие, оно не
банкротится.

В случае, если n > 100 гарантируется, что для всех i от 1 до k−1 выполнено
условие: ∣v_i − v_{i+1}∣ ≤ 10.


Формат вывода:
Вывод должен содержать k+1 целое число, по одному в строке. Первая строка должна
содержать исходную сумму квадратов длин отрезков реки, а каждая из последующих k
строк — сумму квадратов длин отрезков реки после очередного события.


Пример
input: 4
input: 3 5 5 4
input: 5
input: 1 1
input: 2 1
input: 1 3
input: 2 2
input: 1 3
output: 75
output: 105
output: 73
output: 101
output: 83
output: 113
"""
import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ListNode:
    value: int
    next: Self | None = None
    prev: Self | None = None


class River:
    def __init__(self, lengths: list[int]) -> None:
        self.squared_sum = 0
        next = None
        while lengths:
            length = lengths.pop()
            node = ListNode(length, next=next)
            if next:
                next.prev = node
            next = node
            self.squared_sum += length * length

        self.pointer = next
        self.index = 0

    def bankruptcy(self, idx: int) -> None:
        self._move_pointer(idx)

        self.squared_sum -= self.pointer.value * self.pointer.value

        if self.pointer.prev and self.pointer.next:
            left_value, right_value = self._split_value(self.pointer.value)

            self.squared_sum -= self.pointer.prev.value * self.pointer.prev.value
            self.pointer.prev.value += left_value
            self.pointer.prev.next = self.pointer.next
            self.squared_sum += self.pointer.prev.value * self.pointer.prev.value

            self.squared_sum -= self.pointer.next.value * self.pointer.next.value
            self.pointer.next.value += right_value
            self.pointer.next.prev = self.pointer.prev
            self.squared_sum += self.pointer.next.value * self.pointer.next.value

            self.pointer = self.pointer.next

        elif self.pointer.prev:
            self.squared_sum -= self.pointer.prev.value * self.pointer.prev.value
            self.pointer.prev.value += self.pointer.value
            self.pointer.prev.next = self.pointer.next
            self.squared_sum += self.pointer.prev.value * self.pointer.prev.value

            self.pointer = self.pointer.prev
            self.index -= 1

        else:
            self.squared_sum -= self.pointer.next.value * self.pointer.next.value
            self.pointer.next.value += self.pointer.value
            self.pointer.next.prev = self.pointer.prev
            self.squared_sum += self.pointer.next.value * self.pointer.next.value

            self.pointer = self.pointer.next


    def split(self, idx: int) -> None:
        self._move_pointer(idx)

        left_value, right_value = self._split_value(self.pointer.value)

        self.squared_sum -= self.pointer.value * self.pointer.value
        self.squared_sum += left_value * left_value + right_value * right_value

        self.pointer.value = left_value

        node = ListNode(right_value, prev=self.pointer, next=self.pointer.next)
        if self.pointer.next:
            self.pointer.next.prev = node
        self.pointer.next = node

    def _move_pointer(self, idx: int) -> None:
        while idx != self.index:
            if idx > self.index:
                self.index += 1
                self.pointer = self.pointer.next
            else:
                self.index -= 1
                self.pointer = self.pointer.prev

    @staticmethod
    def _split_value(value: int) -> tuple[int, int]:
        left_value = right_value = value // 2
        right_value += value % 2
        return left_value, right_value

@dataclass
class ProblemInput:
    n: int
    lengths: list[int]
    k: int
    events: list[tuple[int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(sys.stdin.readline().strip())
        lengths = list(map(int, sys.stdin.readline().strip().split()))

        k = int(sys.stdin.readline().strip())
        events = []
        for _ in range(k):
            e, v = map(int, sys.stdin.readline().strip().split())
            events.append((e, v))

        return cls(ProblemInput(n, lengths, k, events))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        lengths = list(map(int, lines[1].split()))

        k = int(lines[2])
        events = []
        for j in range(k):
            e, v = map(int, lines[j+3].split())
            events.append((e, v))

        return cls(ProblemInput(n, lengths, k, events))

    def solve(self) -> list[int]:

        river = River(self.data.lengths)

        result = [river.squared_sum]
        for e, v in self.data.events:
            if e == 1:
                river.bankruptcy(v-1)
            else:
                river.split(v-1)
            result.append(river.squared_sum)

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
