from functools import cache
from tools import file_to_list

WINNING_SCORE: int = 21
DICE_SIDES: int = 3

dice_combinations = []
for i in range(1, DICE_SIDES + 1):
    for j in range(1, DICE_SIDES + 1):
        for k in range(1, DICE_SIDES + 1):
            dice_combinations.append((i+j+k)%10)
dice_combinations.sort()

@cache
def recurse_turn(p0: int, s0: int, p1: int, s1: int) -> tuple[int, int]:
    
    if s1 >= WINNING_SCORE:
        return (0, 1)
    
    score0, score1 = 0, 0
    
    for roll in dice_combinations:
        pn = p0 + roll 
        if pn > 10:
            pn %= 10
        sn = s0 + pn
        res1, res0 = recurse_turn(p1, s1, pn, sn)
        score0 += res0
        score1 += res1
    return score0, score1


def main() -> None:
    # data = file_to_list("../inputs/21/data.input")
    data = file_to_list("../inputs/21/data.example")

    t = recurse_turn(int(data[0][-1]), 0, int(data[1][-1]), 0)
    print(t)
    print(max(t))


if __name__ == "__main__":
    main()
