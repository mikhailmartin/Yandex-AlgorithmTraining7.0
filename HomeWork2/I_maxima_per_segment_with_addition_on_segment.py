"""
Максимум на подотрезках с добавлением на отрезке

Ограничение времени - 5 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Реализуйте эффективную структуру данных для хранения массива и выполнения
следующих операций: увеличение всех элементов данного интервала на одно и то же
число; поиск максимума на интервале.


Формат ввода:
В первой строке вводится одно натуральное число N (1 ≤ N ≤ 100000) —
количество чисел в массиве.

Во второй строке вводятся N чисел от 0 до 100_000 — элементы массива.

В третьей строке вводится одно натуральное число M (1 ≤ M ≤ 30_000) —
количество запросов.

Каждая из следующих M строк представляет собой описание запроса. Сначала
вводится одна буква, кодирующая вид запроса (m — найти максимум, a — увеличить
все элементы на отрезке).

Следом за m вводятся два числа — левая и правая граница отрезка.

Следом за a вводятся три числа — левый и правый концы отрезка и число add,
на которое нужно увеличить все элементы данного отрезка массива (0 ≤ add ≤ 100_000).


Формат вывода:
Выведите в одну строку через пробел ответы на каждый запрос m.


Пример
input: 5
input: 2 4 3 1 5
input: 5
input: m 1 3
input: a 2 4 100
input: m 1 3
input: a 5 5 10
input: m 1 5
output: 4 104 104
"""
class Node:
    def __init__(self, maxima: int | float, prop: int) -> None:
        self.maxima = maxima
        self.prop = prop

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.maxima=}, {self.prop=})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.maxima == other.maxima and self.prop == self.prop
        else:
            raise ValueError


class Solver:
    def __init__(
        self,
        array: list[int] | None = None,
        queries: list[tuple[str, int, int, *tuple[int, ...]]] | None = None,
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
            command, _, operands = input().partition(" ")
            match command:
                case "m":
                    left, right = map(int, operands.split())
                    self.queries.append((command, left, right))
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
            self.segment_tree.append(Node(float("-inf"), 0))
        for elem in self.array:
            self.segment_tree.append(Node(elem, 0))
        for _ in range(size - len(self.array)):
            self.segment_tree.append(Node(float("-inf"), 0))

        for index in reversed(range(self.shift)):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            maxima = max(
                self.segment_tree[left_child_index].maxima,
                self.segment_tree[right_child_index].maxima,
            )
            prop = 0
            self.segment_tree[index] = Node(maxima, prop)

    def solve(self) -> None:

        answer = []
        for q in self.queries:
            if (result := self.query(q)) is not None:
                answer.append(str(result))
        print(" ".join(answer))

    def query(self, q: tuple[str, int, *tuple[int, ...]]) -> int | None:

        command = q[0]
        match command:
            case "m":
                left, right = q[1:]
                return self.get(
                    left_segment_border=left-1,
                    right_segment_border=right-1,
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
        left_segment_border: int,
        right_segment_border: int,
        left_node_border: int,
        right_node_border: int,
        node_index: int,
    ) -> int | float:

        # сегмент полностью накрывает узел
        if (
            left_segment_border <= left_node_border
            and right_segment_border >= right_node_border
        ):
            return self.segment_tree[node_index].maxima + self.segment_tree[node_index].prop

        # сегмент не пересекается с узлом
        elif (
            left_segment_border > right_node_border
            or right_segment_border < left_node_border
        ):
            return float("-inf")

        # сегмент частично накрывает узел
        else:
            left_child_node_index = 2 * node_index + 1
            left_child_left_border = left_node_border
            left_child_right_border = (left_node_border + right_node_border) // 2

            right_child_node_index = 2 * node_index + 2
            right_child_left_border = (left_node_border + right_node_border) // 2 + 1
            right_child_right_border = right_node_border

            if self.segment_tree[node_index].prop:
                self.segment_tree[left_child_node_index].prop += self.segment_tree[node_index].prop
                self.segment_tree[right_child_node_index].prop += self.segment_tree[node_index].prop
                self.segment_tree[node_index].prop = 0
                self.segment_tree[node_index].maxima = max(
                    self.segment_tree[left_child_node_index].maxima + self.segment_tree[left_child_node_index].prop,
                    self.segment_tree[right_child_node_index].maxima + self.segment_tree[right_child_node_index].prop,
                )

            left_child_maxima = self.get(
                left_segment_border,
                right_segment_border,
                left_child_left_border,
                left_child_right_border,
                left_child_node_index,
            )
            right_child_maxima = self.get(
                left_segment_border,
                right_segment_border,
                right_child_left_border,
                right_child_right_border,
                right_child_node_index,
            )

            return max(left_child_maxima, right_child_maxima)

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

        # сегмент полностью накрывает узел
        if (
            left_segment_border <= left_node_border
            and right_segment_border >= right_node_border
        ):
            self.segment_tree[node_index].prop += add

        # сегмент не пересекается с узлом
        elif (
            left_segment_border > right_node_border
            or right_segment_border < left_node_border
        ):
            return

        # сегмент частично накрывает узел
        else:
            left_child_node_index = 2 * node_index + 1
            left_child_left_border = left_node_border
            left_child_right_border = (left_node_border + right_node_border) // 2

            right_child_node_index = 2 * node_index + 2
            right_child_left_border = (left_node_border + right_node_border) // 2 + 1
            right_child_right_border = right_node_border

            if self.segment_tree[node_index].prop:
                self.segment_tree[left_child_node_index].prop += self.segment_tree[node_index].prop
                self.segment_tree[right_child_node_index].prop += self.segment_tree[node_index].prop
                self.segment_tree[node_index].prop = 0

            self.update(
                left_segment_border,
                right_segment_border,
                left_child_left_border,
                left_child_right_border,
                left_child_node_index,
                add,
            )
            self.update(
                left_segment_border,
                right_segment_border,
                right_child_left_border,
                right_child_right_border,
                right_child_node_index,
                add,
            )

            self.segment_tree[node_index].maxima = max(
                self.segment_tree[left_child_node_index].maxima + self.segment_tree[left_child_node_index].prop,
                self.segment_tree[right_child_node_index].maxima + self.segment_tree[right_child_node_index].prop,
            )


def main() -> None:

    solver = Solver()
    solver.parse_data()
    solver.build_segment_tree()
    solver.solve()


if __name__ == "__main__":
    main()
