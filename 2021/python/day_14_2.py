from tools import *
from copy import deepcopy


class MoleculeBuilder:
    def __init__(self, input_data: list[str] = []):
        self._polymer: dict[str, int] = {}
        self._counts: dict[str, int] = {}
        self._rules: dict[str, str] = {}

        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input_data: list[str]):
        replace_separator = " -> "
        polymer = input_data[0].strip()
        for i in range(len(polymer)):
            self._counts[polymer[i]] = self._counts.get(polymer[i], 0) + 1
            if i > 0:
                self._polymer[polymer[i - 1] + polymer[i]] = (
                    self._polymer.get(polymer[i - 1] + polymer[i], 0) + 1
                )
        for line in input_data[2:]:
            k, v = line.split(replace_separator)
            self._rules[k] = v

    def run_inserts(self, steps_count: int = 40):
        for i in range(steps_count):
            self._perform_insert()

    def _perform_insert(self) -> None:
        new_polymer = deepcopy(self._polymer)
        for pair, insert in self._rules.items():
            if pair in list(self._polymer.keys()) and self._polymer[pair] > 0:
                new_polymer[pair[0] + insert] = (
                    new_polymer.get(pair[0] + insert, 0) + self._polymer[pair]
                )
                new_polymer[insert + pair[1]] = (
                    new_polymer.get(insert + pair[1], 0) + self._polymer[pair]
                )
                self._counts[insert] = self._counts.get(insert, 0) + self._polymer[pair]
                new_polymer[pair] -= self._polymer[pair]
        self._polymer = deepcopy(new_polymer)

    def get_polymer_score(self) -> int:
        counts: list[tuple[int, str]] = []
        for k, v in self._counts.items():
            counts.append(tuple((v, k)))
        counts.sort()
        return counts[-1][0] - counts[0][0]

    def __str__(self) -> str:
        output = ""
        for char, count in self._counts.items():
            output += char + ": " + str(count) + "\n"
        return output


if __name__ == "__main__":
    input_file = "../inputs/14/data.input"
    # input_file = "../inputs/14/data.example"
    data: list[str] = file_to_list(input_file)
    polymer_molecule = MoleculeBuilder(data)
    polymer_molecule.run_inserts(40)
    print(polymer_molecule)
    print(polymer_molecule.get_polymer_score())
