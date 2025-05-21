"""
K-й ноль

Ограничение времени - 15 секунд
Ограничение памяти - 1024Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Реализуйте эффективную структуру данных, позволяющую изменять элементы массива и
вычислять индекс k-го слева нуля на данном отрезке в массиве.


Формат ввода:
В первой строке вводится одно натуральное число N (1 ≤ N ≤ 200_000) —
количество чисел в массиве.

Во второй строке вводятся N чисел от 0 до 100_000 — элементы массива.

В третьей строке вводится одно натуральное число M (1 ≤ M ≤ 200_000) —
количество запросов.

Каждая из следующих M строк представляет собой описание запроса. Сначала
вводится одна буква, кодирующая вид запроса (s — вычислить индекс k-го нуля,
u — обновить значение элемента).

Следом за s вводится три числа — левый и правый концы отрезка и число k (1 ≤ k ≤ N).

Следом за u вводятся два числа — номер элемента и его новое значение.


Формат вывода:
Для каждого запроса s выведите результат. Все числа выводите в одну строку через
пробел. Если нужного числа нулей на запрашиваемом отрезке нет, выводите −1 для
данного запроса.


Пример
input: 5
input: 0 0 3 0 2
input: 3
input: u 1 5
input: u 1 0
input: s 1 5 3
output: 4
"""
from typing import Any
import math


class Solver:
    def __init__(
        self,
        array: list[int] | None = None,
        queries: list[tuple] | None = None,
        segment_tree: list[int] | None = None,
        shift: int | None = None,
        fill_value: Any | None = None,
    ) -> None:
        self.array = array
        self.queries = queries or []
        self.segment_tree = segment_tree
        self.shift = shift
        self.fill_value = fill_value

    def parse_data(self) -> None:

        n = int(input())
        self.array = list(map(int, input().split()))
        m = int(input())
        for _ in range(m):
            command, _, operands = input().partition(" ")
            match command:
                case "s":
                    left, right, k = map(int, operands.split())
                    self.queries.append((command, left, right, k))
                case "u":
                    number, value = map(int, operands.split())
                    self.queries.append((command, number, value))

    def build_segment_tree(self) -> None:

        self.fill_value = 0
        power = int(math.log2(len(self.array))) + 1
        self.shift = (pow(2, power) - 1)
        self.segment_tree = (
            [self.fill_value] * self.shift
            + [int(element == 0) for element in self.array]
            + [self.fill_value] * (pow(2, power) - len(self.array))
        )
        for index in reversed(range(pow(2, power) - 1)):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            self.segment_tree[index] = self.segment_tree[left_child_index] + self.segment_tree[right_child_index]

    def solve(self) -> None:

        answer = []
        for query in self.queries:
            command = query[0]
            match command:
                case "s":
                    left, right, k = query[1:]

                    _, pos = self.s_query(
                        left_segment_border=left-1,
                        right_segment_border=right-1,
                        node_index=0,
                        left_node_border=0,
                        right_node_border=self.shift,
                        k=k,
                    )

                    answer.append(str(pos+1))
                case "u":
                    number, value = query[1:]
                    self.u_query(number, value)

        print(" ".join(answer))

    def s_query(
        self,
        left_segment_border: int,
        right_segment_border: int,
        node_index: int,
        left_node_border: int,
        right_node_border: int,
        k: int,
    ) -> tuple[int, int]:
        """
        Возвращает номер k-ого нуля в исходном массиве на заданном подотрезке.

        Задача поиска номера в исходном массиве k-ого нуля на подотрезке данного массива
        сводится к поиску в глубину k-ого нуля.
        """
        if (
            # сегмент полностью накрывает узел
            left_segment_border <= left_node_border
            and right_segment_border >= right_node_border
            # и в нём количество нулей меньше k
            and (zero_count := self.segment_tree[node_index]) < k
        ):
            return zero_count, -2

        # мимо
        if (
            right_segment_border < left_node_border
            or left_segment_border > right_node_border
        ):
            zero_count = 0
            return zero_count, -2

        # локализовали k-ый нуль
        if (
            left_node_border == right_node_border
            and (zero_count := self.segment_tree[node_index]) == 1
            and k == 1
        ):
            return zero_count, left_node_border

        # ищем k-ый нуль сначала в левой ветке
        left_zero_count, number = self.s_query(
            left_segment_border,
            right_segment_border,
            node_index=2*node_index+1,
            left_node_border=left_node_border,
            right_node_border=(left_node_border+right_node_border)//2,
            k=k,
        )
        # если нашли, поднимаем наверх
        if number != -2:
            return left_zero_count, number
        if left_zero_count < k:
            k -= left_zero_count

        now_zero_count = left_zero_count

        right_zero_count, number = self.s_query(
            left_segment_border,
            right_segment_border,
            node_index=2*node_index+2,
            left_node_border=(left_node_border+right_node_border)//2+1,
            right_node_border=right_node_border,
            k=k,
        )
        if number != -2:
            return right_zero_count, number
        now_zero_count += right_zero_count

        return now_zero_count, -2

    def u_query(self, number: int, value: int) -> None:

        index = number + self.shift - 1
        if value == 0:
            self.segment_tree[index] = 1
        else:
            self.segment_tree[index] = 0
        parent_index = (index - 1) // 2
        flag = True
        while flag:
            # если дошли до корня дерева
            if parent_index == 0:
                flag = False
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            old_parent_value = self.segment_tree[parent_index]
            new_parent_value = self.segment_tree[left_child_index] + self.segment_tree[right_child_index]
            # если обновление не задело значение в родительском узле
            if old_parent_value != new_parent_value:
                self.segment_tree[parent_index] = new_parent_value
                parent_index = (parent_index - 1) // 2
            else:
                flag = False

def main() -> None:

    solver = Solver()
    solver.parse_data()
    solver.build_segment_tree()
    solver.solve()


if __name__ == "__main__":
    main()
