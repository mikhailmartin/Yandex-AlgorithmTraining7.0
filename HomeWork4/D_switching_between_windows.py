"""
Переключение между окнами

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Когда пользователь работает в операционной системе Windows, у него часто
запущено несколько приложений. Каждое из приложений работает в отдельном окне.
Для переключения между окнами используется комбинация клавиш "Alt+Tab". Эта
комбинация делает активным окно, в котором пользователь работал перед тем, как
перейти в текущее активное окно.

Чтобы переключиться в другое окно, можно нажать клавишу "Alt" и затем, не
отпуская её, несколько раз нажать клавишу "Tab". Чтобы понять, какое окно станет
активным после этого, воспользуемся следующей моделью. Пусть запущено
n приложений. Приложения в операционной системе организованы в виде списка и
упорядочены по убыванию времени последней активности. То есть приложение, окно
которого является активным в настоящий момент, — первое в списке, приложение,
окно которого было активно перед этим, — второе, и т.д.

Если нажать клавишу "Alt" и затем, не отпуская её, нажать клавишу "Tab" k раз,
то активным станет окно приложения, которое находится на (k % n) + 1-м месте в
списке. Здесь a % b означает остаток от деления a на b. Иными словами,
операционная система рассматривает список как циклический, переходя после
последнего элемента списка к первому.

При запуске нового приложения оно добавляется в начало списка.

Задана последовательность действий пользователя, где каждое действие — либо
запуск приложения, либо переключение между окнами. Выведите список имён
приложений в том порядке, в котором с ними работал пользователь.


Формат ввода:
В первой строке вводится целое число n — количество действий пользователя
(1 ≤ n ≤ 1000). Следующие n строк содержат описание действий пользователя.

Запуск приложения описывается строкой "Run <имя приложения>". Здесь
"<имя приложения>" — строка из не более чем 100 латинских букв, цифр и пробелов.
Она отделена от слова "Run" ровно одним пробелом. Все имена приложений различны.
Большие и маленькие буквы считаются различными.

Переключение между приложениями описывается строкой "Alt+Tab+...+Tab", здесь
подстрока "+Tab" повторена в точности столько раз, сколько раз пользователь
нажал клавишу "Tab", не отпуская клавишу "Alt". Это количество не превышает 100.

Первая команда во входных данных — всегда команда "Run".


Формат вывода:
Выведите n строк — последовательность имён приложений, с которыми работал
пользователь в порядке, в котором их окна становились активными.


Пример
input: 6
input: Run Mozilla Firefox
input: Run Free Pascal
input: Alt+Tab
input: Run Miranda IM
input: Alt+Tab+Tab
input: Alt+Tab+Tab+Tab
output: Mozilla Firefox
output: Free Pascal
output: Mozilla Firefox
output: Miranda IM
output: Free Pascal
output: Free Pascal
"""
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


@dataclass
class ProblemInput:
    n: int
    commands: list[str]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(sys.stdin.readline().strip())
        commands = []
        for _ in range(n):
            command = sys.stdin.readline().strip()
            commands.append(command)
        return cls(ProblemInput(n, commands))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        commands = []
        for i in range(n):
            command = lines[1+i]
            commands.append(command)
        return cls(ProblemInput(n, commands))

    def solve(self) -> list[str]:

        result = []
        queue = Queue()

        for command in self.data.commands:
            if command.startswith("Run"):
                command, _, app_name = command.partition(" ")
                queue.push_front(app_name)
            elif command.startswith("Alt"):
                m = command.count("+Tab")
                queue.tab(m)
            result.append(queue.front())

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(result))


if __name__ == "__main__":
    main()
