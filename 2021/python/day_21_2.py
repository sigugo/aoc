from tools import *
from dataclasses import dataclass
from copy import deepcopy
import sys

sys.setrecursionlimit(1000)


@dataclass
class Player:
    position: int
    name: str
    score: int = 0

    def move(self, count: int) -> None:
        move = count % 10
        self.position = (
            self.position + move - 10
            if self.position + move > 10
            else self.position + move
        )
        self.score += self.position
        if self.score >= 31:
            print("THIS IS WRONG, Player", self.name, "has score", self.score)


def recurse_turn(
    players: list[Player], roll: int = 0, active_player: int = 1, depth=0
) -> tuple[int, int]:
    winning_score = 21
    dice_sides: int = 3
    if roll > 0:
        players[active_player].move(roll)

    if players[active_player].score >= winning_score:
        return (1, 0) if active_player == 0 else (0, 1)
    else:
        score0, score1 = 0, 0
        active_player = 1 if active_player == 0 else 0
        for i in range(1, dice_sides + 1):
            for j in range(1, dice_sides + 1):
                for k in range(1, dice_sides + 1):
                    res0, res1 = recurse_turn(
                        deepcopy(players), i + j + k, active_player, depth + 1
                    )
                    score0 += res0
                    score1 += res1
        return score0, score1


def main() -> None:
    print(recurse_turn([Player(4, "One"), Player(8, "Two")]))


if __name__ == "__main__":
    main()
