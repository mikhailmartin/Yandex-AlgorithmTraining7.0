import sys


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    bridges = []
    for i in range(m):
        x, y = map(int, lines[i + 1].split())
        bridges.append((x, y))

    union_find = UnionFind(n)
    for count, (x, y) in enumerate(bridges, 1):
        union_find.union(x - 1, y - 1)
        if union_find.components == 1:
            return count


if __name__ == "__main__":
    result = main()
    print(result)
