from copy import deepcopy


def file_to_list(file_name: str) -> list:
    output = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            output.append(line)
    return output


def get_2d_matrix_value_at_x_y_safe(
    matrix: list[list[int]], x: int, y: int, no_value_value: int = 0
) -> int:
    value = no_value_value
    if 0 <= y < len(matrix):
        if 0 <= x < len(matrix[y]):
            value = matrix[y][x]
    return value


class PathRisk:
    def __init__(self, input_data: list[str] = []):
        self._riskmap: list[list[int]] = []
        self._costmap: list[list[int]] = []
        self._exit: tuple[int, int] = ()
        self._paths: list[tuple[int, int, int]] = []
        self._cheapest_path_value: int = 0
        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input: list[str]) -> None:
        max_field_cost: int = 9
        for line in input:
            self._riskmap.append(list(map(int, list(line))))
        ym: int = len(self._riskmap) - 1
        xmym: int = len(self._riskmap[ym]) - 1
        for i in range(ym + 1):
            line: list[int] = []
            for j in range(len(self._riskmap[i])):
                line.append(max_field_cost * (i + j))
            self._costmap.append(line)
        self._exit = (xmym, ym)
        for i in range(1, len(self._riskmap) - 1):
            self._cheapest_path_value += self._riskmap[i][0]
        for j in range(xmym + 1):
            self._cheapest_path_value += self._riskmap[ym][j]
        self._paths.append((0, 0, 0))
        self._get_cheapest_path()

    def _get_cheapest_path(self) -> None:
        iter = self._cheapest_path_value
        while True:
            paths: list[tuple[int, int, int]] = []
            for cost, x, y in self._paths:
                if not self._at_exit(x, y):
                    for xn, yn in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                        next_value = self._get_value(xn, yn)
                        next_cost = cost + next_value
                        if next_value > 0 and next_cost <= self._cheapest_path_value:
                            if next_cost < self._get_lowest_cost(xn, yn):
                                paths.append((next_cost, xn, yn))
                                self._set_lowest_cost(xn, yn, next_cost)
                                if (
                                    self._at_exit(xn, yn)
                                    and next_cost < self._cheapest_path_value
                                ):
                                    self._cheapest_path_value = next_cost
            if len(paths) == 0:
                print(self._cheapest_path_value)
                break
            self._paths = deepcopy(paths)
            self._paths = paths

    def _at_exit(self, x: int, y: int):
        return (x, y) == self._exit

    def _get_value(self, x: int, y: int) -> int:
        default: int = 0
        return get_2d_matrix_value_at_x_y_safe(self._riskmap, x, y)

    def _get_lowest_cost(self, x, y) -> int:
        return self._costmap[y][x]

    def _set_lowest_cost(self, x, y, cost) -> None:
        self._costmap[y][x] = cost

    def __str__(self) -> str:
        output = ""
        for y in range(len(self._riskmap)):
            line = ""
            for x in range(len(self._riskmap[y])):
                line += str(self._riskmap[y][x])
            output += line + "\n"
        return output


if __name__ == "__main__":
    input_file = "../inputs/15/data.input"
    # input_file = "../inputs/15/data.example"
    input_data: list[str] = file_to_list(input_file)
    risk = PathRisk(input_data)
