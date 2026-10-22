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
