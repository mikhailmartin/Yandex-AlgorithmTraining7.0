"""
Очередь с защитой от ошибок

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Научитесь пользоваться стандартной структурой данных queue для целых чисел.
Напишите программу, содержащую описание очереди и моделирующую работу очереди,
реализовав все указанные здесь методы.

Программа считывает последовательность команд и в зависимости от команды
выполняет ту или иную операцию. После выполнения каждой команды программа должна
вывести одну строчку.

Возможные команды для программы:
- push n
  Добавить в очередь число n (значение n задаётся после команды). Программа
  должна вывести ok.
- pop
  Удалить из очереди первый элемент. Программа должна вывести его значение.
- front
  Программа должна вывести значение первого элемента, не удаляя его из очереди.
- size
  Программа должна вывести количество элементов в очереди.
- clear
  Программа должна очистить очередь и вывести ok.
- exit
  Программа должна вывести bye и завершить работу.

Перед исполнением операций front и pop программа должна проверять, содержится ли
в очереди хотя бы один элемент. Если во входных данных встречается операция
front или pop, и при этом очередь пуста, то программа должна вместо числового
значения вывести строку error.


Формат ввода:
Вводятся команды управления очередью, по одной на строке.


Формат вывода:
Требуется вывести протокол работы очереди, по одному сообщению на строке.


Пример 1
input: push 1
input: front
input: exit
output: ok
output: 1
output: bye

Пример 2
input: size
input: push 1
input: size
input: push 2
input: size
input: push 3
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
input: push 3
input: push 14
input: size
input: clear
input: push 1
input: front
input: push 2
input: front
input: pop
input: size
input: pop
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
output: 1
output: 1
output: 2
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
        queue = Queue()
        for command in self.data.commands:
            if command.startswith("push"):
                _, value = command.split()
                result.append(queue.push(value))
            elif command == "pop":
                result.append(queue.pop())
            elif command == "front":
                result.append(queue.front())
            elif command == "size":
                result.append(str(queue.size()))
            elif command == "clear":
                result.append(queue.clear())
            elif command == "exit":
                result.append(queue.exit())

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(result))


if __name__ == "__main__":
    main()
