from tools import file_to_list
from typing import NamedTuple

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

    def in_field(self, p: Point) -> bool:
        return (
            self.xrange[0] <= p.x <= self.xrange[1]
            and self.yrange[0] <= p.y <= self.yrange[1]
            and self.zrange[0] <= p.z <= self.zrange[1]
        )

    def overlaps(self, other) -> bool:
        if (
            self.xrange[0] <= other.xrange[0] <= self.xrange[1]
            and self.yrange[0] <= other.yrange[0] <= self.yrange[1]
            and self.zrange[0] <= other.zrange[0] <= self.zrange[1]
        ) or (
            self.xrange[0] <= other.xrange[1] <= self.xrange[1]
            and self.yrange[0] <= other.yrange[1] <= self.yrange[1]
            and self.zrange[0] <= other.zrange[1] <= self.zrange[1]
        ):
            return True
        return False

    @property
    def pointlist(self) -> list[Point]:
        points: list[Point] = []
        print("Generating Point List")
        for x in range(self.xrange[0], self.xrange[1] + 1):
            for y in range(self.yrange[0], self.yrange[1] + 1):
                for z in range(self.zrange[0], self.zrange[1] + 1):
                    points.append(Point(x, y, z))
        print("Generating Point List Done")
        return points


class SpacePartition(NamedTuple):
    commands: list[Command]

    def overlaps_any(self, other: Command) -> bool:
        for command in self.commands:
            if command.overlaps(other):
                return True
        return False

    def overlaps_all(self, other: Command) -> bool:
        for command in self.commands:
            if not command.overlaps(other):
                return False
        return True

    def append(self, cmd: Command) -> None:
        self.commands.append(cmd)

    @property
    def size(self) -> int:
        return len(self.commands)


def main() -> None:
    data = file_to_list("../inputs/22/data.input")
    # data = file_to_list("../inputs/22/data.example")

    commands: list[Command] = []
    for line in data:
        commands.append(Command.from_str(line.strip()))

    partitions: list[SpacePartition] = [SpacePartition([commands[0]])]
    commands = commands[1:]

    while len(commands) > 0:
        current_command = commands[0]
        commands = commands[1:]
        for i, partition in enumerate(partitions):
            if current_command and partition.overlaps_any(current_command):
                partitions[i].append(current_command)
                current_command = None
        if current_command:
            partitions += [SpacePartition([current_command])]

    print("Partition Count:", len(partitions))

    oncount: int = 0

    for i, partition in enumerate(partitions):
        print("Partition Index:", i)
        points = set()
        for command in partition.commands:
            for point in command.pointlist:
                if command.on:
                    points.add(point)
                else:
                    points.discard(point)
        partition_oncount = len(points)
        print("Cubes on current:", partition_oncount)
        oncount += partition_oncount
        print("Cubes on total:", oncount)

    print(oncount)


if __name__ == "__main__":
    main()
