"""
Эластичный ровер*

Ограничение времени - 3 секунды
Ограничение памяти - 512Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Один из главных недостатков ровера-доставщика — ограниченный по объёму отсек,
в котором иногда чуть-чуть не хватает места. Экспериментальная модель ровера
обладает эластичным отсеком для перевозки заказов.

Базовый объём отсека составляет S литров. Пока отсек не заполнен, товары в нём
не испытывают дополнительного давления. Однако, поскольку отсек эластичный,
в него можно положить дополнительные товары сверх базового объёма. Если объём
положенных в отсек товаров U превышает S, то все товары в отсеке будут
испытывать давление P = U − S.

Каждый товар обладает тремя характеристиками: объёмом v_i, стоимостью c_i и
давлением, которое он выдерживает p_i.

Всего необходимо доставить N товаров, однако в первую поездку ровера необходимо
отправить товары с максимальной суммарной стоимостью — это обрадует заказчика.
Определите максимальную стоимость товаров, которые можно разместить в ровере
так, чтобы все они выдерживали давление.


Формат ввода:
В первой строке находятся два целых числа N (1 ≤ N ≤ 100) и S (0 ≤ S ≤ 10^9) —
количество товаров.

Следующие N строк содержат описание очередного товара v_i, c_i и p_i
(1 ≤ v_i ≤ 1000, 0 ≤ c_i ≤ 10^6, 0 ≤ p_i ≤ 10^9) — объём и стоимость товара,
а также максимальное давление, которое он выдерживает.


Формат вывода:
В первой строке выведите число товаров K, которые необходимо разместить в отсеке
ровера, и их максимальную суммарную стоимость.

Во второй строке выведите K чисел — номера товаров, которые нужно разместить в
отсеке ровера. Товары нумеруются с единицы в том порядке, в котором они даны во
входном файле.

Если существует несколько вариантов ответа, выведите любой из них.


Пример 1
input: 3 7
input: 4 1 2
input: 3 1 2
input: 2 1 2
output: 3 3
output: 1 2 3

Пример 2
input: 3 7
input: 4 1 3
input: 3 1 2
input: 2 1 1
output: 2 2
output: 2 3
"""
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
