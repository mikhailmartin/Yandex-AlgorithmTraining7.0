"""
Максимум и индекс максимума на отрезке

Ограничение времени - 6 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Реализуйте структуру данных, которая на данном массиве из N целых чисел
позволяет узнать максимальное значение на этом массиве и индекс элемента,
на котором достигается это максимальное значение.


Формат ввода:
В первой строке вводится натуральное число N (1 ≤ N ≤ 10^5) —
количество элементов в массиве.

В следующей строке содержатся N целых чисел, не превосходящих по модулю 10^9 —
элементы массива. Гарантируется, что в массиве нет одинаковых элементов.

Далее идет число K (0 ≤ K ≤ 10^5) — количество запросов к структуре данных.

Каждая из следующих K строк содержит два целых числа l и r (1 ≤ l ≤ r ≤ N) —
левую и правую границы отрезка в массиве для данного запроса.


Формат вывода:
Для каждого из запросов выведите два числа: наибольшее значение среди элементов
массива на отрезке от l до r и индекс одного из элементов массива, принадлежащий
отрезку от l до r, на котором достигается этот максимум.


Пример
input: 5
input: 7 3 1 6 4
input: 3
input: 1 5
input: 2 4
input: 3 3
output: 7 1
output: 6 4
output: 1 3
"""
import math


def main() -> None:

    array, queries = parse_data()
    sparse_table, depths = build_sparse_table(array)
    answer = []
    for left, right in queries:
        k = query(array, sparse_table, depths, left, right)
        answer.append(f"{array[k-1]} {k}")
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
