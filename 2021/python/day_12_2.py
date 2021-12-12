from tools import *
from dataclasses import dataclass, field
from copy import deepcopy
import day_12_1


@dataclass
class CavePathMapper(day_12_1.CavePathMapper):
    revisit_allowed: bool


class CaveSystem(day_12_1.CaveSystem):
    def __init__(self, input_data: list[str] = []):
        self._revisit_allowed: bool = True
        super(CaveSystem, self).__init__(input_data)

    def parse_input(self, input_data: list[str]) -> None:
        split_char = "-"
        for line in input_data:
            a, b = line.strip().split(split_char)
            if a != self._end and b != self._start:
                self._caves.setdefault(a, []).append(b)
            if b != self._end and a != self._start:
                self._caves.setdefault(b, []).append(a)
        self._walk_paths()
        paths: list[str] = []
        for path in self._paths:
            paths.append(",".join(path))
        paths = list(dict.fromkeys(paths))
        paths.sort()
        self._paths = []
        for path in paths:
            self._paths.append(path.split(","))

    def _walk_paths(self, log_level: int = 0):
        caves: list[CavePathMapper] = [
            CavePathMapper(
                self._start, deepcopy(self._caves), [self._start], self._revisit_allowed
            ),
        ]
        keep_walking = True
        while keep_walking:
            keep_walking = False
            temp_caves: list[CavePathMapper] = []
            for cave in caves:
                if log_level > 0:
                    print("\n## Current Cave")
                    print(" YOU ARE HERE:", cave.marker)
                    print(" Visited:", cave.result)
                    print(" Revisit allowed:", cave.revisit_allowed)
                    print(" Location Map:")
                    for k, v in list(cave.dataset.items()):
                        print("  ", k, "=>", v)
                if cave.marker == self._end:
                    temp_caves.append(cave)
                else:
                    keep_walking = True
                    if cave.marker.islower():
                        if (
                            cave.revisit_allowed
                            and cave.marker != self._start
                            and cave.marker != self._end
                        ):
                            next_caves = cave.dataset[cave.marker]
                            if len(next_caves) > 0:
                                for next_cave in next_caves:
                                    next_visited_locations: list[str] = deepcopy(
                                        cave.result
                                    ) + [next_cave]
                                    temp_caves.append(
                                        CavePathMapper(
                                            next_cave,
                                            deepcopy(cave.dataset),
                                            next_visited_locations,
                                            False,
                                        )
                                    )
                        if log_level > 0:
                            print(
                                " - removing",
                                cave.marker,
                                "with repeat",
                                cave.revisit_allowed,
                            )
                        next_caves = cave.dataset.pop(cave.marker)
                        for k in cave.dataset.keys():
                            if cave.marker in cave.dataset[k]:
                                cave.dataset[k].remove(cave.marker)
                        if log_level > 0:
                            print(" New Location Map:", type(cave.dataset))
                            for k1, v1 in list(cave.dataset.items()):
                                print("  ", k1, "=>", v1)
                    else:
                        next_caves = cave.dataset[cave.marker]
                        if log_level > 0:
                            print(" Available Destinations:", next_caves)
                    if len(next_caves) > 0:
                        for next_cave in next_caves:
                            next_visited_locations: list[str] = deepcopy(
                                cave.result
                            ) + [next_cave]
                            temp_caves.append(
                                CavePathMapper(
                                    next_cave,
                                    deepcopy(cave.dataset),
                                    next_visited_locations,
                                    deepcopy(cave.revisit_allowed),
                                )
                            )
            caves = deepcopy(temp_caves)
        for cave in caves:
            self._paths.append(cave.result)


if __name__ == "__main__":
    input_file = "../inputs/12/data.input"
    # input_file = "../inputs/12/data.example"
    input_data: list[str] = file_to_list(input_file)
    cave_system = CaveSystem(input_data)
    print(cave_system.get_path_count())
