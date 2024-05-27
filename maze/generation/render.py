from termcolor import colored

from .maze import Maze, BIT_WALL
from .point import Point


def render(maze: Maze, path: list[Point]):
    def isWall(v: int) -> bool:
        return v is None or v & BIT_WALL == 1

    for row in range(maze.height):
        s = ''
        for col in range(maze.width):
            p = Point(col, row)
            v = maze.cell(p)

            if isWall(v):
                up    = maze.cell(Point(col    , row - 1))
                down  = maze.cell(Point(col    , row + 1))
                left  = maze.cell(Point(col - 1, row    ))
                right = maze.cell(Point(col + 1, row    ))

                if (isWall(up) or isWall(down)) and (isWall(left) or isWall(right)):
                    s += '+'
                elif not (isWall(up) or isWall(down)):
                    s += '-'
                else:
                    s += '|'
            else:
                if p in path:
                    p_up    = Point(col    , row - 1)
                    p_down  = Point(col    , row + 1)
                    p_left  = Point(col - 1, row    )
                    p_right = Point(col + 1, row    )

                    color = 'green'
                    if any([(p not in path) for p in [p_up, p_down, p_left, p_right] if not isWall(maze.cell(p))]):
                        color = 'red'

                    s += colored('*', color)
                else:
                    s += ' '

        print(s)
