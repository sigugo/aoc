from tools import *


class CrabCast:
    def __init__(self):
        self._cast_postitions: list[int] = []

    def parse_input_data(self, input_data: str) -> None:
        cast_positions: list[int] = []
        for value in input_data.strip().split(","):
            cast_positions.append(int(value))
        self._cast_postitions = [0] * (max(cast_positions) + 1)
        for value in cast_positions:
            self._cast_postitions[value] += 1

    def get_cheapest_target_position(self) -> int:
        return min(self._get_target_position_costs())

    def _get_target_position_costs(self) -> list[int]:
        target_position_costs = [0] * len(self._cast_postitions)
        for i in range(len(target_position_costs)):
            for j in range(len(self._cast_postitions)):
                target_position_costs[i] += self._move_cost_to_target(j, i)
        return target_position_costs

    def _move_cost_to_target(self, start_position: int, target_position: int) -> int:
        distance = abs(target_position - start_position)
        return distance * self._cast_postitions[start_position]

    def __str__(self):
        output = ""
        for i in range(len(self._cast_postitions)):
            if self._cast_postitions[i] > 0:
                output += (str(i) + ",") * self._cast_postitions[i]
        return output[:-1]


if __name__ == "__main__":
    input_file = "../inputs/7/input.txt"
    # input_file = "../inputs/7/example.txt"
    input_data: list[str] = file_to_list(input_file)
    cast = CrabCast()
    cast.parse_input_data(input_data[0])
    print(cast.get_cheapest_target_position())
