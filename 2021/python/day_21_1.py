from tools import *
from dataclasses import dataclass


@dataclass
class DeterministicDice:
    value: int = 0
    rolls: int = 0

    def roll(self) -> int:
        self.value += 1
        self.rolls += 1
        if self.value > 100:
            self.value = 1
        return self.value


@dataclass
class Player:
    position: int
    score: int = 0

    def move(self, count: int) -> None:
        move = count % 10
        self.position = (
            self.position + move - 10
            if self.position + move > 10
            else self.position + move
        )
        self.score += self.position


class Game:
    def __init__(self):
        self._dice = DeterministicDice()
        self._players: list[Player] = []
        self._rolls_per_turn: int = 3
        self._winning_score = 1000

    def add_player(self, player: Player) -> None:
        self._players.append(player)

    def play(self) -> int:
        last_score: int = 0
        while True:
            for i in range(len(self._players)):
                player_turn_moves: int = 0
                for _ in range(self._rolls_per_turn):
                    player_turn_moves += self._dice.roll()
                self._players[i].move(player_turn_moves)
                if self._players[i].score >= self._winning_score:
                    print("Rolls:", self._dice.rolls)
                    return last_score * self._dice.rolls
                last_score = self._players[i].score


def main() -> None:
    game = Game()
    game.add_player(Player(7))
    game.add_player(Player(3))
    print(game.play())
    # game.one_round()
    # game.one_round()
    # game.one_round()
    # game.one_round()


if __name__ == "__main__":
    main()
