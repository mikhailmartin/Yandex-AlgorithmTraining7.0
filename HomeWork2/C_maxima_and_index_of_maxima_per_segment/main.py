import sys
import math


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    array = list(map(int, lines[1].split()))
    k = int(lines[2])
    queries = []
    for i in range(k):
        left, right = map(int, lines[3+i].split())
        queries.append((left, right))

    sparse_table, depths = build_sparse_table(array)
    res = []
    for left, right in queries:
        k = query(array, sparse_table, depths, left, right)
        res.append(f"{array[k-1]} {k}")

    return res


def build_sparse_table(array: list[int]) -> tuple[list[list], list[int]]:

    array = [0] + array
    array_length = len(array) - 1
    depths = [-1] + [int(math.log2(length)) for length in range(1, array_length + 1)]

    sparse_table = [[i for i in range(array_length+1)]]
    prev_line = sparse_table[-1]
    for depth in range(1, depths[array_length] + 1):
        window = pow(2, depth)
        gap = pow(2, depth - 1)
        line = [0]
        for j in range(1, array_length - window + 2):
            left_k = prev_line[j]
            right_k = prev_line[j+gap]
            if array[left_k] >= array[right_k]:
                new_k = left_k
            else:
                new_k = right_k
            line.append(new_k)
        sparse_table.append(line)
        prev_line = line

    return sparse_table, depths


def query(
    array: list[int],
    sparse_table: list[list],
    depths: list[int],
    left_array_pointer: int,
    right_array_pointer: int,
) -> int:

    segment_length = right_array_pointer - left_array_pointer + 1
    depth = depths[segment_length]
    line = sparse_table[depth]
    window = pow(2, depth)
    left_line_pointer = left_array_pointer
    right_line_pointer = left_array_pointer + (segment_length - window)
    if left_line_pointer == right_line_pointer:
        k = line[left_line_pointer]
    else:
        left_k = line[left_line_pointer]
        right_k = line[right_line_pointer]
        if array[left_k-1] >= array[right_k-1]:
            k = left_k
        else:
            k = right_k

    return k


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
