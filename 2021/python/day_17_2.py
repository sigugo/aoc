from tools import *
from dataclasses import dataclass, field


@dataclass
class TrajectoryData:
    txmin: int
    txmax: int
    tymin: int
    tymax: int
    ymax: int = 0
    x0: int = 0
    y0: int = 0
    coolest_vx: int = 0
    coolest_vy: int = 0
    vectors: list = field(default_factory=list)

    def __post_init__(self):
        self._get_shots()

    @property
    def vxmax(self) -> int:
        tmax: int = 0
        for i in range(self.txmax, self.txmin - 1, -1):
            x: int = 0
            t: int = 0
            while x < i:
                t += 1
                x += t
            tmax = tmax if tmax > t - 1 else t
        return tmax

    def _get_shots(self):
        vylist = []
        for v in range(-1000, 1000):
            py = 0
            vy = v
            while True:
                py += vy
                vy -= 1
                if py < self.tymin:
                    break
                if self.tymin <= py <= self.tymax:
                    vylist.append(v)
                    break
        for ivx in range(self.txmax + 1):
            for ivy in vylist:
                px = 0
                py = 0
                ymax = 0
                vx = ivx
                vy = ivy
                while True:
                    px += vx
                    py += vy
                    if vx > 0:
                        vx -= 1
                    vy -= 1
                    if py > ymax:
                        ymax = py
                    if (
                        self.txmin <= px <= self.txmax
                        and self.tymin <= py <= self.tymax
                    ):
                        new_vector = tuple((ivx, ivy))
                        if new_vector not in self.vectors:
                            self.vectors.append((ivx, ivy))

                        if ymax > self.ymax:
                            self.ymax = ymax
                            self.coolest_vx = ivx
                            self.coolest_vy = ivy
                        break
                    elif (
                        (px > self.txmax)
                        or (py < self.tymin)
                        or (vx == 0 and px < self.txmin)
                    ):
                        break


class DroneLauncher:
    def __init__(self, input_data: list[str] = []):
        self._target_area: dict[str, int] = {}
        self._trajectory: TrajectoryData
        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input_data: list[str]):
        for line in input_data:
            self._trajectory = TrajectoryData(
                *(
                    [
                        int(value)
                        for pair in [
                            pair.strip()[2:].split("..")
                            for pair in input_data[0][13:].split(",")
                        ]
                        for value in pair
                    ]
                )
            )

    def make_the_shot(self) -> int:
        return self._trajectory.ymax

    def count_all_shots(self) -> int:
        return len(self._trajectory.vectors)


if __name__ == "__main__":
    input_file = "../inputs/17/data.input"
    # input_file = "../inputs/17/data.example"
    input_data: list[str] = file_to_list(input_file)
    launcher = DroneLauncher(input_data)
    print(launcher.count_all_shots())
