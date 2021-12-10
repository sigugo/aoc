from tools import *
from dataclasses import dataclass, field


class SyntaxParser:
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
        debug: int = 0,
    ):
        self._command_strings: list[str] = []
        self._ocmap: dict[str, str] = character_pairs
        self._comap: dict[str, str] = {}
        for k, v in self._ocmap.items():
            self._comap[v] = k
        if input_data:
            self.parse_input(input_data)
        self._illegal_character_scores = illegal_character_scores
        self._log_level = debug

    def parse_input(self, input_data: list[str]) -> None:
        for line in input_data:
            self._command_strings.append(line.strip())

    def get_error_score(self) -> int:
        error_score = 0
        for entry in self._command_strings:
            error_score += self._get_syntax_error(str(entry))
        return error_score

    def _get_syntax_error(self, cmd: str) -> int:
        no_error = 0
        expected_closers: str = ""
        if self._log_level > 0:
            print("Parsing command", cmd)
        for char in cmd:
            if self._log_level > 1:
                print("=> Current Character:", char)
            if self._is_opener(char):
                expected_closers = self._get_matching_closer(char) + expected_closers
            else:
                if expected_closers[0] == char:
                    expected_closers = expected_closers[1:]
                else:
                    return self._illegal_character_scores[char]
        return no_error

    def _is_opener(self, char: str) -> bool:
        try:
            if list(self._ocmap.keys()).index(char) >= 0:
                return True
        except ValueError:
            return False

    def _get_matching_closer(self, opener: str) -> str:
        return self._ocmap[opener]

    def _get_matching_opener(self, closer: str) -> str:
        return self._comap[closer]


if __name__ == "__main__":
    input_file = "../inputs/10/data.input"
    # input_file = "../inputs/10/data.example"
    # input_file = "../inputs/10/data.example2"
    input_data: list[str] = file_to_list(input_file)
    parser = SyntaxParser(input_data)
    print(parser.get_error_score())
