"""
Ни больше ни меньше

Ограничение времени - 2 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дан массив целых положительных чисел a длины n. Разбейте его на минимально
возможное количество отрезков, чтобы каждое число было не меньше длины отрезка,
которому оно принадлежит. Длиной отрезка считается количество чисел в нём.

Разбиение массива на отрезки считается корректным, если каждый элемент
принадлежит ровно одному отрезку.


Формат ввода:
Первая строка содержит одно целое число t (1 ≤ t ≤ 1000) — количество наборов
тестовых данных. Затем следуют t наборов тестовых данных.

Первая строка набора тестовых данных содержит одно целое число (1 ≤ n ≤ 10^5) —
длину массива.

Следующая строка содержит n целых чисел a_1, a_2, …, a_n (1 ≤ a_i ≤ n) —
массив a.

Гарантируется, что сумма n по всем наборам тестовых данных не превосходит 2⋅10^5.


Формат вывода:
Для каждого набора тестовых данных в первой строке выведите число k —
количество отрезков в вашем разбиении.

Затем в следующей строке выведите k чисел len_1, len_2, …, len_k
(1 ≤ len_i ≤ n, sum^k_{i=1} len_i = n) — длины отрезков в порядке слева направо.


Пример
input: 3
input: 5
input: 1 3 3 3 2
input: 16
input: 1 9 8 7 6 7 8 9 9 9 9 9 9 9 9 9
input: 7
input: 7 2 3 4 3 2 7
output: 3
output: 1 2 2
output: 3
output: 1 6 9
output: 3
output: 2 3 2


Примечания:
Ответы в примере соответствуют разбиениям:
{[1], [3, 3], [3, 2]}
{[1], [9, 8, 7, 6, 7, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]}
{[7, 2], [3, 4, 3], [2, 7]}

В первом наборе тестовых данных набор длин {1, 3, 1}, соответствующий разбиению
{[1], [3, 3, 3], [2]}, также был бы корректным.
"""
def main() -> None:

    test_samples = parse_data()
    for test_sample in test_samples:
        k, len_k = solve(test_sample)
        print(k)
        print(*len_k)


def parse_data() -> list[list[int]]:

    test_samples = []

    t = int(input())
    for _ in range(t):
        n = int(input())
        test_sample = list(map(int, input().split()))
        test_samples.append(test_sample)

    return test_samples


def solve(test_sample: list[int]) -> tuple[int, list[int]]:

    counter = 0
    lengths = []

    length = 0
    min_number = float("+inf")
    for number in test_sample:

        if number > length and min_number > length:
            length += 1
            min_number = min(min_number, number)
        else:
            counter += 1
            lengths.append(length)
            length = 1
            min_number = number

    if length > 0:
        counter += 1
        lengths.append(length)

    return counter, lengths


if __name__ == "__main__":
    main()
