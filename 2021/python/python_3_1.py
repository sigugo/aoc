from tools import *

def count_high_at_index(data: list[str], index: int) -> int:
    high = "1"
    return count_char_at_index(data, high, index)


class Diagnostics():
    def __init__(self):
        self._diagnostic_data: list[str] = []
        self._line_length: int = 0
        self._line_count: int = 0

    def read_diagnostic_datafile(self, file_name):
        self._diagnostic_data = file_to_list(file_name)
        self._line_length = len(self._diagnostic_data[0])
        self._line_count = len(self._diagnostic_data)

    def get_gamma(self) -> str:
        one = "1"
        zero = binary_invert(one)
        gamma: str = ""

        for i in range(self._line_length):
            c = count_high_at_index(self._diagnostic_data, i)
            if c > self._line_count/2:
                gamma += one 
            elif c < self._line_count/2:
                gamma += zero
            else:
                raise ValueError('Can\'t resolve winning bit')
        return gamma

    def get_epsilon(self) -> str:
        return(binary_invert(self.get_gamma()))
     

if __name__ == '__main__':
    input_file = '../inputs/3/input.txt'
    # input_file = '../inputs/3/example.txt'
    report = Diagnostics()
    report.read_diagnostic_datafile(input_file)
    print(int(report.get_gamma(), base=2) * int(report.get_epsilon(), base=2))
