"""
Каждому по компьютеру

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В новом учебном году во Дворец Творчества Юных для занятий в компьютерных
классах пришли учащиеся, которые были разбиты на N групп. В i-й группе оказалось
X_i человек. Тут же перед директором встала серьёзная проблема: как распределить
группы по аудиториям. Во дворце имеется M ≥ N аудиторий, в j-й аудитории имеется
Y_j компьютеров. Для занятий необходимо, чтобы у каждого учащегося был компьютер
и ещё один компьютер был у преподавателя. Переносить компьютеры из одной
аудитории в другую запрещается. Помогите директору!

Напишите программу для поиска максимального количества групп, которое удастся
одновременно распределить по аудиториям, чтобы всем учащимся в каждой группе
хватило компьютеров, и при этом остался хотя бы один для учителя.


Формат ввода:
На первой строке входного файла расположены числа N и M (1 ≤ N ≤ M ≤ 1000).
На второй строке расположено N чисел — X_1, …, X_N (1 ≤ X_i ≤ 1000 для всех
1 ≤ i ≤ N). На третьей строке расположено M чисел Y_1, ..., Y_M (1 ≤ Y_i ≤ 1000
для всех 1 ≤ i ≤ M).


Формат вывода:
Выведите на первой строке число P — количество групп, которое удастся
распределить по аудиториям. На второй строке выведите распределение групп по
аудиториям — N чисел, i-е число должно соответствовать номеру аудитории,
в которой должна заниматься i-я группа. Нумерация как групп, так и аудиторий,
начинается с 1. Если i-я группа осталась без аудитории, i-е число должно быть
равно 0. Если допустимых распределений несколько, выведите любое из них.


Примеры:
Пример 1
input: 1 1
input: 1
input: 2
output: 1
output: 1

Пример 2
input: 1 1
input: 1
input: 1
output: 0
output: 0
"""
def main() -> None:

    groups, classrooms = parse_data()
    counter, distribution = solve(groups, classrooms)
    print(counter)
    print(*distribution)


def parse_data() -> tuple[list[int], list[int]]:

    n, m = map(int, input().split())
    groups = list(map(int, input().split()))
    classrooms = list(map(int, input().split()))

    return groups, classrooms


def solve(groups: list[int], classrooms: list[int]) -> tuple[int, list[int]]:

    groups = list(enumerate(groups))
    classrooms = list(enumerate(classrooms))

    groups = sorted(groups, key=lambda x: x[1], reverse=True)
    classrooms = sorted(classrooms, key=lambda x: x[1], reverse=True)

    group_pointer = 0
    classroom_pointer = 0
    counter = 0
    distribution = []
    while group_pointer < len(groups) and classroom_pointer < len(classrooms):

        group_index, group = groups[group_pointer]
        classroom_index, classroom = classrooms[classroom_pointer]

        if classroom >= group + 1:
            counter += 1
            distribution.append((group_index, classroom_index+1))
            group_pointer += 1
            classroom_pointer += 1
        else:
            group_pointer += 1
            distribution.append((group_index, 0))

    distribution = sorted(distribution, key=lambda x: x[0])
    distribution = [classroom_index for group_index, classroom_index in distribution]

    return counter, distribution


if __name__ == "__main__":
    main()
