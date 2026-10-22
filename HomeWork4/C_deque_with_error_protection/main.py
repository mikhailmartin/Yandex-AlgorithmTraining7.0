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


class Deque:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size_ = 0

    def push_front(self, value: str) -> str:
        node = ListNode(value)
        if self.size_ == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size_ += 1
        return "ok"

    def push_back(self, value: str) -> str:
        node = ListNode(value)
        if self.size_ == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size_ += 1
        return "ok"

    def pop_front(self) -> str:
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

    def pop_back(self) -> str:
        if self.size_ == 0:
            return "error"
        result = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size_ -= 1
        return result

    def front(self) -> str:
        if self.size_ == 0:
            return "error"
        return self.head.value

    def back(self) -> str:
        if self.size_ == 0:
            return "error"
        return self.tail.value

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
    deque = Deque()
    while True:
        command = lines[i]
        if command == "exit":
            res.append(deque.exit())
            break
        elif command.startswith("push"):
            command, value = command.split()
            if command == "push_front":
                res.append(deque.push_front(value))
            elif command == "push_back":
                res.append(deque.push_back(value))
        elif command == "pop_front":
            res.append(deque.pop_front())
        elif command == "pop_back":
            res.append(deque.pop_back())
        elif command == "front":
            res.append(deque.front())
        elif command == "back":
            res.append(deque.back())
        elif command == "size":
            res.append(str(deque.size()))
        elif command == "clear":
            res.append(deque.clear())
        i += 1

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
