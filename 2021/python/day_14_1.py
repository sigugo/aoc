from tools import *
from copy import deepcopy


class MoleculeBuilder:
    def __init__(self, input_data: list[str] = []):
        self._polymer: str = ""
        self._insert_rules: dict[str, str] = {}

        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input_data: list[str]):
        replace_separator = " -> "
        self._polymer = input_data[0].strip()
        for line in input_data[2:]:
            k, v = line.split(replace_separator)
            self._insert_rules[k] = v

    def run_inserts(self, steps_count: int = 10):
        polymer = deepcopy(self._polymer)
        for _ in range(steps_count):
            polymer = self._perform_insert(polymer)
        self._polymer = polymer

    def _perform_insert(self, polymer: str) -> str:
        next_polymer = ""
        for i in range(len(polymer)):
            if i == 0:
                next_polymer += polymer[i]
            else:
                pair = polymer[i - 1] + polymer[i]
                if pair in self._insert_rules.keys():
                    next_polymer += self._insert_rules[pair]
                next_polymer += polymer[i]
        return next_polymer

    def get_polymer_score(self) -> int:
        counts = character_counts(self._polymer)
        return counts[-1][0] - counts[0][0]

    def __str__(self) -> str:
        return self._polymer


if __name__ == "__main__":
    input_file = "../inputs/14/data.input"
    # input_file = "../inputs/14/data.example"
    input_data: list[str] = file_to_list(input_file)
    polymer = MoleculeBuilder(input_data)
    polymer.run_inserts()
    print(polymer.get_polymer_score())
