from tools import *


class LargeSchoolOfFish:
    def __init__(self):
        self._swarm: dict[int, int] = {}

        self._spawn_timer: int = 6
        self._initial_spawn_delta: int = 2
        self._init_swarm()

    def _init_swarm(self):
        for i in range(self._spawn_timer + self._initial_spawn_delta + 1):
            self._swarm[i] = 0

    def parse_input_data(self, input_data: list[str]):
        input_strings: list[str] = []
        for line in input_data:
            input_strings.extend(line.strip().split(","))
        for entry in input_strings:
            self._swarm[int(entry)] += 1

    def count_fish(self) -> None:
        count: int = 0
        for value in self._swarm.values():
            count += value
        return count

    def advance_day(self, days: int = 1):
        for d in range(days):
            self._next_day()

    def _next_day(self) -> None:
        last_swarm = self._swarm.copy()
        spawns: int = 0
        self._init_swarm()

        for i in range(self._spawn_timer + self._initial_spawn_delta + 1):
            if i == 0:
                spawns = last_swarm[i]
            else:
                self._swarm[i - 1] += last_swarm[i]

        self._swarm[self._spawn_timer] += spawns
        self._swarm[self._spawn_timer + self._initial_spawn_delta] = spawns


if __name__ == "__main__":
    input_file = "../inputs/6/input.txt"
    # input_file = "../inputs/6/example.txt"
    input_data: list[str] = file_to_list(input_file)
    lanternfish_school = LargeSchoolOfFish()
    lanternfish_school.parse_input_data(input_data)
    print(lanternfish_school._swarm)
    lanternfish_school.advance_day(256)
    print(lanternfish_school.count_fish())
