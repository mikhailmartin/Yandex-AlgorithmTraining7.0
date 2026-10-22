import sys
from typing import Self


class ListNode:
    def __init__(
        self,
        value: str,
        next: Self | None = None,
        prev: Self | None = None,
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size_ = 0

    def push(self, value: str) -> str:
        node = ListNode(value)
        if self.size_ == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size_ += 1
        return "ok"

    def pop(self) -> str:
        if self.size_ == 0:
            return "error"
        result = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size_ -= 1
        return result

    def front(self) -> str:
        if self.size_ == 0:
            return "error"
        return self.head.value

    def size(self) -> int:
        return self.size_

    def clear(self) -> str:
        self.head = None
        self.tail = None
        self.size_ = 0
        return "ok"

    @staticmethod
    def exit() -> str:
        return "bye"


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    res = []
    i = 0
    queue = Queue()
    while True:
        command = lines[i]
        if command == "exit":
            res.append(queue.exit())
            break
        elif command.startswith("push"):
            _, value = command.split()
            res.append(queue.push(value))
        elif command == "pop":
            res.append(queue.pop())
        elif command == "front":
            res.append(queue.front())
        elif command == "size":
            res.append(str(queue.size()))
        elif command == "clear":
            res.append(queue.clear())
        i += 1

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
