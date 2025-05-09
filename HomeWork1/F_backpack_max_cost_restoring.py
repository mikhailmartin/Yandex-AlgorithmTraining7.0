"""
Рюкзак: наибольшая стоимость с восстановлением ответа

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дано N предметов массой m_1, …, m_N и стоимостью c_1, …, c_N, соответственно.
Ими наполняют рюкзак, который выдерживает вес не более M. Определите набор
предметов, который можно унести в рюкзаке, имеющий наибольшую стоимость.


Формат ввода:
В первой строке вводится натуральное число N, не превышающее 100, и натуральное
число M, не превышающее 10000.
Во второе строке вводятся N натуральных чисел m_i, не превышающих 100.
Во третьей строке вводятся N натуральных чисел c_i, не превышающих 100.


Формат вывода:
Выведите номера предметов (числа от 1 до N), которые войдут в рюкзак наибольшей
стоимости.


Пример
input: 4 6
input: 2 4 1 2
input: 7 2 5 1
output: 1
output: 3
output: 4
"""
from collections import namedtuple


Item = namedtuple("Item", ["weight", "cost"])
Option = namedtuple("Option", ["sum_cost", "last_index"])


def main() -> None:

    m, items = parse_data()
    result = solve(m, items)
    for i in result:
        print(i)


def parse_data() -> tuple[int, list[Item]]:

    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    items = [Item(weight, cost) for weight, cost in zip(weights, costs)]

    return m, items


def solve(m: int, items: list[Item]) -> list[int]:

    options_2d = get_options_2d(m, items)

    options = options_2d[-1]
    max_cost = float("-inf")
    max_cost_weight_in = None
    max_cost_i = None
    for weight_in, (cost, i) in enumerate(options):
        if cost > max_cost:
            max_cost = cost
            max_cost_weight_in = weight_in
            max_cost_i = i

    i = max_cost_i
    weight = max_cost_weight_in
    result = []
    while i != 0:
        result.append(i)
        options = options_2d[i-1]
        weight -= items[i-1][0]
        _, i = options[weight]

    return result


def get_options_2d(m: int, items: list[Item]) -> list[list[Option]]:

    options_2d = [[Option(0, 0)] + [Option(-1, -1)] * m]
    for i, item in enumerate(items, 1):
        options = options_2d[-1].copy()
        for weight_in in reversed(range(m - item.weight + 1)):
            option_curr = options[weight_in]
            weight_in_added = weight_in + item.weight
            option_added = options[weight_in_added]
            if (
                option_curr.sum_cost != -1
                and option_added.sum_cost < option_curr.sum_cost + item.cost
            ):
                options[weight_in_added] = Option(option_curr.sum_cost + item.cost, i)
        options_2d.append(options)

    return options_2d


if __name__ == "__main__":
    main()
