"""
Интернет

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Новый интернет-провайдер предоставляет услугу доступа в интернет с посекундной
тарификацией. Для подключения нужно купить карточку, позволяющую пользоваться
интернетом определённое количество секунд. При этом компания продаёт карточки
стоимостью 1, 2, 4, …, 2^30 рублей на a_0, a_1, a_2, …, a_30 секунд
соответственно.

Родители разрешили Пете пользоваться интернетом M секунд. Определите, за какую
наименьшую сумму он сможет купить карточки, которые позволят ему пользоваться
интернетом не менее M секунд. Естественно, Петя может купить как карточки
различного достоинства, так и несколько карточек одного достоинства.


Формат ввода:
В первой строке содержится единственное натуральное число M (1 ≤ M ≤ 10^9). Во
второй строке задаются натуральные числа a_0, a_1, …, a_30, не превосходящие 10^9.


Формат вывода:
Выведите единственное число — наименьшую сумму денег, которую Пете придётся
потратить.


Пример:
input: 11
input: 1 1 10 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
output: 5
"""


def main() -> None:

    m, seconds = parse_data()
    result = solve(m, seconds)
    print(result)


def parse_data() -> tuple[int, list[int]]:

    m = int(input())
    seconds = list(map(int, input().split()))

    return m, seconds


def solve(m: int, seconds: list[int]) -> int:

    cards = []
    for precost, seconds in enumerate(seconds):
        cost = 2 ** precost
        efficiency = seconds / cost
        cards.append((cost, seconds, efficiency))
    # сортируем карточки сначала по убыванию эффективности,
    # затем по убыванию количества секунд
    cards = sorted(cards, key=lambda x: (-x[2], -x[1]))

    payment_options = {0: 0}
    for cost_by_card, seconds_by_card, _ in cards:
        buffer = []
        for seconds_paid, cost_paid in payment_options.items():
            seconds_remaining = m - seconds_paid
            div, mod = divmod(seconds_remaining, seconds_by_card)

            option1 = (seconds_paid + div*seconds_by_card, cost_paid + div*cost_by_card)
            option2 = (m, cost_paid + (div+1)*cost_by_card)

            buffer.append(option1)
            if mod:
                buffer.append(option2)

        for seconds_paid, cost_paid in buffer:
            if payment_options.get(seconds_paid, float("+inf")) > cost_paid:
                payment_options[seconds_paid] = cost_paid

    return payment_options[m]


if __name__ == "__main__":
    main()
