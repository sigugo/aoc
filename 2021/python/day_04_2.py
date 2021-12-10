from tools import *
from day_04_1 import BingoGame


class LosingBingoGame(BingoGame):
    def __init__(self, board_size: int = 5):
        super(LosingBingoGame, self).__init__(board_size)

    def last_winner_score(self) -> int:
        while True:
            if self._draw_index >= len(self._draws):
                return -1
            else:
                self.next_draw()
                if self.isolate_last_board():
                    return self.draw_until_game_end()

    def isolate_last_board(self):
        c = 0
        board_count = len(self._boards)
        last_board_index = 0
        for i in range(board_count):
            if self._boards[i].get_value() > 0:
                c += 1
            else:
                last_board_index = i
        if c == len(self._boards) - 1:
            last_board = self._boards[last_board_index]
            self._boards = []
            self._boards.append(last_board)
            return True
        return False


if __name__ == "__main__":
    input_file = "../inputs/04/input.txt"
    input_data = file_to_list(input_file)

    game = LosingBingoGame()
    game.parse_game_data(input_data)

    print(game.last_winner_score())
