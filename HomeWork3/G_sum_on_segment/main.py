import sys


class BinaryIndexedTree1D:
    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        self.tree: list[int] = [0] * n
        for x in range(n):
            end = x
            start = x & (x + 1)
            self.tree[x] = sum(arr[start:end+1])

    def add(self, x: int, value: int) -> None:
        while x < len(self.tree):
            self.tree[x] += value
            x = x | (x + 1)

    def update(self, x: int, value: int) -> None:
        diff = value - self.get(x, x)
        self.add(x, diff)

    def get(self, start: int, end: int) -> int:
        return self._get(end) - self._get(start-1)

    def _get(self, x: int) -> int:
        res = 0
        while x >= 0:
            res += self.tree[x]
            x = (x & (x + 1)) - 1
        return res


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    res = []
    bit = BinaryIndexedTree1D([0] * n)
    for i in range(k):
        query_type, i, x = lines[i+1].split()
        i = int(i)
        x = int(x)
        if query_type == "A":
            bit.update(i - 1, x)
        elif query_type == "Q":
            l, r = i, x
            answer = bit.get(l - 1, r - 1)
            res.append(answer)

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
