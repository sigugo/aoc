from tools import *
from dataclasses import dataclass, field
from copy import deepcopy


@dataclass
class CavePathMapper:
    marker: str
    dataset: field(default_factory=dict[str, list[str]])
    result: field(default_factory=list[str])


class CaveSystem:
    def __init__(self, input_data: list[str] = []):
        self._caves: dict[str, list[str]] = {}
        self._paths: list[list[str]] = []
        self._start = "start"
        self._end = "end"
        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input_data: list[str]) -> None:
        split_char = "-"
        for line in input_data:
            a, b = line.strip().split(split_char)
            if a != self._end and b != self._start:
                self._caves.setdefault(a, []).append(b)
            if b != self._end and a != self._start:
                self._caves.setdefault(b, []).append(a)
        self._walk_paths()
        self._paths.sort()

    def _walk_paths(self, log_level: int = 0):
        caves: list[CavePathMapper] = [
            CavePathMapper(self._start, deepcopy(self._caves), [self._start]),
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
                    print(" Location Map:", type(cave.dataset))
                    for k, v in list(cave.dataset.items()):
                        print("  ", k, "=>", v)
                if cave.marker == self._end:
                    temp_caves.append(cave)
                else:
                    keep_walking = True
                    if cave.marker.islower():
                        if log_level > 0:
                            print(" - removing", cave.marker)
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
                                )
                            )
            caves = deepcopy(temp_caves)
        for cave in caves:
            self._paths.append(cave.result)

    def get_path_count(self) -> int:
        return len(self._paths)

    def __str__(self) -> str:
        output = ""
        for path in self._paths:
            line = ""
            for cave in path:
                line += cave + ","
            output += line[:-1] + "\n"
        return output


if __name__ == "__main__":
    # input_file = "../inputs/12/data.input"
    input_file = "../inputs/12/data.example"
    input_data: list[str] = file_to_list(input_file)
    cave_system = CaveSystem(input_data)
    print(cave_system.get_path_count())
