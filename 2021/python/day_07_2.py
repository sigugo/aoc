from tools import *
import day_07_1


class CrabCast(day_07_1.CrabCast):
    def __init__(self):
        super(CrabCast, self).__init__()

    def _move_cost_to_target(self, start_position: int, target_position: int) -> int:
        # inspired by: https://math.stackexchange.com/questions/1908152/how-to-calculate-the-sum-of-an-incremental-string-of-numbers
        distance = abs(target_position - start_position)
        return int(
            distance * (distance + 1) / 2 * self._cast_postitions[start_position]
        )


if __name__ == "__main__":
    input_file = "../inputs/07/input.txt"
    # input_file = "../inputs/07/example.txt"
    input_data: list[str] = file_to_list(input_file)
    cast = CrabCast()
    cast.parse_input_data(input_data[0])
    print(cast.get_cheapest_target_position_cost())

