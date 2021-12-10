from tools import *


class SchoolOfFish:
    def __init__(self):
        self._swarm: list[int] = []
        self._spawn_timer: int = 6
        self._initial_spawn_delta: int = 2

    def parse_input_data(self, input_data: list[str]):
        input_strings: list[str] = []
        for line in input_data:
            input_strings.extend(line.strip().split(","))
        for entry in input_strings:
            self._swarm.append(int(entry))

    def count_fish(self) -> None:
        return len(self._swarm)

    def advance_day(self, days: int = 1):
        for d in range(days):
            self._next_day()

    def _next_day(self) -> None:
        new_fish: list[int] = []
        for i in range(len(self._swarm)):
            self._swarm[i] -= 1
            if self._swarm[i] < 0:
                new_fish.append(self._spawn_timer + self._initial_spawn_delta)
                self._swarm[i] = self._spawn_timer
        self._swarm.extend(new_fish)


if __name__ == "__main__":
    input_file = "../inputs/06/input.txt"
    # input_file = "../inputs/06/example.txt"
    input_data: list[str] = file_to_list(input_file)
    lanternfish_school = SchoolOfFish()
    lanternfish_school.parse_input_data(input_data)
    lanternfish_school.advance_day(80)
    print(lanternfish_school.count_fish())
