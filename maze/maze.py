from .point import Point


BIT_WALL = 0b1  # last bit


def _create_cells_as_grid(width: int, height: int) -> list[int]:
    if width % 2 == 0 or height % 2 == 0:
        raise ValueError(f'Both {width=} and {height=} must be odd')

    cells: list[int] = []
    for row in range(height):
        for col in range(width):
            if row % 2 == 1 and col % 2 == 1:
                cells.append(0)
            else:
                cells.append(BIT_WALL)
    return cells


def _create_cells_filled(width: int, height: int) -> list[int]:
    cells = [BIT_WALL] * (width * height)
    return cells


class Maze:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.cells = _create_cells_as_grid(self.width, self.height)
        #self.cells = _create_cells_filled(self.width, self.height)


    def is_inside(self, p: Point) -> bool:
        return 0 <= p.x and p.x < self.width and \
               0 <= p.y and p.y < self.height


    def index(self, p: Point) -> int:
        return p.x + p.y * self.width


    def cell(self, p: Point) -> int:
        idx = self.index(p)
        if idx < len(self.cells):
            return self.cells[idx]
        return None
