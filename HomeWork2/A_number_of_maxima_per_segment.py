"""
Количество максимумов на отрезке

Ограничение времени - 6 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Реализуйте структуру данных для эффективного вычисления максимального значения
из нескольких подряд идущих элементов массива, а также количества элементов,
равных максимальному на данном отрезке.


Формат ввода:
В первой строке вводится одно натуральное число N (1 ≤ N ≤ 100000) —
количество чисел в массиве.

Во второй строке вводятся N чисел от 1 до 100_000 — элементы массива.

В третьей строке вводится одно натуральное число K (1 ≤ K ≤ 30_000) —
количество запросов на вычисление максимума.

В следующих K строках вводится по два числа — номера левого и правого элементов
отрезка массива (считается, что элементы массива нумеруются с единицы).


Формат вывода:
Для каждого запроса выведите в отдельной строке через пробел значение
максимального элемента на указанном отрезке массива и количество максимальных
элементов на этом отрезке.


Пример
input: 5
input: 2 2 2 1 5
input: 2
input: 2 3
input: 2 5
output: 2 2
output: 5 1
"""
import math


def main() -> None:

    array, queries = parse_data()
    sparse_table, depths = build_sparse_table(array)
    answer = []
    for left, right in queries:
        max_, count_ = query(sparse_table, depths, left, right)
        answer.append(f"{max_} {count_}")
    print("\n".join(answer))


def parse_data() -> tuple[list[int], list[tuple[int, int]]]:

    n = int(input())
    array = list(map(int, input().split()))
    k = int(input())
    queries = []
    for _ in range(k):
        left, right = map(int, input().split())
        queries.append((left, right))

    return array, queries


def build_sparse_table(array: list[int]) -> tuple[list[list], list[int]]:

    array = [(0, 0)] + [(num, 1) for num in array]
    array_length = len(array) - 1
    depths = [-1] + [int(math.log2(length)) for length in range(1, array_length+1)]

    sparse_table = [array]
    prev_line = array
    for depth in range(1, depths[array_length]+1):
        window = pow(2, depth)
        gap = pow(2, depth-1)
        line = [(0, 0)]
        for j in range(1, array_length - window + 2):
            left_max, left_count = prev_line[j]
            right_max, right_count = prev_line[j+gap]
            if left_max > right_max:
                new_max = left_max
                new_count = left_count
            elif right_max > left_max:
                new_max = right_max
                new_count = right_count
            else:  # left_max == right_max
                new_max = left_max
                new_count = left_count + right_count
            line.append((new_max, new_count))
        sparse_table.append(line)
        prev_line = line

    return sparse_table, depths


def query(
    sparse_table: list[list],
    depths: list[int],
    left_array_pointer: int,
    right_array_pointer: int,
) -> tuple[int, int]:

    segment_length = right_array_pointer - left_array_pointer + 1
    depth = depths[segment_length]
    line = sparse_table[depth]
    window = pow(2, depth)
    left_line_pointer = left_array_pointer
    right_line_pointer = left_array_pointer + (segment_length - window)
    if left_line_pointer == right_line_pointer:
        max_, count_ = line[left_line_pointer]
    else:
        left_max, left_count = line[left_line_pointer]
        right_max, right_count = line[right_line_pointer]
        if left_max > right_max:
            max_ = left_max
            count_ = left_count
        elif right_max > left_max:
            max_ = right_max
            count_ = right_count
        else:    # left_max == right_max
            max_ = left_max
            count_ = left_count + right_count
            intersect_max, intersect_count = query(
                sparse_table,
                depths,
                left_array_pointer + (segment_length - window),
                right_array_pointer - (segment_length - window),
            )
            if intersect_max == max_:
                count_ -= intersect_count

    return max_, count_


if __name__ == "__main__":
    main()
