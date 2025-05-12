"""
Индекс максимума на отрезке

Ограничение времени - 10 секунд
Ограничение памяти - 1024Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Реализуйте структуру данных для эффективного вычисления номера максимального из
нескольких подряд идущих элементов массива.


Формат ввода:
В первой строке вводится одно натуральное число N (1 ⩽ N ⩽ 100_000) —
количество чисел в массиве.

Во второй строке вводятся N чисел от 1 до 100_000 — элементы массива.

В третьей строке вводится одно натуральное число K (1 ⩽ K ⩽ 300000) —
количество запросов на вычисление максимума.

В следующих K строках вводится по два числа — номера левого и правого элементов
отрезка массива (считается, что элементы массива нумеруются с единицы).


Формат вывода:
Для каждого запроса выведите индекс максимального элемента на указанном отрезке
массива. Если максимальных элементов несколько, выведите любой их них.

Числа выводите по одному в строке.


Пример
input: 5
input: 2 2 2 1 5
input: 2
input: 2 3
input: 2 5
output: 3
output: 5
"""
import math


def main() -> None:

    array, queries = parse_data()
    sparse_table, depths = build_sparse_table(array)
    answer = []
    for left, right in queries:
        k = query(array, sparse_table, depths, left, right)
        answer.append(str(k))
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

    array = [0] + array
    array_length = len(array) - 1
    depths = [-1] + [int(math.log2(length)) for length in range(1, array_length + 1)]

    sparse_table = [[i for i in range(array_length+1)]]
    prev_line = sparse_table[-1]
    for depth in range(1, depths[array_length] + 1):
        window = pow(2, depth)
        gap = pow(2, depth - 1)
        line = [0]
        for j in range(1, array_length - window + 2):
            left_k = prev_line[j]
            right_k = prev_line[j+gap]
            if array[left_k] >= array[right_k]:
                new_k = left_k
            else:
                new_k = right_k
            line.append(new_k)
        sparse_table.append(line)
        prev_line = line

    return sparse_table, depths


def query(
    array: list[int],
    sparse_table: list[list],
    depths: list[int],
    left_array_pointer: int,
    right_array_pointer: int,
) -> int:

    segment_length = right_array_pointer - left_array_pointer + 1
    depth = depths[segment_length]
    line = sparse_table[depth]
    window = pow(2, depth)
    left_line_pointer = left_array_pointer
    right_line_pointer = left_array_pointer + (segment_length - window)
    if left_line_pointer == right_line_pointer:
        k = line[left_line_pointer]
    else:
        left_k = line[left_line_pointer]
        right_k = line[right_line_pointer]
        if array[left_k-1] >= array[right_k-1]:
            k = left_k
        else:
            k = right_k

    return k


if __name__ == "__main__":
    main()
