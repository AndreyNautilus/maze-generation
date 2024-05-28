import random

from ..point import Point
from ..maze import (Maze, BIT_WALL)


BIT_VISITED = 0b10  # second bit


def visit(maze: Maze, p: Point):
    maze.cells[maze.index(p)] |= BIT_VISITED


def isVisited(maze: Maze, p: Point) -> bool:
    return maze.cell(p) & BIT_VISITED != 0


def eraseWall(maze: Maze, x: int, y: int):
    idx = maze.index(Point(x, y))
    maze.cells[idx] = maze.cells[idx] >> 1 << 1  # erase BIT_WALL


def unvisitedNeighbors(maze: Maze, p: Point, dist: int = 2):
    def isSpace(v: int) -> bool:
        return v is not None and v % 2 == 0

    return [p for p in [
        Point(p.x - dist, p.y),
        Point(p.x, p.y - dist),
        Point(p.x + dist, p.y),
        Point(p.x, p.y + dist)] if maze.is_inside(p) and isSpace(maze.cell(p)) and not isVisited(maze, p)]


def cleanVisited(maze: Maze):
    for row in range(maze.height):
        for col in range(maze.width):
            maze.cells[maze.index(Point(col, row))] &= 1


def generate(width: int, height: int) -> Maze:
    maze = Maze(width, height)

    path = [Point(1, 1)]
    visit(maze, path[0])
    while len(path) > 0:
        curPoint = path[len(path) - 1]
        points = unvisitedNeighbors(maze, curPoint)

        if len(points) == 0:
            path.pop()
            continue

        nextPoint = points[random.randint(0, len(points) - 1)]
        visit(maze, nextPoint)
        eraseWall(maze, (curPoint.x + nextPoint.x) // 2, (curPoint.y + nextPoint.y) // 2)
        path.append(nextPoint)

    cleanVisited(maze)
    return maze
