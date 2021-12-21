from tools import *

class TodaysClass():
    def __init__(self, input_data: list[str] = []):

        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input_data: list[str]):
        for line in input_data:
            print(line)


if __name__ == "__main__":
    #input_file = "../inputs/x/data.input"
    input_file = "../inputs/x/data.example"
    input_data: list[str] = file_to_list(input_file)
