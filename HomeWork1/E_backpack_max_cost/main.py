import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    weights = list(map(int, lines[1].split()))
    costs = list(map(int, lines[2].split()))

    items = list(zip(weights, costs))

    options = {0: 0}
    for weight_by_item, cost_by_item in items:
        buffer = []
        for weight_in, cost_in in options.items():
            remaining = m - weight_in
            if remaining >= weight_by_item:
                buffer.append((weight_in + weight_by_item, cost_in + cost_by_item))

        for weight_in, cost_in in buffer:
            if options.get(weight_in, float("-inf")) < cost_in:
                options[weight_in] = cost_in

    return max(options.values())


if __name__ == "__main__":
    result = main()
    print(result)
