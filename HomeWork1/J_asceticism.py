"""
Аскетизм*

Ограничение времени - 3 секунды
Ограничение памяти - 512Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Вася стал аскетом и решил отказаться от всего материального ради духовного.
Действительно, перспектива переродиться в желтого земляного червяка из-за
утреннего капучино может здорово напугать.

Однако отказываться от материального оказалось не так-то просто. Для каждого
события своей ежедневной материальной жизни Вася определил его материальность и
обозначил её целым положительным числом m_i. Свою духовную силу Вася определил
как число D. Каждый день он может отказываться от одного события материальной
жизни и возвращать некоторые события материальной жизни, от которых он отказался
ранее, чтобы суммарное количество материального снизилось не более чем на D. При
этом нельзя делать так, чтобы количество материальности в какой-либо день
выросло — это собьёт Васю с пути аскезы.

Вася разработал оптимальный план для себя и стал гуру. Теперь его ученики
отказывались от материального в пользу Васи. Учеников оказалось очень много,
Вася успешно определяет их события материального мира и духовную силу, но теперь
ему нужна программа, которая будет разрабатывать план отказа от материального.
В оптимальном плане нужно отказаться от максимального количества событий
материальной жизни, а в случае, если это возможно сделать несколькими способами,
нужно сделать это за наименьшее количество дней.


Формат ввода:
В первой строке записано число N (1 ≤ N ≤ 1000) и D (1 ≤ D ≤ 10000) — количество
событий материальной жизни и духовную силу.

В следующих N строках записано название события материальной жизни (слово,
состоящее не более чем из 40 символов без пробелов) и через пробел его
материальность m_i (1 ≤ m_i ≤ 10_000).


Формат вывода:
Выведите два числа: K и T — максимальное количество событий материального мира,
от которых можно отказаться, и минимальное количество дней, за которые это можно
сделать. В случае K = 0 выводите T = 0.

В следующих K строках выведите названия этих событий в алфавитном порядке.


Пример
input: 5 3
input: Cappuccino 25
input: Car 5
input: Food 4
input: Apartment 1
input: Shopping 7
output: 4 9
output: Apartment
output: Car
output: Food
output: Shopping


Примечания:
Вася может отказываться от материального по следующему плану (номер дня —
названия оставшихся событий материального мира — суммарная материальность):
0 — Cappuccino (25), Car (5), Food (4), Apartment (1), Shopping (7) — 42
1 — Cappuccino (25), Car (5), Food (4), Shopping (7) — 41
2 — Cappuccino (25), Car (5), Apartment (1), Shopping (7) — 38
3 — Cappuccino (25), Food (4), Apartment (1), Shopping (7) — 37
4 — Cappuccino (25), Food (4), Shopping (7) — 36
5 — Cappuccino (25), Apartment (1), Shopping (7) — 33
6 — Cappuccino (25), Shopping (7) — 32
7 — Cappuccino (25), Food (4) — 29
8 — Cappuccino (25), Apartment (1) — 26
9 — Cappuccino (25) — 25
"""
class Solver:
    def __init__(
        self,
        spiritual_power: int | None = None,
        events: list[tuple[str, int]] | None = None,
        max_materiality: int | None = None,
    ) -> None:
        self.spiritual_power = spiritual_power
        self.events = events
        self.max_materiality = max_materiality

    def parse_data(self) -> None:

        n, self.spiritual_power = map(int, input().split())
        self.events = []
        self.max_materiality = 0
        for _ in range(n):
            name, materiality = input().split()
            materiality = int(materiality)
            self.events.append((name, materiality))
            self.max_materiality = max(self.max_materiality, materiality)

    def solve(self) -> None:

        self.events.sort(key=lambda e: e[1])

        options = [0] + [-1] * self.max_materiality
        rejected_names = []
        num_days = 0
        for name, materiality in self.events:
            cost = -1
            # ищем минимальный способ избавиться от предметов в
            # интервале [now - spiritual_power, now]
            for j in range(max(0, materiality - self.spiritual_power), materiality + 1):
                if options[j] != -1:
                    if cost != -1:
                        cost = min(cost, options[j])
                    else:
                        cost = options[j]

            if cost == -1:
                continue

            cost += 1  # избавимся от нашего и вернём все предметы
            num_days += cost
            rejected_names.append(name)
            for j in range(self.max_materiality - materiality, -1, -1):
                if options[j] != -1:
                    if options[j + materiality] != -1:
                        options[j + materiality] = min(
                            options[j + materiality],
                            options[j] + cost,
                        )
                    else:
                        options[j + materiality] = options[j] + cost

        self.k = len(rejected_names)
        self.t = num_days
        self.reject_event_names = set(rejected_names)

        print(len(rejected_names), num_days)
        print(*sorted(rejected_names), sep="\n")


def main() -> None:

    solver = Solver()
    solver.parse_data()
    solver.solve()


if __name__ == "__main__":
    main()
