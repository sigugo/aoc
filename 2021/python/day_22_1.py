from tools import file_to_list
from typing import NamedTuple
from functools import cache

MIN_AXIS: int = -50
MAX_AXIS: int = 50
ON_COMMAND: str = "on"


class Point(NamedTuple):
    x: int
    y: int
    z: int


class Command(NamedTuple):
    on: bool
    xrange: tuple[int, int]
    yrange: tuple[int, int]
    zrange: tuple[int, int]

    @classmethod
    @cache
    def from_str(cls, data: str):
        command, coordranges = data.split(" ")

        return cls(
            True if command == ON_COMMAND else False,
            *[ 
                tuple(
                    sorted(
                        [
                            int(coordrange[2:].split("..")[0]),
                            int(coordrange[2:].split("..")[1]),
                        ]
                    )
                )
                for coordrange in coordranges.split(",")
            ],
        )

    @cache
    def in_field(self, p: Point) -> bool:
        return (
            self.xrange[0] <= p.x <= self.xrange[1]
            and self.yrange[0] <= p.y <= self.yrange[1]
            and self.zrange[0] <= p.z <= self.zrange[1]
        )


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
        for core_point in core_points:
            if command.in_field(core_point):
                if command.on:
                    core.add(core_point)
                else:
                    core.discard(core_point)

    return len(core)


if __name__ == "__main__":
    main()
