# Read input data into list of strings
def file_to_list(file_name: str) -> list:
    output = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            output.append(line)
    return output


# given a list of strings with equal length
# count the occurrence of a character in the whole list at the given string index
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


# sort a string alphabetically
def sort_string(data: str) -> str:
    return "".join(sorted(data))


# sort a list by length
def sort_by_length(strings: list) -> list:
    return sorted(strings, key=len)


# get a value from a 2d matrix (list of lists, where y is the index in the list of lists and x the index in the
# individual list a default value will be returned, if the index would be out of bounds
def get_2d_matrix_value_at_x_y_safe(
    matrix: list[list[any]], x: int, y: int, no_value_value=0, log_level: int = 0
) -> any:
    value = no_value_value
    if log_level > 1:
        print("* Getting value for:", x, y)
    if 0 <= y < len(matrix):
        if 0 <= x < len(matrix[y]):
            value = matrix[y][x]
        elif log_level > 0:
            print("out of bounds x", x, y)
    elif log_level > 0:
        print("out of bounds y", x, y)
    if log_level > 1:
        print("value returned", value)
    return value


# get a value from a 2d matrix (list of lists, where y is the index in the list of lists and x the index in the
# individual list a default value will be returned, if the index would be out of bounds
def set_2d_matrix_value_at_x_y_safe(
    matrix: list[list[any]], x: int, y: int, value: any, log_level: int = 0
) -> any:
    if log_level > 1:
        print("* Setting value for:", x, y)
    if 0 <= y < len(matrix):
        if 0 <= x < len(matrix[y]):
            matrix[y][x] = value
        elif log_level > 0:
            print("out of bounds x", x, y)
    elif log_level > 0:
        print("out of bounds y", x, y)
    if log_level > 1:
        print("value set", value, "at", x, y)
    return matrix


# count individual characers in a string and return a sorted list of tuples with count, character
def character_counts(data: str) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    counter: dict[str, int] = {}
    for c in data:
        counter[c] = counter.setdefault(c, 0) + 1
    for k, v in counter.items():
        result.append(tuple((v, k)))
    result.sort()
    return result


# sum of a series incrementing by step from start for count times
# def sum_incrementing(first: int, count: int, step: int = 1) -> int:
#     last = first + (count * step)
#     return (2 * first + count * step) / 2 * count
