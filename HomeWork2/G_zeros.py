"""
Нолики

Ограничение времени - 6 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Дедус любит давать своим ученикам сложные задачки. На этот раз он придумал такую
задачу:

Рейтинг всех его учеников записан в массив A. Запросы Дедуса таковы:
1. Изменить рейтинг i-го ученика на число x
2. Найти максимальную последовательность подряд идущих ноликов в массиве A
на отрезке [l, r].


Формат ввода:
В первой строке входного файла записано число N (1 ≤ N ≤ 500_000) —
количество учеников.

Во второй строке записано N чисел — их рейтинги, числа по модулю
не превосходящие 1000 (по количеству задач, которые ученик решил или не решил
за время обучения).

В третьей строке записано число M (1 ≤ M ≤ 50_000) — количество запросов.
Каждая из следующих M строк содержит описания запросов:

<<UPDATE i x>> — обновить i-ый элемент массива значением x (1 ≤ i ≤ N, ∣x∣ ≤ 1000)
<<QUERY l r>> — найти длину максимальной последовательности из нулей на отрезке
с l по r (1 ≤ l ≤ r ≤ N).


Формат вывода:
В выходной файл выведите ответы на запросы <<QUERY>> в том же порядке,
что и во входном файле.


Пример
input: 5
input: 328 0 0 0 0
input: 5
input: QUERY 1 3
input: UPDATE 2 832
input: QUERY 3 3
input: QUERY 2 3
input: UPDATE 2 0
output: 2
output: 1
output: 1
"""
from collections import namedtuple


Node = namedtuple("Node", ["counter", "prefix", "postfix", "flag"])


class Filler(Node):
    ...


class Solver:
    def __init__(
        self,
        array: list[int] | None = None,
        queries: list[tuple[str, int, int]] | None = None,
        segment_tree: list[Node] | None = None,
        shift: int | None = None,
    ) -> None:
        self.array = array
        self.queries = queries or []
        self.segment_tree = segment_tree or []
        self.shift = shift

    def parse_data(self) -> None:

        n = int(input())
        self.array = list(map(int, input().split()))
        m = int(input())
        for _ in range(m):
            command, operand1, operand2 = input().split()
            self.queries.append((command, int(operand1), int(operand2)))

    def build_segment_tree(self) -> None:

        size = 1
        while size < len(self.array):
            size *= 2
        self.shift = size - 1

        for _ in range(self.shift):
            self.segment_tree.append(Filler(0, 0, 0, False))
        for element in self.array:
            is_zero = int(element == 0)
            self.segment_tree.append(Node(is_zero, is_zero, is_zero, bool(is_zero)))
        for _ in range(size - len(self.array)):
            self.segment_tree.append(Filler(0, 0, 0, False))

        for index in reversed(range(size - 1)):
            self.segment_tree[index] = self.build_node_from_index(index)

    def build_node_from_index(self, index: int) -> Node:

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        left_child_node = self.segment_tree[left_child_index]
        right_child_node = self.segment_tree[right_child_index]

        node = self.build_node_from_nodes(left_child_node, right_child_node)

        return node

    @staticmethod
    def build_node_from_nodes(left_node: Node, right_node: Node) -> Node:

        if isinstance(right_node, Filler):
            return left_node

        if left_node.flag:
            if right_node.flag:
                counter = prefix = postfix = left_node.postfix + right_node.prefix
                flag = True
            else:
                counter = prefix = left_node.counter + right_node.prefix
                postfix = right_node.postfix
                flag = False
        else:
            if right_node.flag:
                counter = postfix = left_node.postfix + right_node.counter
                prefix = left_node.prefix
                flag = False
            else:
                counter = max(
                    left_node.counter,
                    right_node.counter,
                    left_node.postfix + right_node.prefix,
                )
                prefix = left_node.prefix
                postfix = right_node.postfix
                flag = False

        node = Node(counter, prefix, postfix, flag)

        return node

    def solve(self) -> None:

        answer = []
        for command, operand1, operand2 in self.queries:
            match command:
                case "UPDATE":
                    self.u_query(operand1, operand2)
                case "QUERY":
                    node = self.s_query(
                        left_segment_border=operand1-1,
                        right_segment_border=operand2-1,
                        left_node_border=0,
                        right_node_border=self.shift,
                    )
                    answer.append(str(node.counter))
                case _:
                    raise ValueError
        print("\n".join(answer))

    def u_query(self, number: int, value: int) -> None:

        index = number + self.shift - 1
        is_zero = int(value == 0)
        self.segment_tree[index] = Node(is_zero, is_zero, is_zero, bool(is_zero))
        parent_index = (index - 1) // 2
        flag = True
        while flag:
            # если дошли до корня дерева
            if parent_index == 0:
                flag = False
            old_parent_value = self.segment_tree[parent_index]
            new_parent_value = self.build_node_from_index(parent_index)
            # если обновление не задело значение в родительском узле
            if old_parent_value != new_parent_value:
                self.segment_tree[parent_index] = new_parent_value
                parent_index = (parent_index - 1) // 2
            else:
                flag = False

    def s_query(
        self,
        left_segment_border: int,
        right_segment_border: int,
        left_node_border: int,
        right_node_border: int,
        node_index: int = 0,
    ) -> Node:

        # мимо
        if (
            right_segment_border < left_node_border
            or left_segment_border > right_node_border
        ):
            return Node(0, 0, 0, False)

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

            left_child_ = self.s_query(
                left_segment_border,
                right_segment_border,
                left_child_left_border,
                left_child_right_border,
                left_child_node_index,
            )
            right_child_ = self.s_query(
                left_segment_border,
                right_segment_border,
                right_child_left_border,
                right_child_right_border,
                right_child_node_index,
            )

            node = self.build_node_from_nodes(left_child_, right_child_)

            return node


def main() -> None:

    solver = Solver()
    solver.parse_data()
    solver.build_segment_tree()
    solver.solve()


if __name__ == "__main__":
    main()
