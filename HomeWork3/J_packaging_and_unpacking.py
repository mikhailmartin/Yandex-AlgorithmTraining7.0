"""
Упаковка и распаковка

Ограничение времени - 2 секунды
Ограничение памяти - 1024Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Это задача с двойным запуском.

Ваше решение будет запущено два раза.

Вам необходимо реализовать алгоритм сжатия и распаковки, который будет сжимать
тексты на английском языке, записанные только маленькими английскими буквами,
без пробелов, знаков препинания и вообще каких-либо символов, отличных от
маленьких английских букв. Эти тексты являются художественными произведениями
(естественным текстом).

Решение будет считаться верным, если в результате упаковки и распаковки
получается исходная строка. Также необходимо, чтобы количество байт в сжатой
последовательности было как минимум вдвое меньше, чем количество символов в
исходной строке.


Протокол взаимодействия:
При первом запуске на вход программе в первой строке передается слово "pack".

Во второй строке передаётся строка s из маленьких английских букв. Длина строки
для всех тестов находится в пределах от 100_000 до 200_000 букв.

Ваше решение должно вывести количество чисел (байт) N в сжатой вами
последовательности. Во второй строке выведите N чисел от 0 до 255 включительно
в десятичной системе счисления, разделяя их пробелами. В конце обязательно
сбросьте буфер вывода и выведите перевод строки.

Количество байт не должно превышать половины от количества символов входной
строки.

При втором запуске на вход программе в первой строке передается слово "unpack".

Затем в программу передаётся вывод первого запуска: количество байт, а затем
числа от 0 до 255 через пробел — последовательность символов. Необходимо вывести
распакованную строку. В конце обязательно сбросьте буфер вывода и выведите
перевод строки.


Примечания:
Пусть ввод для первого запуска выглядит так:
pack
abacabaca
Допустим, ваша программы вывела в качестве ответа:
5
11 255 0 13 253
Добавляется слово unpack и этот ответ подаётся на вход вашей программе, ввод для
второго запуска будет выглядеть так:
unpack
5
11 255 0 13 253
Ваша программа должна вывести
abacabaca
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    command: str
    string: str


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        command = input().strip()
        if command == "pack":
            string = input().strip()
        else:
            n = input().strip()
            string = input().strip()
        return cls(ProblemInput(command, string))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        command = lines[0]
        if command == "pack":
            string = lines[1]
        else:
            n = lines[1]
            string = lines[2]
        return cls(ProblemInput(command, string))

    def solve(self) -> str:

        if self.data.command == "pack":
            return self.pack(self.data.string)
        else:
            return self.unpack(self.data.string)

    def pack(self, string: str) -> str:

        encoded = self.encode_lzw(string)
        bits = self.encoded_to_bits(encoded)
        bytes = self.bits_to_bytes(bits)
        nums = self.bytes_to_nums(bytes)

        n = len(nums)
        return f"{n}\n{' '.join(map(str, nums))}"

    @staticmethod
    def encode_lzw(string: str) -> list[int | str]:

        result = []
        vocab = {"": 0}
        count = 1
        left = 0
        for right, char in enumerate(string):
            curr_word = string[left:right + 1]
            if curr_word not in vocab:
                prev_word = string[left:right]
                result.append(vocab[prev_word])
                result.append(char)
                vocab[curr_word] = count
                count += 1
                left = right + 1

        if left != right + 1:
            word = string[left:]
            result.append(vocab[word])

        return result

    @staticmethod
    def encoded_to_bits(encoded: list[int | str]) -> str:

        bits_on_char = 5
        bits_on_num = 1
        count = 1

        result = []
        for elem in encoded:
            if isinstance(elem, int):
                num = elem
                bits = bin(num)[2:].zfill(bits_on_num)
                result.append(bits)
            else:
                char = elem
                bits = bin(ord(char) - ord("a"))[2:].zfill(bits_on_char)
                result.append(bits)

                count += 1
                while count > (1 << bits_on_num):
                    bits_on_num += 1

        return "".join(result)

    @staticmethod
    def bits_to_bytes(bits: str) -> list[str]:
        bits += "1"
        padding = (8 - len(bits) % 8) % 8
        bits += "0" * padding
        return [bits[i:i+8] for i in range(0, len(bits), 8)]

    @staticmethod
    def bytes_to_nums(bytes: list[str]) -> list[int]:
        return [int(byte, 2) for byte in bytes]

    def unpack(self, string: str) -> str:

        nums = list(map(int, string.split()))
        bytes = self.nums_to_bytes(nums)
        bits = self.bytes_to_bits(bytes)
        encoded = self.bits_to_encoded(bits)
        result = self.encoded_to_result(encoded)

        return result

    @staticmethod
    def encoded_to_result(encoded: list[int | str]) -> str:

        result = []
        vocab = {0: ""}
        count = 1
        prev = encoded[0]
        for elem in encoded:
            if isinstance(elem, int):
                num = elem
                word = vocab[num]
                result.append(word)
                prev = word
            else:
                char = elem
                result.append(char)

                vocab[count] = f"{prev}{char}"
                count += 1

        return "".join(result)

    @staticmethod
    def nums_to_bytes(nums: list[int]) -> list[str]:
        return [bin(num)[2:].zfill(8) for num in nums]

    @staticmethod
    def bytes_to_bits(bytes: list[str]) -> str:
        bits = "".join(bytes)
        last_one = bits.rfind("1")
        return bits[:last_one]

    @staticmethod
    def bits_to_encoded(bits: str) -> list[int | str]:

        n = len(bits)

        bits_on_char = 5
        bits_on_num = 1
        count = 1

        result = []
        i = 0
        while i < n:
            num = int(bits[i:i + bits_on_num], 2)
            result.append(num)
            i += bits_on_num

            if i >= n:  # хвостовой индекс без символа
                break

            char = chr(int(bits[i:i + bits_on_char], 2) + ord("a"))
            result.append(char)
            i += bits_on_char

            count += 1
            while count > (1 << bits_on_num):
                bits_on_num += 1

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
