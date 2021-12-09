from tools import *


class CaveMap:
    def __init__(self):
        self._min_val = 0
        self._max_val = 9
        self._map: list[list[int]] = []

    def parse_input_data(self, input_data):
        for line in input_data:
            line_list: list[int] = []
            for c in list(line.strip()):
                line_list.append(int(c))
            self._map.append(line_list)

    def get_risklevel_sum(self) -> int:
        sum: int = 0
        for entry in self.find_lowpoints():
            x, y = entry
            sum += self._get_value_at_coordinate(x, y) + 1
        return sum

    def find_lowpoints(self) -> list[tuple[int, int]]:
        lowpoints: list[tuple[int, int]] = []
        for y in range(len(self._map)):
            for x in range(len(self._map[y])):
                if self._is_lowpoint(x, y):
                    lowpoints.append((x, y))
        return lowpoints

    def _is_lowpoint(self, x, y) -> bool:
        is_lowpoint = True
        if self._get_value_at_coordinate(x + 1, y) <= self._get_value_at_coordinate(x, y):
            is_lowpoint = False
        elif self._get_value_at_coordinate(x - 1, y) <= self._get_value_at_coordinate(x, y):
            is_lowpoint = False
        elif self._get_value_at_coordinate(x, y + 1) <= self._get_value_at_coordinate(x, y):
            is_lowpoint = False
        elif self._get_value_at_coordinate(x, y - 1) <= self._get_value_at_coordinate(x, y):
            is_lowpoint = False
        return is_lowpoint

    def _get_value_at_coordinate(self, x, y, debug=0):
        return get_2d_matrix_value_at_x_y_safe(self._map, x, y, self._max_val)


if __name__ == "__main__":
    input_file = "../inputs/9/data.input"
    # input_file = "../inputs/9/data.example"
    input_data: list[str] = file_to_list(input_file)
    map = CaveMap()
    map.parse_input_data(input_data)
    print(map.get_risklevel_sum())
