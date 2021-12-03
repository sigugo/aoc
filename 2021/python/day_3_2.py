from tools import binary_invert
from day_3_1 import count_high_at_index
from day_3_1 import Diagnostics as DiagnosticsSuper
from copy import deepcopy


class Diagnostics(DiagnosticsSuper):
    def __init__(self):
        super(Diagnostics, self).__init__()
 
    def _get_rating(self, default: str = "1") -> str:
        data = deepcopy(self._diagnostic_data)
        fallback = binary_invert(default)
        for i in range(self._line_length):
            results: list[str] = []
            matches = count_high_at_index(data, i)
            if matches >= len(data)/2:
                result = default
            else:
                result = fallback
            for line in data:
                if line[i] == result:
                    results.append(line)
            if len(results) == 1:
                return int(results.pop(),2)
            else:
                data = deepcopy(results)
   

    def get_oxygen_rating(self) -> str:
        return self._get_rating()
     
    def get_scrubber_rating(self) -> str:
        return self._get_rating("0")

    def get_life_support_rating(self) -> int:
        return self.get_oxygen_rating() * self.get_scrubber_rating()


if __name__ == '__main__':
    # input_file = '../inputs/3/example.txt'
    input_file = '../inputs/3/input.txt'
    
    report = Diagnostics()
    report.read_diagnostic_datafile(input_file)

    print("Oxygen")
    print(report._get_rating())
    print("---")

    print("CO2")
    print(report.get_scrubber_rating())
    print("---")
    
    print("AOC result")
    print(report.get_life_support_rating())

