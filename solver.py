from cube import Cube


class Solver:
    cube: Cube

    def __init__(self, cube: Cube):
        self.cube = cube

    def solve_cross(self) -> None:
        ...
