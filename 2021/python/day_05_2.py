from tools import *
import day_05_1


class VentMap(day_05_1.VentMap):
    def __init__(self):
        super(VentMap, self).__init__()

    def _check_line_add(self, x1: int, y1: int, x2: int, y2: int, i: int) -> None:

        ax1, ax2 = 0, x2 - x1

        if y1 > y2:
            ay1, ay2 = y1 - y2, 0
        else:
            ay1, ay2 = 0, y2 - y1

        if ax1 == ax2 or ay1 == ay2:
            self._add_orthogonal_line(x1, y1, x2, y2, i)
        elif (ax1 == ay1 and ax2 == ay2) or (ax1 == ay2 and ax2 == ay1):
            self._add_diagonal(x1, y1, x2, y2, i)

    def _add_diagonal(self, x1, y1, x2, y2, i):
        y = y1
        for x in range(x1, x2 + 1):
            self._add_point(x, y, i)
            if y1 > y2:
                y -= 1
            else:
                y += 1


if __name__ == "__main__":
    input_file = "../inputs/05/input.txt"
    # input_file = '../inputs/05/example.txt'
    input_data: list[str] = file_to_list(input_file)
    ventmap = VentMap()
    ventmap.read_input(input_data)
    print()
    # print('Map')
    # print(ventmap)
    print("Overlap Count", ventmap.get_overlap_count())
