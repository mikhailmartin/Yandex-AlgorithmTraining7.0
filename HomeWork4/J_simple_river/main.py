import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ListNode:
    value: int
    next: Self | None = None
    prev: Self | None = None


class River:
    def __init__(self, lengths: list[int]) -> None:
        self.squared_sum = 0
        next = None
        while lengths:
            length = lengths.pop()
            node = ListNode(length, next=next)
            if next:
                next.prev = node
            next = node
            self.squared_sum += length * length

        self.pointer = next
        self.index = 0

    def bankruptcy(self, idx: int) -> None:
        self._move_pointer(idx)

        self.squared_sum -= self.pointer.value * self.pointer.value

        if self.pointer.prev and self.pointer.next:
            left_value, right_value = self._split_value(self.pointer.value)

            self.squared_sum -= self.pointer.prev.value * self.pointer.prev.value
            self.pointer.prev.value += left_value
            self.pointer.prev.next = self.pointer.next
            self.squared_sum += self.pointer.prev.value * self.pointer.prev.value

            self.squared_sum -= self.pointer.next.value * self.pointer.next.value
            self.pointer.next.value += right_value
            self.pointer.next.prev = self.pointer.prev
            self.squared_sum += self.pointer.next.value * self.pointer.next.value

            self.pointer = self.pointer.next

        elif self.pointer.prev:
            self.squared_sum -= self.pointer.prev.value * self.pointer.prev.value
            self.pointer.prev.value += self.pointer.value
            self.pointer.prev.next = self.pointer.next
            self.squared_sum += self.pointer.prev.value * self.pointer.prev.value

            self.pointer = self.pointer.prev
            self.index -= 1

        else:
            self.squared_sum -= self.pointer.next.value * self.pointer.next.value
            self.pointer.next.value += self.pointer.value
            self.pointer.next.prev = self.pointer.prev
            self.squared_sum += self.pointer.next.value * self.pointer.next.value

            self.pointer = self.pointer.next


    def split(self, idx: int) -> None:
        self._move_pointer(idx)

        left_value, right_value = self._split_value(self.pointer.value)

        self.squared_sum -= self.pointer.value * self.pointer.value
        self.squared_sum += left_value * left_value + right_value * right_value

        self.pointer.value = left_value

        node = ListNode(right_value, prev=self.pointer, next=self.pointer.next)
        if self.pointer.next:
            self.pointer.next.prev = node
        self.pointer.next = node

    def _move_pointer(self, idx: int) -> None:
        while idx != self.index:
            if idx > self.index:
                self.index += 1
                self.pointer = self.pointer.next
            else:
                self.index -= 1
                self.pointer = self.pointer.prev

    @staticmethod
    def _split_value(value: int) -> tuple[int, int]:
        left_value = right_value = value // 2
        right_value += value % 2
        return left_value, right_value


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    lengths = list(map(int, lines[1].split()))

    k = int(lines[2])
    events = []
    for j in range(k):
        e, v = map(int, lines[j+3].split())
        events.append((e, v))

    river = River(lengths)

    res = [river.squared_sum]
    for e, v in events:
        if e == 1:
            river.bankruptcy(v - 1)
        else:
            river.split(v - 1)
        res.append(river.squared_sum)

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
