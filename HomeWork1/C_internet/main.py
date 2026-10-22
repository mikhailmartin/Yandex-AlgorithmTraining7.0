import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    m = int(lines[0])
    seconds = list(map(int, lines[1].split()))

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

            option1 = (seconds_paid + div * seconds_by_card,
                       cost_paid + div * cost_by_card)
            option2 = (m, cost_paid + (div + 1) * cost_by_card)

            buffer.append(option1)
            if mod:
                buffer.append(option2)

        for seconds_paid, cost_paid in buffer:
            if payment_options.get(seconds_paid, float("+inf")) > cost_paid:
                payment_options[seconds_paid] = cost_paid

    return payment_options[m]


if __name__ == "__main__":
    result = main()
    print(result)
