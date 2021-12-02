import python_1_1
from copy import deepcopy


class SonarSweep(python_1_1.SonarSweep):

    def __init__(self):
        super().__init__()

    def count_sliding_depth_increases(self, window_size: int = 3) -> int:
        last = None
        n = 0
        window = []
        last_window = None
        for value in self._sonar_values:
            if len(window) == window_size:
                last_window = deepcopy(window)
                del window[0]
            window.append(value)
            if last_window:
                if self.get_depth_change(sum(last_window), sum(window)) > 0:
                    n += 1

        return n


if __name__ == '__main__':
    input_file = '../inputs/1/input.txt'
    sweep = SonarSweep()
    sweep.read_input_file(input_file)
    print(sweep.count_sliding_depth_increases())

