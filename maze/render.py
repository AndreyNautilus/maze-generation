from termcolor import colored

from .maze import Maze, BIT_WALL
from .point import Point


def is_wall(v: int) -> bool:
    return v is None or v & BIT_WALL == 1


def render(maze: Maze, path: list[Point]):
    for row in range(maze.height):
        s = ''
        for col in range(maze.width):
            p = Point(col, row)
            v = maze.cell(p)

            if is_wall(v):
                up    = maze.cell(Point(col    , row - 1))
                down  = maze.cell(Point(col    , row + 1))
                left  = maze.cell(Point(col - 1, row    ))
                right = maze.cell(Point(col + 1, row    ))

                if (is_wall(up) or is_wall(down)) and (is_wall(left) or is_wall(right)):
                    s += '+'
                elif not (is_wall(up) or is_wall(down)):
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
                    if any([(p not in path) for p in [p_up, p_down, p_left, p_right] if not is_wall(maze.cell(p))]):
                        color = 'red'

                    s += colored('*', color)
                else:
                    s += ' '

        print(s)
