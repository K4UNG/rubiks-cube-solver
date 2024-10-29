class Cube:
    cube: list[list[str]]
    piece_map = {
        0: [(1, [0, 1, 2]), (4, [0, 1, 2]), (3, [0, 1, 2]), (2, [0, 1, 2])],
        1: [(0, [6, 7, 8]), (2, [0, 3, 6]), (5, [2, 1, 0]), (4, [8, 5, 2])],
        2: [(0, [8, 5, 2]), (3, [0, 3, 6]), (5, [8, 5, 2]), (1, [8, 5, 2])],
        3: [(0, [0, 1, 2]), (4, [6, 3, 0]), (5, [8, 7, 6]), (2, [2, 5, 8])],
        4: [(0, [0, 3, 6]), (1, [0, 3, 6]), (5, [0, 3, 6]), (3, [8, 5, 2])],
        5: [(1, [6, 7, 8]), (2, [6, 7, 8]), (3, [6, 7, 8]), (4, [6, 7, 8])],
    }

    def __init__(self, cube: list[list[str]]):
        self.cube = cube

    def __rotate(self, face: int, cw: bool) -> None:
        c1, e1, c2, e2, c, e3, c3, e4, c4 = self.cube[face]
        if cw:
            self.cube[face] = [c3, e2, c1, e4, c, e1, c4, e3, c2]
        else:
            self.cube[face] = [c2, e3, c4, e1, c, e4, c1, e2, c3]

        new_row = []
        pieces = self.piece_map[face] if cw else list(reversed(self.piece_map[face]))
        for row in pieces:
            curr_face = self.cube[row[0]]
            curr_row = []
            for i, piece in enumerate(row[1]):
                curr_row.append(curr_face[piece])
                if new_row:
                    curr_face[piece] = new_row[i]
            new_row = curr_row

        first_pieces = pieces[0]
        for i, piece in enumerate(first_pieces[1]):
            self.cube[first_pieces[0]][piece] = new_row[i]

    def R(self) -> None:
        self.__rotate(2, True)

    def R_(self) -> None:
        self.__rotate(2, False)

    def U(self) -> None:
        self.__rotate(0, True)

    def U_(self) -> None:
        self.__rotate(0, False)

    def L(self) -> None:
        self.__rotate(4, True)

    def L_(self) -> None:
        self.__rotate(4, False)

    def D(self) -> None:
        self.__rotate(5, True)

    def D_(self) -> None:
        self.__rotate(5, False)

    def B(self) -> None:
        self.__rotate(3, True)

    def B_(self) -> None:
        self.__rotate(3, False)

    def F(self) -> None:
        self.__rotate(1, True)

    def F_(self) -> None:
        self.__rotate(1, False)

    def execute_moves(self, moves: list[str]) -> None:
        notation_map = {
            "R": self.R,
            "R2": self.R,
            "R'": self.R_,
            "U": self.U,
            "U2": self.U,
            "U'": self.U_,
            "L": self.L,
            "L2": self.L,
            "L'": self.L_,
            "D": self.D,
            "D2": self.D,
            "D'": self.D_,
            "B": self.B,
            "B2": self.B,
            "B'": self.B_,
            "F": self.F,
            "F2": self.F,
            "F'": self.F_,
        }
        for move in moves:
            move_func = notation_map.get(move)
            if move_func:
                if move[-1] == "2":
                    move_func()
                move_func()
            else:
                raise ValueError(f"Invalid notation: {move}")

    def __get_row_string(self, *faces: int | None) -> str:
        result = ""
        for i in range(3):
            result += " ".join(
                map(
                    lambda face: "".join(self.cube[face][0 + (3 * i) : 3 + (3 * i)])
                    if face is not None
                    else "   ",
                    faces,
                )
            )
            if i < 2:
                result += "\n"
        return result

    def describe(self) -> str:
        print(self.__get_row_string(None, 0))
        print(self.__get_row_string(4, 1, 2, 3))
        print(self.__get_row_string(None, 5))
        print()
