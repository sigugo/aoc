from tools import *


class VentMap:
    def __init__(self):
        self._map: dict[tuple[int, int], list[int]] = {}

    def read_input(self, input_data: list[str]) -> None:
        for i in range(len(input_data)):

            # this sucks, but my brain is offline atm
            coords = input_data[i].strip().split(" -> ")
            start = coords[0].split(',')
            end = coords[1].split(',')
            x1 = int(start[0])
            y1 = int(start[1])
            x2 = int(end[0])
            y2 = int(end[1])

            if x1 == x2 or y1 == y2:
                print("## adding orthogonal", x1, ",", y1, "->", x2, ",", y2)
                self._add_orthogonal_line(x1, y1, x2, y2, i)
            elif x1 == y2 and x2 == y1:
                print("## adding diagonal", x1, ",", y1, "->", x2, ",", y2)
            else:
                print("## discarding", x1, ",", y1, "->", x2, ",", y2)

    def _add_orthogonal_line(self, x1, y1, x2, y2, i) -> None:
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                print("- coordinate added:", x , y, "with index", i)
                self._map.setdefault((x, y), []).append(i)

    def get_overlap_count(self) -> int:
        return len(self.get_overlapping_coordinates())

    def get_overlapping_coordinates(self) -> list[tuple[int, int]]:
        result: list[tuple[int, int]] = []
        for k, v in self._map.items():
            if len(v) > 1:
                result.append(k)
        return result


if __name__ == '__main__':
    input_file = '../inputs/5/example.txt'
    input_data: list[str] = file_to_list(input_file)
    print(input_data)
    ventmap = VentMap()
    ventmap.read_input(input_data)
    print(ventmap.get_overlap_count())
