"""
Ближайшее большее число справа

Ограничение времени - 12 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Дан массив a из n чисел. Нужно обрабатывать запросы:
0. set(i, x) — присвоить новое значение элементу массива a[i] = x;
1. get(i, x) — найти min k: k ≥ i и a_k ≥ x.


Формат ввода:
Первая строка входных данных содержит два числа: длину массива n и количество
запросов m (1 ≤ n, m ≤ 200_000).

Во второй строке записаны n целых чисел – элементы массива a (0 ≤ a_i ≤ 200_000).

Следующие m строк содержат запросы, каждый запрос содержит три числа t, i, x.
Первое число t равно 0 или 1 – тип запроса. t = 0 означает запрос типа set,
t = 1 соответствует запросу типа get, 1 ≤ i ≤ n, 0 ≤ x ≤ 200_000. Элементы
массива нумеруются с единицы.


Формат вывода:
На каждый запрос типа get на отдельной строке выведите соответствующее значение k.
Если такого k не существует, выведите −1.


Пример
input: 4 5
input: 1 2 3 4
input: 1 1 1
input: 1 1 3
input: 1 1 5
input: 0 2 3
input: 1 1 3
output: 1
output: 3
output: -1
output: 2
"""
NO_SOLUTION = -2


class Solver:
    def __init__(
        self,
        array: list[int] | None = None,
        queries: list[tuple] | None = None,
        segment_tree: list[int] | None = None,
        shift: int | None = None,
    ) -> None:
        self.array = array
        self.queries = queries or []
        self.segment_tree = segment_tree
        self.shift = shift

    def parse_data(self):

        n, m = map(int, input().split())
        self.array = list(map(int, input().split()))
        for _ in range(m):
            t, i, x = map(int, input().split())
            self.queries.append((t, i, x))

    def build_segment_tree(self) -> None:

        fill_value = float("-inf")

        size = 1
        while size < len(self.array):
            size *= 2
        self.shift = size - 1
        self.segment_tree = (
            [fill_value] * self.shift
            + self.array
            + [fill_value] * (size - len(self.array))
        )
        for index in reversed(range(size - 1)):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            self.segment_tree[index] = max(
                self.segment_tree[left_child_index],
                self.segment_tree[right_child_index],
            )

    def solve(self) -> None:

        answer = []
        for t, i, x in self.queries:
            match t:
                case 0:
                    self.u_query(i, x)
                case 1:
                    index = self.s_query(
                        left_segment_border=i-1,
                        right_segment_border=self.shift,
                        node_index=0,
                        left_node_border=0,
                        right_node_border=self.shift,
                        value=x,
                    )
                    k = index + 1
                    answer.append(str(k))
                case _:
                    raise ValueError
        print("\n".join(answer))

    def s_query(
        self,
        left_segment_border: int,
        right_segment_border: int,
        node_index: int,
        left_node_border: int,
        right_node_border: int,
        value: int,
    ):
        if (
            left_segment_border >= left_node_border
            and right_segment_border <= right_node_border
            and self.segment_tree[node_index] < value
        ):
            return NO_SOLUTION

        # сегмент полностью накрывает узел
        if (
            left_segment_border <= left_node_border
            and right_segment_border >= right_node_border
        ):
            # и локальный максимум меньше значения
            if self.segment_tree[node_index] < value:
                return NO_SOLUTION

        # мимо
        if (
            right_segment_border < left_node_border
            or left_segment_border > right_node_border
        ):
            return NO_SOLUTION

        # локализовали
        if left_node_border == right_node_border:
            if self.segment_tree[node_index] >= value:
                return left_node_border
            else:
                return NO_SOLUTION

        # ищем ближайшее большее число справа сначала в левой ветке
        number = self.s_query(
            left_segment_border,
            right_segment_border,
            node_index=2*node_index+1,
            left_node_border=left_node_border,
            right_node_border=(left_node_border+right_node_border)//2,
            value=value,
        )
        # если нашли, поднимаем наверх
        if number != NO_SOLUTION:
            return number

        number = self.s_query(
            left_segment_border,
            right_segment_border,
            node_index=2 * node_index + 2,
            left_node_border=(left_node_border + right_node_border) // 2 + 1,
            right_node_border=right_node_border,
            value=value,
        )
        if number != NO_SOLUTION:
            return number

        return NO_SOLUTION

    def u_query(self, number: int, value: int) -> None:

        index = number + self.shift - 1
        self.segment_tree[index] = value
        parent_index = (index - 1) // 2
        flag = True
        while flag:
            # если дошли до корня дерева
            if parent_index == 0:
                flag = False
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            old_parent_value = self.segment_tree[parent_index]
            new_parent_value = max(
                self.segment_tree[left_child_index],
                self.segment_tree[right_child_index],
            )
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
