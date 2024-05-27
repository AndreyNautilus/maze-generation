from .maze import Maze
from .point import Point


def getNeighbours(maze: Maze, p: Point) -> list[Point]:
    def isSpace(v: int) -> bool:
        return v is not None and v % 2 == 0

    return [p for p in [
        Point(p.x - 1, p.y),
        Point(p.x,     p.y - 1),
        Point(p.x + 1, p.y),
        Point(p.x,     p.y + 1)] if maze.isInside(p) and isSpace(maze.cell(p))]


def findPath(maze: Maze, start: Point, end: Point) -> list[Point]:
    path = [start]
    visited_cells = [path[0]]
    while len(path) > 0:
        curPoint = path[len(path) - 1]
        if curPoint == end:
            break

        neighbors = getNeighbours(maze, curPoint)
        unvisitedNeighbors = [p for p in neighbors if p not in visited_cells]

        if len(unvisitedNeighbors) == 0:
            path.pop()
            continue

        nextPoint = min(unvisitedNeighbors, key=lambda p: (p - end).normSq())
        visited_cells.append(nextPoint)
        path.append(nextPoint)

    return path
