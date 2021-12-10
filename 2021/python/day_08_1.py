from tools import *


class SimpleDisplayDecoder:
    def __init__(self):
        self._signals: list[SignalDecoder] = []

    def parse_input_data(self, input_data: list[str]) -> None:
        for line in input_data:
            unique_signals, decode_signals = line.strip().split("|")
            signal_decoder = SignalDecoder()
            signal_decoder.set_unique_signals(unique_signals.strip().split(" "))
            signal_decoder.set_signal_data(decode_signals.strip().split(" "))
            self._signals.append(signal_decoder)

    def get_1478_count(self) -> int:
        count = 0
        for signal in self._signals:
            count += signal.get_one_count()
            count += signal.get_four_count()
            count += signal.get_seven_count()
            count += signal.get_eight_count()
        return count


class SignalDecoder:
    def __init__(self):
        self._unique_signals: list[str] = []
        self._signal_data: list[str] = []

    def set_unique_signals(self, unique_signals: list[str]) -> None:
        map(sort_string, unique_signals)
        self._unique_signals = unique_signals

    def set_signal_data(self, signal_data: list[str]) -> None:
        map(sort_string, signal_data)
        self._signal_data = signal_data

    def get_one_count(self):
        return self._get_output_of_length_count(2)

    def get_four_count(self):
        return self._get_output_of_length_count(4)

    def get_seven_count(self):
        return self._get_output_of_length_count(3)

    def get_eight_count(self):
        return self._get_output_of_length_count(7)

    def _get_output_of_length_count(self, length: int) -> int:
        count = 0
        for s in self._signal_data:
            if len(s) == length:
                count += 1
        return count


if __name__ == "__main__":
    input_file = "../inputs/08/input.txt"
    # input_file = "../inputs/08/example.txt"
    input_data: list[str] = file_to_list(input_file)
    display_decoder = SimpleDisplayDecoder()
    display_decoder.parse_input_data(input_data)
    print(display_decoder.get_1478_count())
