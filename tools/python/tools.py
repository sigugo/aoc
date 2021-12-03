# Read input data into list of strings
def file_to_list(file_name: str) -> list:
    output = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.rstrip()
            if len(line.strip()) > 0:
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
 
