"""
Стек с защитой от ошибок

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Научитесь пользоваться стандартной структурой данных stack для целых чисел.
Напишите программу, содержащую описание стека и моделирующую работу стека,
реализовав все указанные здесь методы. Программа считывает последовательность
команд и в зависимости от команды выполняет ту или иную операцию. После
выполнения каждой команды программа должна вывести одну строчку. Возможные
команды для программы:
- push n
  Добавить в стек число n (значение n задаётся после команды). Программа должна
  вывести ok.
- pop
  Удалить из стека последний элемент. Программа должна вывести его значение.
- back
  Программа должна вывести значение последнего элемента, не удаляя его из стека.
- size
  Программа должна вывести количество элементов в стеке.
- clear
  Программа должна очистить стек и вывести ok.
- exit
  Программа должна вывести bye и завершить работу.

Перед исполнением операций back и pop программа должна проверять, содержится ли
в стеке хотя бы один элемент. Если во входных данных встречается операция back
или pop, и при этом стек пуст, то программа должна вместо числового значения
вывести строку error.


Формат ввода:
Вводятся команды управления стеком, по одной на строке.


Формат вывода:
Программа должна вывести протокол работы стека, по одному сообщению на строке.


Пример 1
input: push 1
input: back
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
input: back
input: push 2
input: back
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
output: 2
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
        result = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size_ -= 1
        return result

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
        stack = Stack()
        for command in self.data.commands:
            if command.startswith("push"):
                _, value = command.split()
                result.append(stack.push(value))
            elif command == "pop":
                result.append(stack.pop())
            elif command == "back":
                result.append(stack.back())
            elif command == "size":
                result.append(str(stack.size()))
            elif command == "clear":
                result.append(stack.clear())
            elif command == "exit":
                result.append(stack.exit())

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(result))


if __name__ == "__main__":
    main()
