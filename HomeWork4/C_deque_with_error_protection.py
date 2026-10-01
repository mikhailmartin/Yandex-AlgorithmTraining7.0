"""
Дек с защитой от ошибок

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Научитесь пользоваться стандартной структурой данных deque для целых чисел.
Напишите программу, содержащую описание дека и моделирующую работу дека,
реализовав все указанные здесь методы. Программа считывает последовательность
команд и в зависимости от команды выполняет ту или иную операцию. После
выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:
- push_front n
  Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.
- push_back n
  Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.
- pop_front
  Извлечь из дека первый элемент. Программа должна вывести его значение.
- pop_back
  Извлечь из дека последний элемент. Программа должна вывести его значение.
- front
  Узнать значение первого элемента (не удаляя его). Программа должна вывести его
  значение.
- back
  Узнать значение последнего элемента (не удаляя его). Программа должна вывести
  его значение.
- size
  Вывести количество элементов в деке.
- clear
  Очистить дек (удалить из него все элементы) и вывести ok.
- exit
  Программа должна вывести bye и завершить работу.

Гарантируется, что количество элементов в деке в любой момент не превосходит 100.
Перед исполнением операций pop_front, pop_back, front, back программа должна
проверять, содержится ли в деке хотя бы один элемент. Если во входных данных
встречается операция pop_front, pop_back, front, back, и при этом дек пуст, то
программа должна вместо числового значения вывести строку error.


Формат ввода:
Вводятся команды управления деком, по одной на строке.


Формат вывода:
Требуется вывести протокол работы дека, по одному сообщению на строке


Пример 1
input: push_back 1
input: back
input: exit
output: ok
output: 1
output: bye

Пример 2
input: size
input: push_back 1
input: size
input: push_back 2
input: size
input: push_front 3
input: size
input: exit
output: 0
output: ok
output: 1
output: ok
output: 2
output: ok
output: 3
output: bye

Пример 3
input: push_back 3
input: push_front 14
input: size
input: clear
input: push_front 1
input: back
input: push_back 2
input: front
input: pop_back
input: size
input: pop_front
input: size
input: exit
output: ok
output: ok
output: 2
output: ok
output: ok
output: 1
output: ok
output: 1
output: 2
output: 1
output: 1
output: 0
output: bye
"""
import sys
from dataclasses import dataclass
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

@dataclass
class ProblemInput:
    commands: list[str]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        commands = []
        while True:
            command = sys.stdin.readline().strip()
            commands.append(command)
            if command == "exit":
                break
        return cls(ProblemInput(commands))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        commands = []
        i = 0
        while True:
            command = lines[i]
            commands.append(command)
            if command == "exit":
                break
            i += 1
        return cls(ProblemInput(commands))

    def solve(self) -> list[str]:

        result = []
        deque = Deque()
        for command in self.data.commands:
            if command.startswith("push"):
                command, value = command.split()
                if command == "push_front":
                    result.append(deque.push_front(value))
                elif command == "push_back":
                    result.append(deque.push_back(value))
            elif command == "pop_front":
                result.append(deque.pop_front())
            elif command == "pop_back":
                result.append(deque.pop_back())
            elif command == "front":
                result.append(deque.front())
            elif command == "back":
                result.append(deque.back())
            elif command == "size":
                result.append(str(deque.size()))
            elif command == "clear":
                result.append(deque.clear())
            elif command == "exit":
                result.append(deque.exit())

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(result))


if __name__ == "__main__":
    main()
