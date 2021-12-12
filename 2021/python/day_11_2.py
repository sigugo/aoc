from tools import file_to_list
import day_11_1


class GameOfOctopodes(day_11_1.GameOfOctopodes):
    def __init__(self, input_data: list[str] = []):
        self._size: int = 0
        super(GameOfOctopodes, self).__init__(input_data)

    def parse_input(self, input_data: list[str]) -> None:
        for line in input_data:
            line = list(line.strip())
            self._consortium.append(list(map(int, line)))
        self._calculate_size()

    def _calculate_size(self):
        size = 0
        for i in self._consortium:
            size += len(i)
        self._size = size

    def advance_lifecycle_until_all_flash(self):
        flashes = 0
        while flashes < self._size:
            self._cycles += 1
            flashes = self._run_lifecycle()
            self._flashes += flashes

    def get_cycle(self) -> int:
        return self._cycles


if __name__ == "__main__":
    input_file = "../inputs/11/data.input"
    # input_file = "../inputs/11/data.example"
    input_data: list[str] = file_to_list(input_file)
    consortium = GameOfOctopodes(input_data)
    consortium.advance_lifecycle_until_all_flash()
    print(consortium.get_cycle())
