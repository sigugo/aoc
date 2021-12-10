from tools import *
import day_09_1


class CaveMap(day_09_1.CaveMap):
    def __init__(self, input_data):
        super(CaveMap, self).__init__()
        self.parse_input_data(input_data)
        self._basin_map: list[list[int]] = []
        self._no_basin_index: int = 0
        self._basin_index: int = self._no_basin_index
        self._initialize_basin_map()

    def _initialize_basin_map(self) -> None:
        for y in self._map:
            basin_x = []
            for x in y:
                basin_x.append(self._no_basin_index)
            self._basin_map.append(basin_x)

    def map_basins(self) -> None:
        for y in range(len(self._map)):
            for x in range(len(self._map[y])):
                self._walk_basin(x, y)

    def _walk_basin(self, x: int = 0, y: int = 0, new_basin: bool = True):
        point_basin_index = self._get_basin_index_at_coordinate(x, y)
        is_basin_point = self._is_basin_point(x, y)
        if point_basin_index == self._no_basin_index and is_basin_point:
            if new_basin and self._get_max_basin_index() == self._basin_index:
                self._basin_index += 1
            self._set_basin_index_at_coordinate(x, y, self._basin_index)
            self._walk_basin(x + 1, y, False)
            self._walk_basin(x - 1, y, False)
            self._walk_basin(x, y + 1, False)
            self._walk_basin(x, y - 1, False)

    def _get_basin_index_at_coordinate(self, x, y, debug=0) -> int:
        return get_2d_matrix_value_at_x_y_safe(
            self._basin_map, x, y, self._no_basin_index, debug
        )

    def _set_basin_index_at_coordinate(self, x, y, i) -> None:
        self._basin_map[y][x] = i

    def _is_basin_point(self, x, y) -> bool:
        if self._get_value_at_coordinate(x, y) == self._max_val:
            return False
        return True

    def _get_max_basin_index(self) -> int:
        max_basin_index = self._no_basin_index
        for y in range(len(self._map)):
            for x in range(len(self._map[y])):
                point_basin_index = self._get_basin_index_at_coordinate(x, y)
                if point_basin_index > max_basin_index:
                    max_basin_index = point_basin_index
        return max_basin_index

    def get_largest_basins_product(self, count: int = 3) -> int:
        basin_sizes = self._get_basin_sizes_list()
        basin_sizes.sort(reverse=True)
        product = 1
        for n in basin_sizes[:count]:
            product *= n
        return product

    def _get_basin_sizes_list(self) -> list[int]:
        size_dict: dict[int, int] = {}
        for y in range(len(self._map)):
            for x in range(len(self._map[y])):
                index = self._get_basin_index_at_coordinate(x, y)
                if index > 0:
                    size_dict[index] = size_dict.setdefault(index, 0) + 1
        return list(size_dict.values())


if __name__ == "__main__":
    input_file = "../inputs/9/data.input"
    # input_file = "../inputs/9/data.example"
    input_data: list[str] = file_to_list(input_file)
    map = CaveMap(input_data)
    map.map_basins()
    print(map.get_largest_basins_product())
