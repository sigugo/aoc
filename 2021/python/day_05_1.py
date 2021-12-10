from tools import *


class VentMap:
    def __init__(self):
        self._map: dict[tuple[int, int], list[int]] = {}

    def read_input(self, input_data: list[str]) -> None:
        for i in range(len(input_data)):
            coords = input_data[i].strip().split(" -> ")
            start = coords[0].split(",")
            end = coords[1].split(",")
            x1 = int(start[0])
            y1 = int(start[1])
            x2 = int(end[0])
            y2 = int(end[1])

            if x1 > x2 or (x1 == x2 and y1 > y2):
                x1, y1, x2, y2 = x2, y2, x1, y1

            self._check_line_add(x1, y1, x2, y2, i)

    def _check_line_add(self, x1: int, y1: int, x2: int, y2: int, i: int) -> None:
        if x1 == x2 or y1 == y2:
            self._add_orthogonal_line(x1, y1, x2, y2, i)

    def _add_orthogonal_line(self, x1, y1, x2, y2, i) -> None:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self._add_point(x, y, i)

    def _add_point(self, x: int, y: int, i: int = 0) -> None:
        self._map.setdefault((x, y), []).append(i)

    def get_overlap_count(self) -> int:
        return len(self._get_overlapping_coordinates())

    def _get_overlapping_coordinates(self) -> list[tuple[int, int]]:
        result: list[tuple[int, int]] = []
        for k, v in self._map.items():
            if len(v) > 1:
                result.append(k)
        return result

    def __str__(self) -> str:
        output = ""
        x1, y1, x2, y2 = 0, 0, 0, 0
        for t in self._map:
            if t[0] > x2:
                x2 = t[0]
            if t[1] > y2:
                y2 = t[1]

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                indexes = self._map.get((x, y), [])
                if len(indexes) > 0:
                    output += str(len(indexes))
                else:
                    output += "."
            output += "\n"
        return output


if __name__ == "__main__":
    input_file = "../inputs/05/input.txt"
    # input_file = '../inputs/05/example.txt'
    input_data: list[str] = file_to_list(input_file)
    ventmap = VentMap()
    ventmap.read_input(input_data)
    # print()
    # print('Map')
    # print(ventmap)
    print("Overlap Count", ventmap.get_overlap_count())
