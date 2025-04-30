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
def main() -> None:

    m, items = parse_data()
    result = solve(m, items)
    for i in result:
        print(i)


def parse_data() -> tuple[int, list[tuple[int, int]]]:

    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    items = list(zip(weights, costs))

    return m, items


def solve(m: int, items: list[tuple[int, int]]) -> list[int]:

    options = get_options(m, items)

    option = options[-1]
    max_cost = float("-inf")
    max_cost_weight_in = None
    max_cost_i = None
    for weight_in, (cost, i) in enumerate(option):
        if cost > max_cost:
            max_cost = cost
            max_cost_weight_in = weight_in
            max_cost_i = i

    i = max_cost_i
    weight = max_cost_weight_in
    result = []
    while i != 0:
        result.append(i)
        option = options[i-1]
        weight -= items[i-1][0]
        _, i = option[weight]

    return result


def get_options(
    m: int, items: list[tuple[int, int]]
) -> list[list[tuple[int, int]]]:

    options = [[(0, 0)] + [(-1, -1)] * m]
    for i, (weight_by_item, cost_by_item) in enumerate(items, 1):
        option = options[i - 1].copy()
        for weight_in in reversed(range(m - weight_by_item + 1)):
            cost_in, _ = option[weight_in]
            if cost_in != -1:
                weight_in_added = weight_in + weight_by_item
                cost_in_added, _ = option[weight_in_added]
                if cost_in_added < cost_in + cost_by_item:
                    option[weight_in_added] = (cost_in + cost_by_item, i)
        options.append(option)

    return options


if __name__ == "__main__":
    main()
