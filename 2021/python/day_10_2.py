from tools import *
import day_10_1
from math import ceil


class SyntaxParser(day_10_1.SyntaxParser):
    def __init__(
        self,
        input_data: list[str] = [],
        character_pairs: dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"},
        illegal_character_scores: dict[str, int] = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137,
        },
        autocomplete_scores: dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4},
        debug: int = 0,
    ):
        super(SyntaxParser, self).__init__(
            input_data, character_pairs, illegal_character_scores, debug
        )
        self._autocomplete_scores = autocomplete_scores

    def get_autocomplete_score(self) -> int:
        complete_scores: list[int] = []
        for entry in self._get_autocompletes():
            complete_scores.append(self._get_autocomplete_value(entry))
        complete_scores.sort()
        score_index = ceil(len(complete_scores) / 2) - 1
        return complete_scores[score_index]

    def _get_autocomplete_value(self, autocomplete: str) -> int:
        score = 0
        for c in autocomplete:
            score *= 5
            score += self._autocomplete_scores[c]
        return score

    def _get_autocompletes(self) -> list[str]:
        autocompletes: list[str] = []
        for command in self._command_strings:
            if self._get_syntax_error(command) == 0:
                autocompletes.append(self._get_autocomplete_for_valid_command(command))
        return autocompletes

    def _get_autocomplete_for_valid_command(self, cmd: str) -> list[str]:
        openers: str = ""
        expected_closers: str = ""
        if self._log_level > 0:
            print("Parsing command", cmd)
        for char in cmd:
            if self._log_level > 1:
                print("=> Current Character:", char)
            if self._is_opener(char):
                openers += char
                expected_closers = self._get_matching_closer(char) + expected_closers
            else:
                i = expected_closers.find(char)
                expected_closers = expected_closers[:i] + expected_closers[i + 1 :]
        return expected_closers


if __name__ == "__main__":
    input_file = "../inputs/10/data.input"
    # input_file = "../inputs/10/data.example"
    # input_file = "../inputs/10/data.example2"
    input_data: list[str] = file_to_list(input_file)
    parser = SyntaxParser(input_data)
    print(parser.get_autocomplete_score())
