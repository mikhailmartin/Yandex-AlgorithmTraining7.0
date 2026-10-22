import sys
from collections import namedtuple


Option = namedtuple("Option", ["sum_cost", "min_pressure", "last_i"])
Product = namedtuple("Product", ["number", "volume", "cost", "pressure"])


class Solver:
    def __init__(
        self,
        volume_rover: int | None = None,
        products: list[Product] | None = None,
        options_2d: list[list[Option]] | None = None,
    ) -> None:
        self.volume_rover = volume_rover
        self.products = products
        self.options_2d = options_2d

        self.numbers = None
        self.max_cost = None

    def solve(self) -> None:

        self.build_options_2d()

        last_options = self.options_2d[-1]
        self.max_cost = float("-inf")
        max_cost_volume_in = None
        max_cost_last_i = None
        for volume_in, option in enumerate(last_options):
            if option.sum_cost > self.max_cost:
                self.max_cost = option.sum_cost
                max_cost_volume_in = volume_in
                max_cost_last_i = option.last_i

        i = max_cost_last_i
        volume = max_cost_volume_in
        self.numbers = []
        while i != 0:
            number = self.products[i-1].number
            self.numbers.append(number)

            options = self.options_2d[i-1]
            volume -= self.products[i-1].volume
            i = options[volume].last_i

        print(len(self.numbers), self.max_cost)
        print(*self.numbers)

    def parse_data(self) -> None:

        n, self.volume_rover = map(int, input().split())
        self.products = []
        for number in range(1, n+1):
            volume, cost, pressure = map(int, input().split())
            product = Product(number, volume, cost, pressure)
            self.products.append(product)

    def build_options_2d(self) -> None:

        self.products = sorted(self.products, key=lambda p: p.pressure, reverse=True)
        max_pressure = self.products[0].pressure
        max_volume = min(
            sum([p.volume for p in self.products]),
            self.volume_rover + max_pressure,
        )

        options = [Option(0, max_pressure+1, 0)] + [Option(-1, -1, -1)] * max_volume
        self.options_2d = [options]
        for i, product in enumerate(self.products, 1):
            options = self.options_2d[-1].copy()
            for volume_curr in reversed(range(max_volume+1)):
                option_curr = options[volume_curr]
                volume_added = volume_curr + product.volume
                min_pressure_added = min(option_curr.min_pressure, product.pressure)
                if (
                    option_curr.sum_cost != -1
                    and volume_added - self.volume_rover <= min_pressure_added
                    and options[volume_added].sum_cost < option_curr.sum_cost + product.cost
                ):
                    options[volume_added] = Option(
                        option_curr.sum_cost+product.cost, min_pressure_added, i
                    )
            self.options_2d.append(options)


def main() -> None:

    solver = Solver()
    solver.parse_data()
    solver.solve()


if __name__ == "__main__":
    main()
