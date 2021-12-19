from tools import *
from dataclasses import dataclass
from abc import ABC, abstractmethod, abstractproperty
from ast import literal_eval
from math import floor, ceil


@dataclass
class SnailfishNumber(ABC):
    @abstractproperty
    def magnitude(self) -> int:
        pass

    def __add__(self, other):
        return SnailfishPair(self, other)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractproperty
    def depth(self) -> int:
        pass


@dataclass
class SnailfishInt(SnailfishNumber):
    value: int

    @property
    def magnitude(self) -> int:
        return self.value

    def __str__(self):
        return str(self.value)

    def split(self) -> SnailfishPair:
        return SnailfishPair(
            SnailfishInt(floor(self.value / 2)), SnailfishInt(ceil(self.value / 2))
        )


@dataclass
class SnailfishPair(SnailfishNumber):
    left: SnailfishNumber
    right: SnailfishNumber

    @property
    def magnitude(self) -> idt:
        return 3 * self.left.magnitude + 2 * self.right.magnitude

    def __str__(self):
        return "[" + str(self.left) + "," + str(self.right) + "]"


class SnailfishMath:
    def __init__(self, input_data: list[str] = []):
        self._data: list[SnailfishNumber]
        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input_data: list[str]):
        for line in input_data:
            print(line)

    @staticmethod
    def snailfish_add(
        first: SnailfishNumber, second: SnailfishNumber
    ) -> SnailfishNumber:
        return SnailfishPair(second, first)

    @staticmethod
    def make_snailfish_number(number_input) -> SnailfishNumber:
        if type(number_input) == str:
            number = literal_eval(number_input)
        else:
            number = number_input
        if type(number) == int:
            return SnailfishInt(int(number))
        elif type(number) == list:
            return SnailfishPair(
                SnailfishMath.make_snailfish_number(number[0]),
                SnailfishMath.make_snailfish_number(number[1]),
            )

    @staticmethod
    def sfstring_to_sflist(string_input) -> SnailfishNumber:
        return literal_eval(string_input)


    @staticmethod
    def sflist_to_sfstring(list_input: int) -> str:
        pass

    @staticmethod
    def reduce(number: SnailfishNumber, depth: int = 0) -> SnailfishNumber:
        pass


if __name__ == "__main__":
    # input_file = "../inputs/18/data.input"
    input_file = "../inputs/18/data.example"
    input_data: list[str] = file_to_list(input_file)

    stringnumber = "[1,[3,4]]"
    print(SnailfishMath.make_snailfish_number(stringnumber).magnitude)
