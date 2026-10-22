from collections import namedtuple


Node = namedtuple("Node", ["counter", "prefix", "postfix", "flag"])


class Filler(Node):
    ...


class Solver:
    def __init__(
        self,
        array: list[int] | None = None,
        queries: list[tuple[str, int, int]] | None = None,
        segment_tree: list[Node] | None = None,
        shift: int | None = None,
    ) -> None:
        self.array = array
        self.queries = queries or []
        self.segment_tree = segment_tree or []
        self.shift = shift

    def parse_data(self) -> None:

        n = int(input())
        self.array = list(map(int, input().split()))
        m = int(input())
        for _ in range(m):
            command, operand1, operand2 = input().split()
            self.queries.append((command, int(operand1), int(operand2)))

    def build_segment_tree(self) -> None:
        """Строит дерево отрезков в виде массива"""
        array = self.array
        n = len(array)

        size = 1  # размер нижнего слоя
        while size < n:
            size *= 2
        shift = size - 1  # сдвиг в массиве для доступа к нижнему слою

        for _ in range(shift):
            self.segment_tree.append(Filler(0, 0, 0, False))
        # выстраиваем листья
        for element in array:
            is_zero = int(element == 0)
            self.segment_tree.append(Node(is_zero, is_zero, is_zero, bool(is_zero)))
        for _ in range(size - n):
            self.segment_tree.append(Filler(0, 0, 0, False))
        # выстраиваем внутренние узлы
        for index in reversed(range(shift)):
            self.segment_tree[index] = self.build_node_from_index(index)

        self.shift = shift

    def build_node_from_index(self, index: int) -> Node:

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        left_child_node = self.segment_tree[left_child_index]
        right_child_node = self.segment_tree[right_child_index]

        node = self.build_node_from_nodes(left_child_node, right_child_node)

        return node

    @staticmethod
    def build_node_from_nodes(left_node: Node, right_node: Node) -> Node:

        if isinstance(right_node, Filler):
            return left_node

        if left_node.flag:
            if right_node.flag:
                counter = prefix = postfix = left_node.postfix + right_node.prefix
                flag = True
            else:
                counter = prefix = left_node.counter + right_node.prefix
                postfix = right_node.postfix
                flag = False
        else:
            if right_node.flag:
                counter = postfix = left_node.postfix + right_node.counter
                prefix = left_node.prefix
                flag = False
            else:
                counter = max(
                    left_node.counter,
                    right_node.counter,
                    left_node.postfix + right_node.prefix,
                )
                prefix = left_node.prefix
                postfix = right_node.postfix
                flag = False

        node = Node(counter, prefix, postfix, flag)

        return node

    def solve(self) -> None:

        answer = []
        for command, operand1, operand2 in self.queries:
            match command:
                case "UPDATE":
                    self.u_query(operand1, operand2)
                case "QUERY":
                    node = self.s_query(
                        left_segment_border=operand1-1,
                        right_segment_border=operand2-1,
                        left_node_border=0,
                        right_node_border=self.shift,
                    )
                    answer.append(str(node.counter))
                case _:
                    raise ValueError
        print("\n".join(answer))

    def u_query(self, number: int, value: int) -> None:

        index = number + self.shift - 1
        is_zero = int(value == 0)
        self.segment_tree[index] = Node(is_zero, is_zero, is_zero, bool(is_zero))
        parent_index = (index - 1) // 2
        flag = True
        while flag:
            # если дошли до корня дерева
            if parent_index == 0:
                flag = False
            old_parent_value = self.segment_tree[parent_index]
            new_parent_value = self.build_node_from_index(parent_index)
            # если обновление не задело значение в родительском узле
            if old_parent_value != new_parent_value:
                self.segment_tree[parent_index] = new_parent_value
                parent_index = (parent_index - 1) // 2
            else:
                flag = False

    def s_query(
        self,
        left_segment_border: int,
        right_segment_border: int,
        left_node_border: int,
        right_node_border: int,
        node_index: int = 0,
    ) -> Node:

        # мимо
        if (
            right_segment_border < left_node_border
            or left_segment_border > right_node_border
        ):
            return Node(0, 0, 0, False)

        # сегмент полностью накрывает узел
        elif (
            left_segment_border <= left_node_border
            and right_segment_border >= right_node_border
        ):
            return self.segment_tree[node_index]

        # сегмент частично накрывает узел
        else:
            left_child_node_index = 2 * node_index + 1
            left_child_left_border = left_node_border
            left_child_right_border = (left_node_border + right_node_border) // 2

            right_child_node_index = 2 * node_index + 2
            right_child_left_border = (left_node_border + right_node_border) // 2 + 1
            right_child_right_border = right_node_border

            left_child_ = self.s_query(
                left_segment_border,
                right_segment_border,
                left_child_left_border,
                left_child_right_border,
                left_child_node_index,
            )
            right_child_ = self.s_query(
                left_segment_border,
                right_segment_border,
                right_child_left_border,
                right_child_right_border,
                right_child_node_index,
            )

            node = self.build_node_from_nodes(left_child_, right_child_)

            return node


def main() -> None:

    solver = Solver()
    solver.parse_data()
    solver.build_segment_tree()
    solver.solve()


if __name__ == "__main__":
    main()
