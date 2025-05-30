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
                case "m":
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

    def query(self, q: tuple[str, int, *tuple[int, ...]]) -> int | None:

        command = q[0]
        match command:
            case "m":
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


def main() -> None:

    solver = Solver()
    solver.parse_data()


if __name__ == "__main__":
    main()
