from tools import *
from enum import Enum
from copy import deepcopy


class Field(str, Enum):
    EMPTY = "."
    EAST = ">"
    SOUTH = "v"


class Cucumbers:
    def __init__(self, input_data: list[str] = []):
        self._map: list[list[str]] = []
        self._steps: int = 0

        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input_data: list[str]):
        print("Parsing")
        for line in input_data:
            self._map.append(list(line))
        print("Done Parsing")

    def _check_to(self, x: int, y: int):
        if y >= len(self._map):
            y = 0
        if x >= len(self._map[y]):
            x = 0
        return self._map[y][x]

    def _move_to(self, x: int, y: int, xn: int, yn: int) -> bool:
        if yn >= len(self._map):
            yn = 0
        if xn >= len(self._map[y]):
            xn = 0
        self._map[yn][xn] = self._map[y][x]
        self._map[y][x] = Field.EMPTY

    def __str__(self) -> str:
        out = ""
        for row in self._map:
            outrow = ""
            for c in row:
                outrow += c
            out += outrow + "\n"
        return out

    def _move(self) -> int:
        self._steps += 1
        print(self)
        move_count: int = 0

        moves = set()
        for y, xrow in enumerate(self._map):
            for x, value in enumerate(xrow):
                if self._map[y][x] == Field.EAST:
                    if self._check_to(x + 1, y) == Field.EMPTY:
                        moves.add((x, y))
        for x, y in moves:
            self._move_to(x, y, x + 1, y)
        move_count += len(moves)

        moves = set()
        for y, xrow in enumerate(self._map):
            for x, value in enumerate(xrow):
                if self._map[y][x] == Field.SOUTH:
                    if self._check_to(x, y + 1) == Field.EMPTY:
                        moves.add((x, y))
        for x, y in moves:
            self._move_to(x, y, x, y + 1)
        move_count += len(moves)

        return move_count

    def get_last_move(self) -> int:
        print("Move Counter Start")
        while True:
            if self._move() == 0:
                break
        return self._steps


def main() -> None:
    input_file = "../inputs/25/data.input"
    input_data: list[str] = file_to_list(input_file)
    cucumbers = Cucumbers(input_data)
    print(cucumbers.get_last_move())


if __name__ == "__main__":
    main()
