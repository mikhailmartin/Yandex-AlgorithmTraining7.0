"""
Максимум на подотрезках с изменением элемента

Ограничение времени - 6 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Реализуйте эффективную структуру данных, позволяющую изменять элементы массива и
вычислять максимальное значение из нескольких подряд идущих элементов.


Формат ввода:
В первой строке вводится одно натуральное число N (1 ≤ N ≤ 100_000) —
количество чисел в массиве.

Во второй строке вводятся N чисел от 0 до 100000 — элементы массива.

В третьей строке вводится одно натуральное число M (1 ≤ M ≤ 30000) —
количество запросов.

Каждая из следующих M строк представляет собой описание запроса. Сначала
вводится одна буква, кодирующая вид запроса (s — вычислить максимум,
u — обновить значение элемента).

Следом за s вводятся два числа — номера левой и правой границы отрезка.

Следом за u вводятся два числа — номер элемента и его новое значение.


Формат вывода:
Для каждого запроса s выведите результат. Все числа выводите в одну строку через
пробел.


Пример:
input:
5
1 2 3 4 5
5
s 1 5
u 3 10
s 1 5
u 2 12
s 1 3
output:
5 10 12
"""
import sys
import math


class SegmentTree:
    def __init__(self, array: list[int], fill_value: float = float("-inf")) -> None:
        n = len(array)

        power = int(math.log2(n)) + 1
        size = pow(2, power)  # размер нижнего слоя
        shift = size - 1  # сдвиг в массиве для доступа к нижнему слою

        tree = (
            [fill_value] * shift
            + array  # выстраиваем листья
            + [fill_value] * (size - n)
        )
        # выстраиваем внутренние узлы
        for i in reversed(range(shift)):
            left_child_i = 2 * i + 1
            right_child_i = 2 * i + 2
            tree[i] = max(tree[left_child_i], tree[right_child_i])

        self.shift = shift
        self.fill_value = fill_value
        self.tree = tree

    def s_query(
        self,
        left_segment_border: int,
        right_segment_border: int,
        node_i: int,
        left_node_border: int,
        right_node_border: int,
    ) -> int | float:

        # мимо
        if (
            right_segment_border < left_node_border
            or left_segment_border > right_node_border
        ):
            return self.fill_value

        # сегмент полностью накрывает узел
        elif (
            left_segment_border <= left_node_border
            and right_segment_border >= right_node_border
        ):
            return self.tree[node_i]

        # сегмент частично накрывает узел
        else:
            left_child_node_i = 2 * node_i + 1
            left_child_left_border = left_node_border
            left_child_right_border = (left_node_border + right_node_border) // 2

            right_child_node_i = 2 * node_i + 2
            right_child_left_border = (left_node_border + right_node_border) // 2 + 1
            right_child_right_border = right_node_border

            left_child_maxima = self.s_query(
                left_segment_border,
                right_segment_border,
                left_child_node_i,
                left_child_left_border,
                left_child_right_border,
            )
            right_child_maxima = self.s_query(
                left_segment_border,
                right_segment_border,
                right_child_node_i,
                right_child_left_border,
                right_child_right_border,
            )

            return max(left_child_maxima, right_child_maxima)

    def u_query(self, number: int, value: int) -> None:

        i = number + self.shift - 1
        self.tree[i] = value
        parent_i = (i - 1) // 2
        flag = True
        while flag:
            if parent_i == 0:
                flag = False
            left_child_i = 2 * parent_i + 1
            right_child_i = 2 * parent_i + 2
            old_parent_value = self.tree[parent_i]
            new_parent_value = max(self.tree[left_child_i], self.tree[right_child_i])
            if old_parent_value != new_parent_value:
                self.tree[parent_i] = new_parent_value
                parent_i = (parent_i - 1) // 2
            else:
                flag = False


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    array = list(map(int, lines[1].split()))
    segment_tree = SegmentTree(array)

    result = []
    m = int(lines[2])
    for i in range(m):
        command, operand1, operand2 = lines[3+i].split()
        operand1 = int(operand1)
        operand2 = int(operand2)

        if command == "s":
            maxima = segment_tree.s_query(
                left_segment_border=operand1-1,
                right_segment_border=operand2-1,
                node_i=0,
                left_node_border=0,
                right_node_border=segment_tree.shift,
            )
            result.append(maxima)
        else:
            segment_tree.u_query(operand1, operand2)

    return result


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
