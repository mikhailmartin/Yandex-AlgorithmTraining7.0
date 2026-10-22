import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])

    max_n = n
    bit_length = n.bit_length()
    for _ in range(bit_length):
        carry = n & 1
        n >>= 1
        n |= carry << (bit_length - 1)
        max_n = max(max_n, n)

    return max_n


if __name__ == "__main__":
    result = main()
    print(result)
