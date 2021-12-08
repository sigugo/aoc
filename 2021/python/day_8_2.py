from tools import *
from copy import deepcopy
import day_8_1


class DisplayDecoder:
    def __init__(self):
        self._signals: list[SignalDecoder] = []

    def parse_input_data(self, input_data: list[str]) -> None:
        for line in input_data:
            unique_signals, decode_signals = line.strip().split("|")
            signal_decoder = SignalDecoder()
            signal_decoder.set_unique_signals(
                sorted(unique_signals.strip().split(" "), key=len)
            )
            signal_decoder.set_signal_data(decode_signals.strip().split(" "))
            signal_decoder.build_signal_list()
            self._signals.append(signal_decoder)

    def get_signal_sum(self) -> int:
        result = 0
        for signal in self._signals:
            result += signal.get_signal_value()
        return result


def characters_not_in_second_string(first: str, second: str) -> str:
    """
    String first and second are compared,
    the output will be a string ouf all characters that are in string first but not in string second
    :param first: str
    :param second: str
    :return: str
    """
    chars = ""
    for c in first:
        if second.find(c) == -1:
            chars += c
    return chars


def remove_string_from_list(strings: list[str], string: [str]) -> list[str]:
    """
    Will remove all occurrences of string from the list strings and return it
    :param strings: list[str]
    :param string: str
    :return: list[str]
    """
    del strings[strings.index(string)]
    return strings


def strings_from_list_containing_characters(
    strings: list[str], search: str
) -> list[str]:
    """
    Looks through the list "strings".
    Will return a list of all items in strings, that contain all characters of "search"
    :param strings: list[str]
    :param search: str
    :return: list[str]
    """
    output: list[str] = []
    for string in strings:
        match = True
        for c in search:
            if string.find(c) == -1:
                match = False
        if match:
            output.append(string)
    return output


def get_strings_with_difference_n_from_second(
    first_strings: list[str], second_strings: list[str], n: int
) -> list[str]:
    """
    Looks at the two list of strings, first_strings and second_strings.
    Will return all entries from second_strings that differ by n characters from any entry in first_strings
    :param first_strings: list[str]
    :param second_strings: list[str]
    :param n: int
    """
    output: list[str] = []
    for first in first_strings:
        for second in second_strings:
            if abs(len(first) - len(second)) == n:
                output.append(second)


def common_characters(first: str, second: str) -> str:
    """
    Takes two strings and returns the common characters as a string
    :param first: str
    :param second: str
    :return: str
    """
    output = ""
    for c in first:
        if second.find(c) != -1:
            output += c
    return output


class SignalDecoder(day_8_1.SignalDecoder):
    def __init__(self):
        super(SignalDecoder, self).__init__()
        self._signals: list[str] = []
        self._signal_list: list[str] = 0

    def set_unique_signals(self, unique_signals: list[str]) -> None:
        unique_signals = list(map(sort_string, unique_signals))
        self._unique_signals = unique_signals

    def set_signal_data(self, signal_data: list[str]) -> None:
        signal_data = list(map(sort_string, signal_data))
        self._signal_data = signal_data

    def build_signal_list(self):
        signal_list: list[str] = [""] * 10

        signal_list[1] = self._unique_signals_with_length(2)[0]  # found 1
        signal_list[4] = self._unique_signals_with_length(4)[0]  # found 1,4
        signal_list[7] = self._unique_signals_with_length(3)[0]  # found 1,4,7
        signal_list[8] = self._unique_signals_with_length(7)[0]  # found 1,4,7,8

        length_5 = self._unique_signals_with_length(5)  # contains 2,3,5
        length_6 = self._unique_signals_with_length(6)  # contains 0,6,9

        a = characters_not_in_second_string(signal_list[7], signal_list[1])  # found a
        bd = characters_not_in_second_string(signal_list[4], signal_list[1])
        abdeg = characters_not_in_second_string(signal_list[8], signal_list[1])
        bdeg = characters_not_in_second_string(abdeg, a)
        eg = characters_not_in_second_string(bdeg, bd)

        # out of length_5 only the number 2 will have eg in it
        signal_list[2] = strings_from_list_containing_characters(length_5, eg)[
            0
        ]  # found 1,2,4,7,8

        bf = characters_not_in_second_string(signal_list[8], signal_list[2])

        b = common_characters(bf, bd)  # found a, b
        d = characters_not_in_second_string(bd, b)  # found a, b, d
        f = characters_not_in_second_string(bf, b)  # found a, b, d, f
        c = characters_not_in_second_string(
            signal_list[1], f
        )  # found a, b, c, d, f / missing e, g

        cdefg = characters_not_in_second_string(signal_list[8], a + b)

        # removing the d line from 8 gives us a 0
        signal_list[0] = signal_list[8].replace(d, "")  # 0,1,2,4,7,8

        length_6 = remove_string_from_list(length_6, signal_list[0])  # contains 6,9

        for s in length_6:
            temp = characters_not_in_second_string(s, a + b + c + d + f)
            if len(temp) == 1:
                g = temp
        e = characters_not_in_second_string(eg, g)

        signal_list[3] = a + c + d + f + g
        signal_list[5] = a + b + d + f + g
        signal_list[6] = a + b + d + e + f + g
        signal_list[9] = a + b + c + d + f + g

        signal_list = list(map(sort_string, signal_list))

        self._signal_list = deepcopy(signal_list)

    def get_signal_value(self) -> int:
        if not self._signal_list:
            self.build_signal_list()
        # return int(self.get_signal_string())
        output = 0
        for d in self._signal_data:
            output *= 10
            output += self._signal_list.index(d)
        return output

    def get_signal_string(self) -> str:
        if not self._signal_list:
            self.build_signal_list()
        output = ""
        for d in self._signal_data:
            output += str(self._signal_list.index(d))
        return output

    def _unique_signals_with_length(self, length: int):
        output: list[str] = []
        for signal in self._unique_signals:
            if len(signal) == length:
                output.append(signal)
        return output

    def __str__(self) -> str:
        return self.get_signal_string()


if __name__ == "__main__":
    input_file = "../inputs/8/input.txt"
    # input_file = "../inputs/8/example.txt"
    # input_file = "../inputs/8/example2.txt"
    input_data: list[str] = file_to_list(input_file)
    display_decoder = DisplayDecoder()
    display_decoder.parse_input_data(input_data)
    print(display_decoder.get_signal_sum())
