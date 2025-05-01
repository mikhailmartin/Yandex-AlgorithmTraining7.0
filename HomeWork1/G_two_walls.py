"""
Две стены

Ограничение времени - 3 секунды
Ограничение памяти - 512Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

У Пети есть набор из N кирпичиков. Каждый кирпичик полностью окрашен в один из
K цветов, i-й кирпичик имеет размер 1×1×L_i. Петя знает, что он может построить
из кирпичиков прямоугольную стену толщиной 1 и высотой K, причём первый
горизонтальный слой кирпичиков в стене будет первого цвета, второй — второго и
т.д. Теперь Петя хочет узнать, может ли он из своего набора построить две
прямоугольные стены, обладающие тем же свойством. Помогите ему выяснить это.


Формат ввода:
В первой строке входных данных задаются числа N и K (1 <= N <= 5000, 1 <= K <= 100).
Следующие N строк содержат описание Петиных кирпичиков: сначала длина L_i,
затем номер цвета C_i (1 <= L_i <= 100, 1 <= C_i <= K). Известно, что у Пети не
более 50 кирпичиков каждого цвета.


Формат вывода:
Выведите в первой строке YES, если Петя сможет построить из своих кирпичиков две
прямоугольные стены высоты K, j-й слой кирпичиков в каждой из которых будет j-го
цвета, и NO в противном случае. В случае положительного ответа, выведите во
второй строке в произвольном порядке номера кирпичиков, из которых следует
построить первую стену (кирпичики нумеруются в том порядке, в котором они заданы
во входных данных, начиная с 1). Если решений несколько, можно выдать любое из
них.


Пример
input: 3 1
input: 1 1
input: 2 1
input: 3 1
output: YES
output: 1
"""
class Solver:
    def __init__(
        self,
        height: int | None = None,
        bricks: list[int] | None = None,
        wall: list[list[tuple[int, int]]] | None = None,
        options: list[list[int]] | None = None,
        intersection: set[int] | None = None,
    ) -> None:
        self.height = height
        self.bricks = bricks or [0]
        self.wall = wall
        self.options = options
        self.common_splits = intersection

    def solve(self) -> None:

        self.parse_data()
        self.build_options()
        print("YES" if self.has_solution() else "NO")
        if solution := self.build_solution():
            print(*solution)

    def parse_data(self) -> None:

        n, self.height = map(int, input().split())
        self.wall = [[] for _ in range(self.height)]
        for i in range(1, n+1):
            length, color = map(int, input().split())
            self.bricks.append(length)
            self.wall[color-1].append((i, length))

    def build_options(self) -> None:

        wall_length = sum([brick[1] for brick in self.wall[-1]])

        self.options = []
        for layer in self.wall:
            option = [0] + [-1] * wall_length
            for brick in layer:
                i, length = brick
                for j in reversed(range(wall_length - length + 1)):
                    if option[j] != -1 and option[j + length] == -1:
                        option[j + length] = i
            self.options.append(option)

    def has_solution(self) -> bool:

        splits: list[set[int]] = []
        for option in self.options:
            current_splits = {
                split for split, i in enumerate(option[1:-1], 1) if i != -1
            }
            splits.append(current_splits)

        self.common_splits = set.intersection(*splits)

        return bool(self.common_splits)

    def build_solution(self) -> list[int] | None:

        if not self.common_splits:
            return None

        common_split = next(iter(self.common_splits))  # достаём любой split

        solution: list[int] = []
        for option in self.options:
            current_length = common_split
            while current_length != 0:
                i = option[current_length]
                solution.append(i)
                current_length -= self.bricks[i]

        return solution


def main() -> None:
    solution = Solver()
    solution.solve()


if __name__ == "__main__":
    main()
