from tools import *


class InvisibleOrigami:
    def __init__(self, input_data: list[str] = []):
        self._sheet: list[list[bool]] = []
        self._folds: list[tuple[str, int]] = []
        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input: list[str]) -> None:
        fold_prefix = "fold along"
        fold_separator = "="
        draw_separator = ","
        draw_instructions: list[tuple[int, int]] = []
        max_x_index: int = 0
        max_y_index: int = 0
        for line in input_data:
            if line and line.find(fold_prefix) == 0:
                direction, index = (
                    line.replace(fold_prefix, "").strip().split(fold_separator)
                )
                self._folds.append((direction, int(index)))
            elif line:
                x, y = list(map(int, line.split(draw_separator)))
                if x > max_x_index:
                    max_x_index = x
                if y > max_y_index:
                    max_y_index = y
                draw_instructions.append((x, y))
        self._sheet = [[False] * (max_x_index + 1) for i in range(max_y_index + 1)]
        for x, y in draw_instructions:
            self._sheet[y][x] = True

    def fold_all(self) -> None:
        for fd, fi in self._folds:
            self.fold(fd, fi)

    def fold(self, fold_axis: str, fold_index: int) -> None:
        print("Folding", fold_axis, "at index", fold_index, "\n")
        if fold_axis == "x":
            self._fold_x(fold_index)
        elif fold_axis == "y":
            self._fold_y(fold_index)

    def _fold_x(self, fold_index: int) -> None:
        sheet_a: list[list[bool]] = []
        sheet_b_reversed: list[list[bool]] = []
        for xaxis in self._sheet:
            sheet_a.append(xaxis[:fold_index])
            part_b = xaxis[fold_index + 1 :]
            part_b.reverse()
            sheet_b_reversed.append(part_b)
        la = len(sheet_a[0])
        lb = len(sheet_b_reversed[0])
        if la != lb:
            ldiff = abs(la - lb)
            if la < lb:
                for i in range(len(sheet_a)):
                    sheet_a[i] = ldiff * [False] + sheet_a[i]
            elif lb < la:
                for i in range(len(sheet_b_reversed)):
                    sheet_b_reversed[i] = ldiff * [False] + sheet_b_reversed[i]
        self._combine_folds(sheet_a, sheet_b_reversed)
        # self._sheet = [[False] * len(sheet_a[0]) for i in range(len(sheet_a))]
        # for y in range(len(sheet_a)):
        #     for x in range(len(sheet_a[y])):
        #         self._sheet[y][x] = sheet_a[y][x] or sheet_b_reversed[y][x]

    def _fold_y(self, fold_index: int) -> None:
        sheet_a = self._sheet[:fold_index]
        sheet_b_reversed = self._sheet[fold_index + 1 :]
        sheet_b_reversed.reverse()
        la = len(sheet_a)
        lb = len(sheet_b_reversed)
        if la != lb:
            ldiff = abs(la - lb)
            if la < lb:
                sheet_a = [[False] * len(sheet_a[0]) for i in range(diff)] + sheet_a
            elif lb < la:
                sheet_b_reversed = [[False] * len(sheet_b_reversed[0]) for i in range(ldiff)] + sheet_b_reversed

        self._combine_folds(sheet_a, sheet_b_reversed)

    def _combine_folds(
        self, a: list[list[bool]], b: list[list[bool]], debug: bool = False 
    ) -> None:
        self._sheet = [[False] * len(a[0]) for i in range(len(a))]
        for y in range(len(a)):
            for x in range(len(a[y])):
                self._sheet[y][x] = a[y][x] or b[y][x]
        if debug:
            print(self)

    def count_dots(self) -> int:
        count = 0
        for i in self._sheet:
            for j in i:
                if j:
                    count += 1
        return count

    def __str__(self):
        output = ""
        for i in self._sheet:
            line = ""
            for j in i:
                if j:
                    line += "#"
                else:
                    line += "."
            output += line + "\n" 
        return output


if __name__ == "__main__":
    input_file = "../inputs/13/data.input"
    # input_file = "../inputs/13/data.example"
    input_data: list[str] = file_to_list(input_file)
    
    paper = InvisibleOrigami(input_data)
    # print(paper) 
    # (fd, fi) = paper._folds[0]
    # paper.fold(fd, fi)
    # print(paper.count_dots())
    
    #(fd, fi) = paper._folds[0]
    #paper.fold(fd, fi)
    
    paper.fold_all()
   
    print(paper)
