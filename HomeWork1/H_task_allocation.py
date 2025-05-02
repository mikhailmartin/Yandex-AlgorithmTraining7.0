"""
Распределение задач*

Ограничение времени - 3 секунды
Ограничение памяти - 512Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Вася и Маша организовали производство бирдекелей. Они договорились работать день
через день, при этом Вася любит простую и понятную работу, а Маша — сложную и
творческую. В первый день работает Вася, во второй — Маша, потом снова Вася и
т.д.

К ним поступило N заказов, для каждого заказа известна его продолжительность в
днях и для каждого из дней известно, будет ли в этот день работа сложной или
простой. Заказы можно выполнять в любом порядке, перерывов между заказами нет.

Определите такой порядок выполнения заказов, чтобы Вася получил как можно больше
простых задач, а Маша — сложных.


Формат ввода:
В первой строке задается число N (1 ≤ N ≤ 100_000) — количество заказов.

В следующих N строках описываются заказы. Каждое описание представляет собой
строку, состоящую из символов S и D, обозначающих, соответственно, простую и
сложную работу в этот день. Длина строки не превосходит 100 символов. Суммарная
длина всех строк не превосходит 1_000_000 символов.


Формат вывода:
Выведите одно число — максимальное количество дней с простой работой, которые
достанутся Васе.


Пример
input: 4
input: DSD
input: SS
input: DD
input: SDD
output: 3


Примечания
Наибольшее количество дней с простой работой достается Васе при выполнении работ
в порядке SDD, SS, DD, DSD.
"""
def main() -> None:

    orders = parse_data()
    result = solve(orders)
    print(result)


def parse_data() -> list[str]:

    n = int(input())
    orders = [input() for _ in range(n)]

    return orders


def solve(orders: list[str]) -> int:

    even_items = []
    odd_items = []
    for order in orders:
        even_s_count = order[::2].count("S")
        odd_s_count = order[1::2].count("S")
        if len(order) % 2 == 0:
            even_items.append((even_s_count, odd_s_count))
        else:
            odd_items.append((even_s_count, odd_s_count))

    result = 0
    if not odd_items:
        for even_s_count, odd_s_count in even_items:
            result += even_s_count
    else:
        for even_s_count, odd_s_count in even_items:
            result += max(even_s_count, odd_s_count)

        odd_items = sorted(odd_items, key=lambda x: x[1] - x[0])

        left_pointer = 0
        right_pointer = len(odd_items) - 1
        step = 0
        while left_pointer <= right_pointer:
            if step == 0:
                result += odd_items[left_pointer][0]
                left_pointer += 1
            else:
                result += odd_items[right_pointer][1]
                right_pointer -= 1
            step = 1 - step

    return result


if __name__ == "__main__":
    main()
