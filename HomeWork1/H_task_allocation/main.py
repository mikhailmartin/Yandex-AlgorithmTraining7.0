import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])

    even_items = []
    odd_items = []
    for i in range(n):
        order = lines[1+i]
        even_s_count = order[::2].count("S")
        odd_s_count = order[1::2].count("S")
        if len(order) % 2 == 0:
            even_items.append((even_s_count, odd_s_count))
        else:
            odd_items.append((even_s_count, odd_s_count))

    res = 0
    if not odd_items:
        for even_s_count, odd_s_count in even_items:
            res += even_s_count
    else:
        for even_s_count, odd_s_count in even_items:
            res += max(even_s_count, odd_s_count)

        odd_items = sorted(odd_items, key=lambda x: x[1] - x[0])

        left_pointer = 0
        right_pointer = len(odd_items) - 1
        step = 0
        while left_pointer <= right_pointer:
            if step == 0:
                res += odd_items[left_pointer][0]
                left_pointer += 1
            else:
                res += odd_items[right_pointer][1]
                right_pointer -= 1
            step = 1 - step

    return res


if __name__ == "__main__":
    result = main()
    print(result)
