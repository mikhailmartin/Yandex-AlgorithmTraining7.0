import sys


class PersistentStack:
    def __init__(self) -> None:
        self.versions = [(-1, 0)]

    def push(self, value: int, version: int) -> None:
        _, prev_value  = self.versions[version]
        self.versions.append((version, prev_value + value))

    def pop(self, version: int) -> None:
        prev_version, _ = self.versions[version]
        self.versions.append(self.versions[prev_version])


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0].strip())
    actions = []
    for i in range(n):
        t, m = map(int, lines[i+1].split())
        actions.append((t, m))

    persistent_stack = PersistentStack()
    for t, m in actions:
        if m == 0:
            persistent_stack.pop(t)
        else:
            persistent_stack.push(m, t)

    return sum(node[1] for node in persistent_stack.versions)


if __name__ == "__main__":
    result = main()
    print(result)
