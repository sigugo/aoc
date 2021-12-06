from tools import *


class SchoolOfFish:
    def __init__(self):
        self._spawn_timer: int = 6
        self._mature_delta: int = 2
        self._swarm: list[int] = [0] * (self._spawn_timer + self._mature_delta + 1)

    def parse_input_data(self, input_data: list[str]):
        for value in input_data.strip().split(","):
            self._swarm[int(value)] += 1

    def count_fish(self) -> None:
        count: int = 0
        for i in range(len(self._swarm)):
            count += self._swarm[i]
        return count

    def advance_day(self, days: int = 1) -> None:
        for d in range(days):
            self._next_day()

    def _next_day(self) -> None:
        spawn_timer_zero_count: int = 0
        for i in range(len(self._swarm)):
            if i == 0:
                spawn_timer_zero_count = self._swarm[i]
            else:
                self._swarm[i - 1] = self._swarm[i]
        self._swarm[self._spawn_timer] += spawn_timer_zero_count
        self._swarm[self._spawn_timer + self._mature_delta] = spawn_timer_zero_count

    def __str__(self) -> str:
        output: str = ""
        for i in range(len(self._swarm)):
            marker: str = ""
            if i == 0:
                marker = "."
            elif i == self._spawn_timer:
                marker = "|"
            elif i == self._spawn_timer + 1:
                marker = "+"
            output += marker + str(self._swarm[i]) + marker + " "
        return output


if __name__ == "__main__":
    input_file = "../inputs/6/input.txt"
    # input_file = "../inputs/6/example.txt"
    input_data: list[str] = file_to_list(input_file)
    lanternfish_school = SchoolOfFish()
    lanternfish_school.parse_input_data(input_data[0])
    lanternfish_school.advance_day(256)
    print(lanternfish_school.count_fish())

