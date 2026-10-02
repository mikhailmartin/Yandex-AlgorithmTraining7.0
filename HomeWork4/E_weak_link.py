"""
Слабое звено

Ограничение времени - 2 секунды
Ограничение памяти - 512Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

В Берляндии по воскресеньям проходит известное шоу — игра «Слабое звено».

В игре принимают участие n игроков, которые выстраиваются в круг. Каждому игроку
сопоставлен рейтинг — некоторое целое число a_i.

Игра проходит в несколько раундов, каждый из которых выглядит следующим образом:
- В очередном раунде принимают участие все ещё не выбывшие игроки.
- Все игроки, которые по рейтингу строго слабее обоих своих соседей по кругу,
  объявляются слабым звеном и выбывают из игры.
- Все оставшиеся участники сдвигаются чуть плотнее, чтобы снова образовывать
  круг.
- Игра заканчивается, если после очередного раунда осталось ровно два человека
  или если после очередного раунда не выбыл ни один человек.
- Иначе начинается новый раунд.

Можно показать, что если до очередного раунда в игре оставалось хотя бы три
участника, то после одного раунда гарантированно останется не менее двух
участников.

Вам нужно выяснить для каждого участника, останется ли он до конца, или номер
раунда, в котором он покинет игру.


Формат ввода:
В первой строке дано одно целое число n (2 ≤ n ≤ 200_000) — количество
участников в игре.

Вторая строка содержит n целых чисел a_i (1 ≤ a_i ≤ 200_000) — рейтинги всех
участников игры в том порядке, в котором они стоят, при этом участник с номером
n является соседом участника с номером 1.


Формат вывода:
Выведите n целых чисел — номер раунда, в котором участник игры с номером i
покинет игру, или 0, если этот игрок останется до конца игры.

Раунды нумеруются последовательными целыми числами, начиная с 1.


Пример 1
input: 5
input: 4 5 5 2 3
output: 3 0 0 1 2

Пример 2
input: 5
input: 5 1 3 1 5
output: 0 1 2 1 0

Пример 3
input: 3
input: 6 6 6
output: 0 0 0

Пример 4
input: 4
input: 6 5 5 6
output: 0 0 0 0


Примечания:
В первом примере игра проходит следующим образом (при помощи _ обозначаются
выбывшие участники):
[4;5;5;2;3] → [4;5;5;_;3] → [4;5;5;_;_] → [_;5;5;_;_]
После этого игра заканчивается, так как осталось ровно два человека.

Во втором примере игра проходит следующим образом:
[5;1;3;1;5] → [5;_;3;_;5] → [5;_;_;_;5]

В третьем и четвертом примере нет ни одного игрока, который был бы одновременно
слабее обоих своих соседей, поэтому игра заканчивается, не успев начаться.
"""
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


@dataclass
class ProblemInput:
    n: int
    ratings: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(sys.stdin.readline().strip())
        ratings = list(map(int, sys.stdin.readline().strip().split()))
        return cls(ProblemInput(n, ratings))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        ratings = list(map(int, lines[1].split()))
        return cls(ProblemInput(n, ratings))

    def solve(self) -> list[int]:

        result = [0] * self.data.n

        chain = Chain()
        for i, rating in enumerate(self.data.ratings):
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
                result[node.idx] = round_count
                chain.remove(node)
            candidates = next_candidates
            round_count += 1

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
