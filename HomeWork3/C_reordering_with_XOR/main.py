import sys
import bisect


def main(lines: list[str] | None = None) -> tuple[bool, list[int]]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))

    L = max(num.bit_length() for num in nums)
    counts = [num.bit_count() for num in nums]
    total = sum(counts)

    if total & 1:
        return False, []

    max_pairs_per_column = n // 2
    pairs = total // 2

    if pairs > L * max_pairs_per_column:
        return False, []

    base, rem = divmod(pairs, L)
    columns = [2 * (base + 1)] * rem + [2 * base] * (L - rem)

    counter = []
    for i, count in enumerate(counts):
        if count > 0:
            bisect.insort(counter, (count, i))

    answer = [0] * n

    for bit_pos, column_size in enumerate(columns):
        if column_size == 0:
            continue

        if len(counter) < column_size:
            return False, []

        taken = []

        for _ in range(column_size):
            count, idx = counter.pop()

            if count <= 0:
                return False, []

            answer[idx] |= 1 << bit_pos
            taken.append((count - 1, idx))

        for count, idx in taken:
            if count > 0:
                bisect.insort(counter, (count, idx))

    if counter:
        return False, []

    return True, answer


if __name__ == "__main__":
    result = main()
    if not result[0]:
        print("impossible")
    else:
        print(*result[1])
