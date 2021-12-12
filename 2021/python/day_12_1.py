from tools import *


class CavePathsMap:
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

        for k, v in self._caves.items():
            print(k, "connects to", v)
        self.find_pathes()
        for path in self._paths:
            print(path)
        print(len(self._paths))

    def find_pathes(self) -> None:
        caves = self._caves.copy()
        start_caves = caves.pop(self._start)
        for first_cave in start_caves:
            self._walk_path(first_cave, [], caves.copy())

    def _walk_path(
        self,
        current_cave: str,
        previous_caves: list[str],
        caves_to_explore: dict[list[str]],
    ):
        if current_cave == self._end:
            self._paths.append(previous_caves.append(current_cave))
        else:
            if current_cave.islower():
                next_caves = caves_to_explore.pop(current_cave)
                for cave, destinations in caves_to_explore.items():
                    if current_cave in destinations:
                        caves_to_explore[cave].remove(current_cave)
            else:
                next_caves = caves_to_explore[current_cave]
            for cave in next_caves:
                self._walk_path(current_cave, previous_caves, caves_to_explore.copy())


if __name__ == "__main__":
    # input_file = "../inputs/12/data.input"
    input_file = "../inputs/12/data.example"
    input_data: list[str] = file_to_list(input_file)
    map = CavePathsMap(input_data)
