from tools import file_to_list


class Submarine:
    def __init__(self):
        self._x: int = 0
        self._y: int = 0
        self._course: list[tuple[str, int]] = []

    def append_course_file(self, file_name: str) -> None:
        file_data = file_to_list(file_name)
        for entry in file_data:
            direction = entry.split(" ")[0].strip()
            distance = entry.split(" ")[1].strip()
            self._course.append((direction, int(distance)))

    def follow_course(self) -> None:
        for command in self._course:
            if command[0] == "forward":
                self._x += command[1]
            elif command[0] == "down":
                self._y += command[1]
            elif command[0] == "up":
                self._y -= command[1]
                if self._y <= 0:
                    self._y = 0

    def print_position(self) -> None:
        print("Distance:", self._x)
        print("Depth:", self._y)
        print("AOC Result", self._x * self._y)


if __name__ == '__main__':
    input_file = '../inputs/2/input.txt'
    sub = Submarine()
    sub.append_course_file(input_file)
    sub.follow_course()
    sub.print_position()
