"""
Дерево отрезков с операцией на отрезке

Ограничение времени - 5 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Реализуйте эффективную структуру данных для хранения элементов и увеличения
нескольких подряд идущих элементов на одно и то же число.


Формат ввода:
В первой строке вводится одно натуральное число N (1 ⩽ N ⩽ 100_000) —
количество чисел в массиве.

Во второй строке вводятся N чисел от 100_000 — элементы массива.

В третьей строке вводится одно натуральное число M (1 ⩽ M ⩽ 30_000) —
количество запросов.

Каждая из следующих M строк представляет собой описание запроса. Сначала
вводится одна буква, кодирующая вид запроса (g — получить текущее значение
элемента по его номеру, а — увеличить все элементы на отрезке).

Следом за g вводится одно число — номер элемента.

Следом за a вводится три числа — левый и правый концы отрезка и число add,
на которое нужно увеличить все элементы данного отрезка массива (0 ⩽ add ⩽ 100_000).


Формат вывода:
Выведите в одну строку через пробел ответы на каждый запрос g.


Пример
input: 5
input: 2 4 3 5 2
input: 5
input: g 2
input: g 5
input: a 1 3 10
input: g 2
input: g 4
output: 4
output: 2
output: 14
output: 5
"""
class Solver:
    def __init__(
        self,
        array: list[int] | None = None,
        queries: list[tuple[str, int, *tuple[int, ...]]] | None = None,
        segment_tree: list[int] | None = None,
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
            command, _, operands = input().partition(" ")
            match command:
                case "g":
                    number = int(operands)
                    self.queries.append((command, number))
                case "a":
                    left, right, add = map(int, operands.split())
                    self.queries.append((command, left, right, add))

    def build_segment_tree(self, array: list[int] | None = None) -> None:

        if array:
            self.array = array

        size = 1
        while size < len(self.array):
            size *= 2
        self.shift = size - 1

        for _ in range(self.shift):
            self.segment_tree.append(0)
        self.segment_tree.extend(self.array)
        for _ in range(size - len(self.array)):
            self.segment_tree.append(0)

    def solve(self) -> None:

        answer = []
        for q in self.queries:
            if (result := self.query(q)) is not None:
                answer.append(str(result))
        print("\n".join(answer))

    def query(self, q: tuple[str, int, *tuple[int, ...]]) -> int | None:

        command = q[0]
        match command:
            case "g":
                number = q[1]
                return self.get(
                    element_index=number-1,
                    left_node_border=0,
                    right_node_border=self.shift,
                    node_index=0,
                )
            case "a":
                left, right, add = q[1:]
                self.update(
                    left_segment_border=left-1,
                    right_segment_border=right-1,
                    left_node_border=0,
                    right_node_border=self.shift,
                    node_index=0,
                    add=add,
                )
                return None
            case _:
                raise ValueError

    def get(
        self,
        element_index: int,
        left_node_border: int,
        right_node_border: int,
        node_index: int,
    ) -> int:

        if element_index == left_node_border and element_index == right_node_border:
            return self.segment_tree[node_index]
        else:
            left_child_node_index = 2 * node_index + 1
            left_child_left_border = left_node_border
            left_child_right_border = (left_node_border + right_node_border) // 2

            right_child_node_index = 2 * node_index + 2
            right_child_left_border = (left_node_border + right_node_border) // 2 + 1
            right_child_right_border = right_node_border

            # сегмент лежит полностью в левом потомке
            if element_index <= left_child_right_border:
                return self.segment_tree[node_index] + self.get(
                    element_index,
                    left_child_left_border,
                    left_child_right_border,
                    left_child_node_index,
                )
            # сегмент лежит полностью в правом потомке
            elif element_index >= right_child_left_border:
                return self.segment_tree[node_index] + self.get(
                    element_index,
                    right_child_left_border,
                    right_child_right_border,
                    right_child_node_index,
                )
            else:
                raise ValueError

    def update(
        self,
        left_segment_border: int,
        right_segment_border: int,
        left_node_border: int,
        right_node_border: int,
        node_index: int,
        add: int,
    ) -> None:

        if add == 0:
            return

        if (
            left_segment_border == left_node_border
            and right_segment_border == right_node_border
        ):
            self.segment_tree[node_index] += add
        else:
            left_child_node_index = 2 * node_index + 1
            left_child_left_border = left_node_border
            left_child_right_border = (left_node_border + right_node_border) // 2

            right_child_node_index = 2 * node_index + 2
            right_child_left_border = (left_node_border + right_node_border) // 2 + 1
            right_child_right_border = right_node_border

            # сегмент лежит полностью в левом потомке
            if right_segment_border <= left_child_right_border:
                self.update(
                    left_segment_border,
                    right_segment_border,
                    left_child_left_border,
                    left_child_right_border,
                    left_child_node_index,
                    add,
                )
            # сегмент лежит полностью в правом потомке
            elif left_segment_border >= right_child_left_border:
                self.update(
                    left_segment_border,
                    right_segment_border,
                    right_child_left_border,
                    right_child_right_border,
                    right_child_node_index,
                    add,
                )
            # сегмент лежит в обоих потомках
            else:
                self.update(
                    left_segment_border,
                    left_child_right_border,
                    left_child_left_border,
                    left_child_right_border,
                    left_child_node_index,
                    add,
                )
                self.update(
                    right_child_left_border,
                    right_segment_border,
                    right_child_left_border,
                    right_child_right_border,
                    right_child_node_index,
                    add,
                )


def main() -> None:

    solver = Solver()
    solver.parse_data()
    solver.build_segment_tree()
    solver.solve()


if __name__ == "__main__":
    main()
