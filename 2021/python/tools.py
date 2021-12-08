# Read input data into list of strings
def file_to_list(file_name: str) -> list:
    output = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            output.append(line)
    return output


# given a list of strings with equal length, count the occurenc of a character in the whole list at the given string index
def count_char_at_index(data: list[str], char: str, index: int) -> int:
    count: int = 0
    for string_value in data:
        if string_value[index] == char:
            count += 1
    return count


# XOR binary invert
def binary_invert(binary: str) -> str:
    return bin(int(binary, 2) ^ (2 ** (len(binary) + 1) - 1))[3:]


# compress multiple whitespaces in a string into one
def compress_spaces(data: str) -> str:
    return " ".join(data.split())


## sort a string alphabetically
def sort_string(data: str) -> str:
    return "".join(sorted(data))


## sort a list by length
def sort_by_length(strings: list) -> list:
    return sorted(strings, key=len)


# sum of a series incrementing by step from start for count times
# def sum_incrementing(first: int, count: int, step: int = 1) -> int:
#     last = first + (count * step)
#     return (2 * first + count * step) / 2 * count
