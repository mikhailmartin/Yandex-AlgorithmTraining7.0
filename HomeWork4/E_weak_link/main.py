import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ListNode:
    idx: int
    rating: int
    next: Self | None = None
    prev: Self | None = None
    is_removed: bool = False


class Chain:
    head: ListNode | None = None
    tail: ListNode | None = None
    size: int = 0

    def add(self, idx: int, value: int) -> None:
        node = ListNode(idx, value)

        if self.size == 0:
            self.head = node
            self.tail = node

            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.head.prev = node
            self.tail.next = node

            node.prev = self.tail
            node.next = self.head

            self.tail = node

        self.size += 1

    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    ratings = list(map(int, lines[1].split()))

    res = [0] * n

    chain = Chain()
    for i, rating in enumerate(ratings):
        chain.add(i, rating)

    candidates = []
    node = chain.head
    for _ in range(chain.size):
        candidates.append(node)
        node = node.next

    round_count = 1
    while chain.size > 2:
        removed = []
        next_candidates = []
        for node in candidates:
            if node.is_removed:
                continue
            if node.rating < node.prev.rating and node.rating < node.next.rating:
                node.is_removed = True
                removed.append(node)
                next_candidates.append(node.prev)
                next_candidates.append(node.next)

        if not removed:
            break
        for node in removed:
            res[node.idx] = round_count
            chain.remove(node)
        candidates = next_candidates
        round_count += 1

    return res


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
