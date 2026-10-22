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
            return True
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    n, m, k = map(int, lines[0].split())
    edges = []
    for i in range(m):
        u, v = map(int, lines[i + 1].split())
        edges.append((u, v))
    operations = []
    for j in range(k):
        operations.append(lines[1 + m + j].strip())

    union_find = UnionFind(n)

    res = []
    for operation in reversed(operations):
        operation, u, v = operation.split()
        u = int(u)
        v = int(v)
        if operation == "cut":
            union_find.union(u - 1, v - 1)
        elif operation == "ask":
            if union_find.connected(u - 1, v - 1):
                res.append("YES")
            else:
                res.append("NO")

    return list(reversed(res))


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
