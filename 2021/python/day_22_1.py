from tools import file_to_list
from typing import NamedTuple


MIN_AXIS: int = -50
MAX_AXIS: int = 50
ON_COMMAND: str = "on"


class Point(NamedTuple):
    x: int
    y: int
    z: int


class Command(NamedTuple):
    on: bool
    xrange: list[int]
    yrange: list[int]
    zrange: list[int]

    @classmethod
    def from_str(cls, data: str):
        command, coordranges = data.split(" ")
        xmm, ymm, zmm = [
            sorted(
                [
                    int(coordrange[2:].split("..")[0]),
                    int(coordrange[2:].split("..")[1]),
                ]
            )
            for coordrange in coordranges.split(",")
        ]
        return cls(
            True if command == ON_COMMAND else False,
            [x for x in range(xmm[0], xmm[1] + 1)],
            [y for y in range(ymm[0], ymm[1] + 1)],
            [z for z in range(zmm[0], zmm[1] + 1)],
        )

    def get_points_set(self):
        result = set()
        for x in self.xrange:
            for y in self.yrange:
                for z in self.zrange:
                    result.add(Point(x, y, z))
        return result


core_points: list[Point] = []

for x in range(MIN_AXIS, MAX_AXIS + 1):
    for y in range(MIN_AXIS, MAX_AXIS + 1):
        for z in range(MIN_AXIS, MAX_AXIS + 1):
            core_points.append(Point(x, y, z))


def main() -> None:
    data = file_to_list("../inputs/22/data.input")
    # data = file_to_list("../inputs/22/data.example")
    core = set()
    commands = []
    for line in data:
        commands.append(Command.from_str(line.strip()))
    print("Command count:", len(commands))
    for i, command in enumerate(commands):
        print("Processing Command", i)
        command_points = command.get_points_set()
        for core_point in core_points:
            if core_point in command_points:
                if command.on:
                    core.add(core_point)
                else:
                    core.discard(core_point)

    return len(core)


if __name__ == "__main__":
    main()
