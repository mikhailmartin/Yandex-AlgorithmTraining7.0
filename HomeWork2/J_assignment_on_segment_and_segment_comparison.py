"""
Присваивание на отрезке, сравнение подотрезков*

Ограничение времени - 12.001 секунда
Ограничение памяти - 1024Mb
Ввод - стандартный ввод
Вывод - стандартный вывод

Реализуйте структуру данных, которая позволяет выполнять две операции:
- Присвоить всем элементам на отрезке от L до R значение K;
- Поэлементно сравнить все числа на отрезках длины K, начинающихся с позиций L и R.


Формат ввода:
В первой строке записано число N (1 ≤ N ≤ 100_000) — количество элементов
в последовательности.

Во второй строке записано N целых чисел — начальные значения последовательности,
все числа имеют значения от 1 до 100_000.

В третьей строке записано число Q (1 ≤ Q ≤ 100_000) — количество операций
сравнения и присваивания.

Следующие Q строк содержат описания операций: четыре числа T, L, R и K.

Если T = 0, то необходимо всем числам с индексами с L до R включительно присвоить
значение K (1 ≤ L ≤ R ≤ N, 1 ≤ K ≤ 100_000).

Если T = 1, то необходимо сравнить подотрезки, начинающиеся с позиций L и R и
имеющие длину K (1 ≤ L, R ≤ N − K + 1, K > 0).


Формат вывода:
Для каждого запроса сравнения подстрок выведите ’+’, если подотрезки совпадают
и ’-’ в противном случае в одну строку без пробелов.


Пример
input: 5
input: 1 2 1 2 1
input: 4
input: 1 2 4 2
input: 0 3 5 2
input: 1 1 3 2
input: 1 2 3 3
output: +-+
"""
class Solver:
    def __init__(
        self,
        array: list[int] | None = None,
        queries: list[tuple[int, int, int, int]] | None = None,
    ) -> None:
        self.array = array
        self.queries = queries or []

    def parse_data(self) -> None:

        n = int(input())
        self.array = list(map(int, input().split()))
        q = int(input())
        for _ in range(q):
            t, l, r, k = map(int, input().split())
            self.queries.append((t, l, r, k))

    def solve(self) -> None:

        answer = []
        for t, l, r, k in self.queries:
            match t:
                case 0:
                    self.update(l, r, k)
                case 1:
                    result = "+" if self.compare(l, r, k) else "-"
                    answer.append(result)
                case _:
                    raise ValueError
        print("".join(answer))

    def update(self, l: int, r: int, k: int) -> None:
        ...

    def compare(self, l: int, r: int, k: int) -> bool:
        ...


def main() -> None:

    solver = Solver()


if __name__ == "__main__":
    main()
