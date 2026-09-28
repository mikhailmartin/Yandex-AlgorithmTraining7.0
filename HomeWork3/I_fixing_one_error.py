"""
Исправление одной ошибки

Ограничение времени - 1 секунда
Ограничение памяти - 512Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Это задача с двойным запуском.

Ваше решение будет запущено два раза.

При первом запуске ему на вход будет передана строка x из нулей и единиц длиной
не больше n. Программа должна вывести строку y из нулей и единиц, длина которой
не более чем m. Число m не известно вашей программе и зависит от подзадачи,
соответствующее значение указано в таблице системы оценивания. Если ваша
программа выведет строку длиннее, чем m, она получит вердикт «Wrong answer».

Между запусками решения программа жюри внесёт в строку y не более одной
модификации, заменив ноль на единицу или единицу на ноль, получив таким образом,
строку z.

При втором запуске программе на вход будет подана строка z. Она должна
восстановить исходную строку x и выдать её на выход.


Формат ввода:
При первом запуске на первой строке ввода находится число 1. На второй строке
ввода находится строка x из нулей и единиц длины n (10 ≤ n ≤ 100_000).

При втором запуске на первой строке ввода находится число 2. На второй строке
ввода находится строка z из нулей и единиц длины не больше m (10 ≤ m ≤ 100_017).
Гарантируется, что эта строка равна строке y, выведенной программой при первом
запуске, или получена из неё изменением ровно одного символа на противоположный.


Формат вывода:
При первом запуске необходимо вывести строку y, которая позволит восстановить x
после внесения в неё изменения. Длина строки y не должна превышать m, m не
должно превосходить n более чем на log_2(n) округленный вверх.

При втором запуске по заданной строке z необходимо восстановить исходную строку
x и вывести её.


Примечания:
Пусть ввод для первого запуска выглядит так:
1
01010
Допустим, ваша программы вывела в качестве ответа:
000111000111000
В этот ответ вносится одно изменение и подается на вход вашей программе,
например, ввод для второго запуска может выглядеть так:
2
000101000111000
Ваша программа должна вывести
01010
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    num: str
    x: str


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        num = input().strip()
        x = input().strip()
        return cls(ProblemInput(num, x))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        num = lines[0].strip()
        x = lines[1].strip()
        return cls(ProblemInput(num, x))

    def solve(self) -> str:

        if self.data.num == "1":
            return self.encode(self.data.x)
        else:
            return self.decode(self.data.x)

    @staticmethod
    def encode(x: str) -> str:

        n = len(x)

        parity_bit_count = 0
        while (1 << parity_bit_count) < n + parity_bit_count + 1:
            parity_bit_count += 1

        m = n + parity_bit_count
        result = [0] * m

        # расставляем информационные биты
        x_idx = 0
        for pos in range(1, m + 1):
            if (pos & (pos - 1)) == 0:
                continue
            result[pos-1] = 1 if x[x_idx] == "1" else 0
            x_idx += 1

        # расставляем контрольные биты
        for k in range(parity_bit_count):
            p = 1 << k
            parity = 0
            step = p << 1
            for start in range(p, m + 1, step):
                end = min(start + p, m + 1)
                for pos in range(start, end):
                    parity ^= result[pos-1]
            result[p-1] = parity

        return "".join("1" if bit else "0" for bit in result)


    @staticmethod
    def decode(z: str) -> str:

        m = len(z)

        r = 0
        while (1 << r) < m + 1:
            r += 1

        bits = [1 if char == "1" else 0 for char in z]

        # Ищем позицию ошибки
        error_pos = 0
        for k in range(r):
            p = 1 << k
            parity = 0
            step = p << 1
            for start in range(p, m + 1, step):
                end = min(start + p, m + 1)
                for pos in range(start, end):
                    parity ^= bits[pos-1]
            if parity != 0:
                error_pos += p

        if error_pos > 0:
            bits[error_pos - 1] ^= 1

        result = []
        for pos in range(1, m + 1):
            if (pos & (pos - 1)) != 0:
                result.append("1" if bits[pos - 1] else "0")

        return "".join(result)


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
