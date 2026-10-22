import sys


def main(lines: list[str] | None = None):

    lines = lines or sys.stdin.read().splitlines()

    t = int(lines[0])
    for i in range(t):
        n = int(lines[1+2*i])
        test_sample = list(map(int, lines[1+2*i+1].split()))
        k, len_k = solve(test_sample)
        print(k)
        print(*len_k)


def solve(test_sample: list[int]) -> tuple[int, list[int]]:

    counter = 0
    lengths = []

    length = 0
    min_number = float("+inf")
    for number in test_sample:

        if number > length and min_number > length:
            length += 1
            min_number = min(min_number, number)
        else:
            counter += 1
            lengths.append(length)
            length = 1
            min_number = number

    if length > 0:
        counter += 1
        lengths.append(length)

    return counter, lengths


if __name__ == "__main__":
    main()
