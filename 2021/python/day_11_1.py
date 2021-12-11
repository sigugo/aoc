from tools import *


class GameOfOctopodes:
    def __init__(self, input_data: list[str] = []):
        self._consortium: list[list[int]] = []
        self._cycles: int = 0
        self._flashes: int = 0
        self._energy_threshold: int = 10
        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input_data: list[str]) -> None:
        for line in input_data:
            line = list(line.strip())
            self._consortium.append(list(map(int, line)))

    def advance_lifecycles(self, count: int = 100):
        for foo in range(count):
            self._cycles += 1
            self._flashes += self._run_lifecycle()

    def _run_lifecycle(self) -> int:
        for y in range(len(self._consortium)):
            for x in range(len(self._consortium[y])):
                self._raise_energy(x, y)
        flashes = 0
        for y in range(len(self._consortium)):
            for x in range(len(self._consortium[y])):
                if self._get_energy(x, y) >= self._energy_threshold:
                    flashes += 1
                    self._set_energy(x, y, 0)
        return flashes

    def _raise_energy(self, x, y):
        energy = self._get_energy(x, y)
        if energy >= 0:
            self._set_energy(x, y, energy + 1)
            if energy == self._energy_threshold - 1:
                for x2 in range(x - 1, x + 2):
                    for y2 in range(y - 1, y + 2):
                        self._raise_energy(x2, y2)

    def _get_energy(self, x: int, y: int) -> int:
        return get_2d_matrix_value_at_x_y_safe(self._consortium, x, y, -1)

    def _set_energy(self, x: int, y: int, energy: int) -> None:
        self._consortium = set_2d_matrix_value_at_x_y_safe(
            self._consortium, x, y, energy
        )

    def get_flashes(self) -> int:
        return self._flashes


if __name__ == "__main__":
    input_file = "../inputs/11/data.input"
    # input_file = "../inputs/11/data.example"
    input_data: list[str] = file_to_list(input_file)
    consortium = GameOfOctopodes(input_data)
    consortium.advance_lifecycles()
    print(consortium.get_flashes())
