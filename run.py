from cube import Cube

cube_in = [
    ["y", "y", "y", "y", "y", "y", "y", "y", "y"],
    ["g", "g", "g", "g", "g", "g", "g", "g", "g"],
    ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
    ["b", "b", "b", "b", "b", "b", "b", "b", "b"],
    ["r", "r", "r", "r", "r", "r", "r", "r", "r"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w"],
]

cube = Cube(cube_in)
cube.describe()
cube.execute_moves(["R2", "L2", "U2", "D2", "F2", "B2"])
cube.describe()
