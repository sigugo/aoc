from tools import *


class BingoGame:
    def __init__(self, board_size: int = 5):
        self._draws: list[int] = []
        self._boards: list[BingoBoard] = []
        self._draw_index: int = 0
        self._board_size: int = board_size

    def parse_game_data(self, bingo_data: list[str]) -> None:
        self.parse_draw_data(bingo_data[0])
        self.parse_boards_data(bingo_data[1:])

    def parse_draw_data(self, draw_data: str, separator: str = ',') -> None:
        for draw in draw_data.strip().split(separator):
            self.add_draw(int(draw))

    def add_draw(self, draw: int):
        self._draws.append(draw)

    def parse_boards_data(self, boards_data: list[str], separator=' ') -> None:
        board_data: list[list[str]] = []
        for line in boards_data:
            if not line == "":
                board_data.append(compress_spaces(line).split(separator))
                if len(board_data) == self._board_size:
                    board: BingoBoard = BingoBoard()
                    board.add_board_data(board_data)
                    self._boards.append(board)
                    board_data = []

    def draw_until_game_end(self) -> int:
        while True:
            if self._draw_index >= len(self._draws):
                break
            else:
                draw = self.next_draw()
                if draw > 0:
                    return draw

    def next_draw(self) -> int:
        results: list[int] = []
        for i in range(len(self._boards)):
            results.append(self._boards[i].add_draw(self._draws[self._draw_index]))
        max_score = 0
        for score in results:
            if score > max_score:
                max_score = score
        self._draw_index += 1
        return max_score
    
    def __str__(self) -> str:
        output = '================================================\n'
        for board in self._boards:
            output += str(board) + '\n'
        return output


class BingoBoard:
    def __init__(self, size: int = 5):
        self._size = 5
        self._board: list[list[tuple[int, bool]]] = []
        self._value: int = 0
        self._current_draw: int = 0

    def add_board_data(self, board_data: list[list[str]]) -> None:
        for horizontal_values in board_data:
            horizontal_data: list[tuple[int, bool]] = []
            for value in horizontal_values:
                horizontal_data.append((int(value), False))
            self._board.append(horizontal_data)

    def add_draw(self, draw: int) -> int:
        self._current_draw = draw
        for v in range(self._size):
            for h in range(self._size):
                if self._board[v][h][0] == self._current_draw:
                    self._board[v][h] = (self._current_draw, True)
                    return self._check_winner()
        return self._value

    def _check_winner(self) -> int:
        for v in range(self._size):
            is_winner = True
            for h in range(self._size):
                if not self._board[v][h][1]:
                    is_winner = False
            if is_winner:
                self._value = self._calculate_points()
        for h in range(self._size):
            is_winner = True
            for v in range(self._size):
                if not self._board[v][h][1]:
                    is_winner = False
            if is_winner:
                self._value = self._calculate_points()
        return self._value

    def _calculate_points(self) -> int:
        points = 0
        for v in range(self._size):
            for h in range(self._size):
                if not self._board[v][h][1]:
                    points += self._board[v][h][0]
        return points * self._current_draw

    def get_value(self) -> int:
        return self._value

    def __str__(self) -> str:
        output = ""
        for line in self._board:
            for entry in line:
                padding = " "
                if entry[1]:
                    padding = "|"
                output += padding + '{0:02d}'.format(entry[0]) + padding + " "
            output += '\n';
        return output


if __name__ == '__main__':
    input_file = '../inputs/4/input.txt'
    # input_file = '../inputs/4/example.txt'
    input_data: list[str] = file_to_list(input_file)
    game = BingoGame()
    game.parse_game_data(input_data)
    print(game.draw_until_game_end())
    # print(game)
