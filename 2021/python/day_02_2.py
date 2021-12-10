import day_02_1


class Submarine(day_02_1.Submarine):
    def __init__(self):
        super(Submarine, self).__init__()
        self._aim: int = 0

    def follow_course(self) -> None:
        for command in self._course:
            if command[0] == "forward":
                self._x += command[1]
                if self._aim != 0:
                    self._y += self._aim * command[1]
                    if self._y <= 0:
                        self._y = 0
            else:
                if command[0] == "down":
                    self._aim += command[1]
                elif command[0] == "up":
                    self._aim -= command[1]


if __name__ == "__main__":
    input_file = "../inputs/02/input.txt"
    sub = Submarine()
    sub.append_course_file(input_file)
    sub.follow_course()
    sub.print_position()
