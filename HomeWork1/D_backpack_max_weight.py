"""
Рюкзак: наибольший вес

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дано N золотых слитков массой m_1, …, m_N. Ими наполняют рюкзак, который
выдерживает вес не более M. Какую наибольшую массу золота можно унести в таком
рюкзаке?


Формат ввода:
В первой строке вводится натуральное число N, не превышающее 100, и натуральное
число M, не превышающее 10000.
Во второй строке вводятся N натуральных чисел m_i, не превышающих 100.


Формат вывода:
Выведите одно целое число — наибольшую возможную массу золота, которую можно
унести в данном рюкзаке.


Пример
input: 1 5968
input: 18
output: 18
"""


def main() -> None:

    m, weights = parse_data()
    result = solve(m, weights)
    print(result)


def parse_data() -> tuple[int, list[int]]:

    n, m = map(int, input().split())
    weights = list(map(int, input().split()))

    return m, weights


def solve(m: int, weights: list[int]) -> int:

    options = set()
    options.add(0)
    for weight in weights:
        buffer = set()
        for option in options:
            remaining = m - option
            if remaining >= weight:
                buffer.add(option + weight)
        options |= buffer

    return max(options)


if __name__ == "__main__":
    main()
