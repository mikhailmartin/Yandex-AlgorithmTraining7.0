import sys
from collections import namedtuple


Item = namedtuple("Item", ["weight", "cost"])
Option = namedtuple("Option", ["sum_cost", "last_index"])


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    weights = list(map(int, lines[1].split()))
    costs = list(map(int, lines[2].split()))

    items = [Item(weight, cost) for weight, cost in zip(weights, costs)]

    options_2d = get_options_2d(m, items)

    options = options_2d[-1]
    max_cost = float("-inf")
    max_cost_weight_in = None
    max_cost_i = None
    for weight_in, (cost, i) in enumerate(options):
        if cost > max_cost:
            max_cost = cost
            max_cost_weight_in = weight_in
            max_cost_i = i

    j = max_cost_i
    weight = max_cost_weight_in
    res = []
    while j != 0:
        res.append(j)
        options = options_2d[j-1]
        weight -= items[j-1][0]
        _, j = options[weight]

    return res


def get_options_2d(m: int, items: list[Item]) -> list[list[Option]]:

    options_2d = [[Option(0, 0)] + [Option(-1, -1)] * m]
    for i, item in enumerate(items, 1):
        options = options_2d[-1].copy()
        for weight_in in reversed(range(m - item.weight + 1)):
            option_curr = options[weight_in]
            weight_in_added = weight_in + item.weight
            option_added = options[weight_in_added]
            if (
                option_curr.sum_cost != -1
                and option_added.sum_cost < option_curr.sum_cost + item.cost
            ):
                options[weight_in_added] = Option(option_curr.sum_cost + item.cost, i)
        options_2d.append(options)

    return options_2d


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
