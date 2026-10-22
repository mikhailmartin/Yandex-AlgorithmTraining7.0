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


class Stack:
    def __init__(self) -> None:
        self.tail = None
        self.size_ = 0

    def push(self, value: str) -> str:
        node = ListNode(value)
        if self.size_ == 0:
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
        res = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size_ -= 1
        return res

    def back(self) -> str:
        if self.size_ == 0:
            return "error"
        return self.tail.value

    def size(self) -> int:
        return self.size_

    def clear(self) -> str:
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
    stack = Stack()
    while True:
        command = lines[i]
        if command == "exit":
            res.append(stack.exit())
            break
        elif command.startswith("push"):
            _, value = command.split()
            res.append(stack.push(value))
        elif command == "pop":
            res.append(stack.pop())
        elif command == "back":
            res.append(stack.back())
        elif command == "size":
            res.append(str(stack.size()))
        elif command == "clear":
            res.append(stack.clear())
        i += 1

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
