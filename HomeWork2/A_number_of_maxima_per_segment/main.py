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
        max_, count_ = query(sparse_table, depths, left, right)
        res.append(f"{max_} {count_}")

    return res


def build_sparse_table(arr: list[int]) -> tuple[list[list], list[int]]:

    arr = [(0, 0)] + [(num, 1) for num in arr]
    array_length = len(arr) - 1
    depths = [-1] + [int(math.log2(length)) for length in range(1, array_length+1)]

    sparse_table = [arr]
    prev_line = arr
    for depth in range(1, depths[array_length]+1):
        window = pow(2, depth)
        gap = pow(2, depth-1)
        line = [(0, 0)]
        for j in range(1, array_length - window + 2):
            left_max, left_count = prev_line[j]
            right_max, right_count = prev_line[j+gap]
            if left_max > right_max:
                new_max = left_max
                new_count = left_count
            elif right_max > left_max:
                new_max = right_max
                new_count = right_count
            else:  # left_max == right_max
                new_max = left_max
                new_count = left_count + right_count
            line.append((new_max, new_count))
        sparse_table.append(line)
        prev_line = line

    return sparse_table, depths


def query(
    sparse_table: list[list],
    depths: list[int],
    left_array_pointer: int,
    right_array_pointer: int,
) -> tuple[int, int]:

    segment_length = right_array_pointer - left_array_pointer + 1
    depth = depths[segment_length]
    line = sparse_table[depth]
    window = pow(2, depth)
    left_line_pointer = left_array_pointer
    right_line_pointer = left_array_pointer + (segment_length - window)
    if left_line_pointer == right_line_pointer:
        max_, count_ = line[left_line_pointer]
    else:
        left_max, left_count = line[left_line_pointer]
        right_max, right_count = line[right_line_pointer]
        if left_max > right_max:
            max_ = left_max
            count_ = left_count
        elif right_max > left_max:
            max_ = right_max
            count_ = right_count
        else:    # left_max == right_max
            max_ = left_max
            count_ = left_count + right_count
            intersect_max, intersect_count = query(
                sparse_table,
                depths,
                left_array_pointer + (segment_length - window),
                right_array_pointer - (segment_length - window),
            )
            if intersect_max == max_:
                count_ -= intersect_count

    return max_, count_


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
