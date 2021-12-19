from tools import *
from math import floor, ceil
from ast import literal_eval
import re


def sfadd(first: str, second: str) -> str:
    return "[{0},{1}]".format(first, second)


def sfmagnitude(input) -> int:
    if type(input) == str:
        return sfmagnitude(literal_eval(input))
    elif type(input) == list:
        return sfmagnitude(input[0]) * 3 + sfmagnitude(input[1]) * 2
    elif type(input) == int:
        return input
    else:
        raise (ValueError)


def sfreduce(sfnum: str) -> str:
    sfreplaced = None
    while not sfreplaced == sfnum:
        sfreplaced = sfexplode(sfnum)
        if sfreplaced != sfnum:
            sfnum, sfreplaced = sfreplaced, sfnum
        else:
            sfreplaced = sfsplit(sfnum)
            if sfreplaced != sfnum:
                sfnum, sfreplaced = sfreplaced, sfnum
    return sfnum


def sfsplit(sfnum: str) -> str:
    match = re.search("\d\d+", sfnum)
    if match:
        num = int(match.group(0)) / 2
        return sfnum.replace(match.group(0), sfadd(str(floor(num)), str(ceil(num))), 1)
    return sfnum


def sfexplode(sfnum: str) -> str:
    index, count, opener, closer = 0, 0, "[", "]"
    while index < len(sfnum):
        if sfnum[index] == opener:
            count += 1
        elif sfnum[index] == closer:
            count -= 1
        if count > 4:
            while sfnum[index + 1] == opener:
                count += 1
                index += 1
            closer_index = sfnum[index:].find(closer) + index
            sfnum_match = sfnum[index + 1 : closer_index].split(",")
            if len(sfnum_match) == 2:
                before, after = sfnum[:index], sfnum[closer_index + 1 :]
                left, right = int(sfnum_match[0]), int(sfnum_match[1])
                match = re.search("\d+", after)
                if match:
                    after = after.replace(
                        match.group(0), str(right + int(match.group(0))), 1
                    )
                reversed_before = before[::-1]
                match = re.search("\d+", reversed_before)
                if match:
                    reversed_before = reversed_before.replace(
                        match.group(0), str(left + int(match.group(0)[::-1]))[::-1], 1
                    )
                sfnum = reversed_before[::-1] + str(0) + after
                break
            else:
                index = closer_index - 1
        index += 1
    return sfnum


def main() -> None:
    # input_file = "../inputs/18/data.example"
    input_file = "../inputs/18/data.input"
    input_data: list[str] = file_to_list(input_file)
    data = []
    for line in input_data:
        data.append(sfreduce(line.strip()))
    maxsfmagnitude = 0
    for i in range(len(data)):
        for j in range(i+1,len(data)):
                result = sfmagnitude(sfreduce(sfadd(data[i],data[j])))
                if result > maxsfmagnitude:
                    maxsfmagnitude = result
                result = sfmagnitude(sfreduce(sfadd(data[j],data[i])))
                if result > maxsfmagnitude:
                    maxsfmagnitude = result
    print(maxsfmagnitude)

if __name__ == "__main__":
    # example()
    main()
    # test()
