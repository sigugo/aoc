

def file_to_list(file_name: str) -> list:
    output = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.rstrip()
            if len(line.strip()) > 0:
                    output.append(line)
    return output

