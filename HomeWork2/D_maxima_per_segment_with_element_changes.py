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


Пример
input: 5
input: 1 2 3 4 5
input: 5
input: s 1 5
input: u 3 10
input: s 1 5
input: u 2 12
input: s 1 3
output: 5 10 12
"""
import math


class Solver:
    def __init__(
        self,
        array: list[int] | None = None,
        queries: list[tuple[str, int, int]] | None = None,
        segment_tree: list[int | float] | None = None,
        fill_value: float | None = None,
        shift: int | None = None,
    ) -> None:
        self.array = array
        self.queries = queries or []
        self.segment_tree = segment_tree
        self.fill_value = fill_value
        self.shift = shift

    def parse_data(self) -> None:

        n = int(input())
        self.array = list(map(int, input().split()))
        m = int(input())
        for _ in range(m):
            command, operand1, operand2 = input().split()
            self.queries.append((command, int(operand1), int(operand2)))

    def build_segment_tree(self) -> None:

        self.fill_value = float("-inf")
        power = int(math.log2(len(self.array))) + 1
        self.shift = (pow(2, power) - 1)
        self.segment_tree = (
            [self.fill_value] * self.shift
            + self.array
            + [self.fill_value] * (pow(2, power) - len(self.array))
        )
        for index in reversed(range(pow(2, power) - 1)):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            self.segment_tree[index] = max(
                self.segment_tree[left_child_index],
                self.segment_tree[right_child_index],
            )

    def solve(self) -> None:

        answer = []
        for command, operand1, operand2 in self.queries:
            match command:
                case "s":
                    left_segment_border = operand1 - 1
                    right_segment_border = operand2 - 1
                    node_index = 0
                    left_node_border = 0
                    right_node_border = self.shift

                    maxima = self.s_query(
                        left_segment_border,
                        right_segment_border,
                        node_index,
                        left_node_border,
                        right_node_border,
                    )

                    answer.append(str(maxima))
                case "u":
                    self.u_query(operand1, operand2)
        print(" ".join(answer))

    def s_query(
        self,
        left_segment_border: int,
        right_segment_border: int,
        node_index: int,
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
            return self.segment_tree[node_index]

        # сегмент частично накрывает узел
        else:
            left_child_node_index = 2 * node_index + 1
            left_child_left_border = left_node_border
            left_child_right_border = (left_node_border + right_node_border) // 2

            right_child_node_index = 2 * node_index + 2
            right_child_left_border = (left_node_border + right_node_border) // 2 + 1
            right_child_right_border = right_node_border

            left_child_maxima = self.s_query(
                left_segment_border,
                right_segment_border,
                left_child_node_index,
                left_child_left_border,
                left_child_right_border,
            )
            right_child_maxima = self.s_query(
                left_segment_border,
                right_segment_border,
                right_child_node_index,
                right_child_left_border,
                right_child_right_border,
            )

            return max(left_child_maxima, right_child_maxima)

    def u_query(self, number: int, value: int) -> None:

        index = number + self.shift - 1
        self.segment_tree[index] = value
        parent_index = (index - 1) // 2
        flag = True
        while flag:
            if parent_index == 0:
                flag = False
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            old_parent_value = self.segment_tree[parent_index]
            new_parent_value = max(
                self.segment_tree[left_child_index],
                self.segment_tree[right_child_index],
            )
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
