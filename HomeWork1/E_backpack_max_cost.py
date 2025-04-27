"""
Рюкзак: наибольшая стоимость

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дано N предметов массой m_1, …, m_N и стоимостью c_1, …, c_N, соответственно.
Ими наполняют рюкзак, который выдерживает вес не более M. Какую наибольшую
стоимость могут иметь предметы в рюкзаке?


Формат ввода:
В первой строке вводится натуральное число N, не превышающее 100, и натуральное
число M, не превышающее 10000.
Во второе строке вводятся N натуральных чисел m_i, не превышающих 100.
Во третьей строке вводятся N натуральных чисел c_i, не превышающих 100.


Формат вывода:
Выведите наибольшую стоимость рюкзака.


Пример 1
input: 1 597
input: 18
input: 16
output: 16

Пример 2
input: 2 789
input: 45 44
input: 51 41
output: 92
"""
def main() -> None:

    m, items = parse_data()
    result = solve(m, items)
    print(result)


def parse_data() -> tuple[int, list[tuple[int, int]]]:

    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    items = list(zip(weights, costs))

    return m, items


def solve(m: int, items: list[tuple[int, int]]) -> int:

    options = {0: 0}
    for weight_by_item, cost_by_item in items:
        buffer = []
        for weight_in, cost_in in options.items():
            remaining = m - weight_in
            if remaining >= weight_by_item:
                buffer.append((weight_in + weight_by_item, cost_in + cost_by_item))

        for weight_in, cost_in in buffer:
            if options.get(weight_in, float("-inf")) < cost_in:
                options[weight_in] = cost_in

    return max(options.values())


if __name__ == "__main__":
    main()
