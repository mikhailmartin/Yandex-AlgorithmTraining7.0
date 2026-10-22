import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ListNode:
    value: str
    next: Self | None = None
    prev: Self | None = None


@dataclass
class Queue:
    head: ListNode | None = None
    size: int = 0

    def push_front(self, value: str) -> None:
        node = ListNode(value)
        if self.size > 0:
            node.next = self.head
            self.head.prev = node
        self.head = node
        self.size += 1

    def front(self) -> str:
        return self.head.value

    def tab(self, m: int) -> None:
        m %= self.size
        if m > 0:
            node = self.head
            for _ in range(m):
                node = node.next

            # remove
            if node.next:
                node.next.prev = node.prev
            node.prev.next = node.next

            # push front
            node.next = self.head
            self.head.prev = node
            self.head = node


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    queue = Queue()
    res = []
    for i in range(n):
        command = lines[1+i]
        if command.startswith("Run"):
            command, _, app_name = command.partition(" ")
            queue.push_front(app_name)
        elif command.startswith("Alt"):
            m = command.count("+Tab")
            queue.tab(m)
        res.append(queue.front())

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
