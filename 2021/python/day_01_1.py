from tools import file_to_list


class SonarSweep:
    def __init__(self):
        self._sonar_values = list[int]

    def read_input_file(self, file_name: str) -> None:
        self._sonar_values = [int(value) for value in file_to_list(file_name)]

    @staticmethod
    def get_depth_change(last_depth: int, current_depth: int) -> int:
        return current_depth - last_depth

    def count_depth_increases(self) -> int:
        last = None
        n = 0
        for value in self._sonar_values:
            if last:
                if self.get_depth_change(last, value) > 0:
                    n += 1
            last = value
        return n


if __name__ == "__main__":
    input_file = "../inputs/01/input.txt"
    sweep = SonarSweep()
    sweep.read_input_file(input_file)
    print(sweep.count_depth_increases())
