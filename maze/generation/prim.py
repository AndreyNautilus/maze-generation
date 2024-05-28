import random

from ..point import Point
from ..maze import (Maze, BIT_WALL)


def erase_wall(maze: Maze, p: Point):
    idx = maze.index(p)
    maze.cells[idx] = maze.cells[idx] >> 1 << 1  # erase BIT_WALL


def get_neighbours(maze: Maze, p: Point) -> list[Point]:
    def is_space(v: int) -> bool:
        return v is not None and v & BIT_WALL == 0

    return [p for p in [
        Point(p.x - 2, p.y),
        Point(p.x,     p.y - 2),
        Point(p.x + 2, p.y),
        Point(p.x,     p.y + 2)] if maze.is_inside(p) and is_space(maze.cell(p))]


def generate(width: int, height: int) -> Maze:
    maze = Maze(width, height)

    front = [Point(1, 1)]
    visited = [front[0]]
    while len(front) > 0:
        p_index = random.randint(0, len(front) - 1)
        p = front[p_index]

        neighbors = get_neighbours(maze, p)
        unvisited_neighbors = [p for p in neighbors if p not in visited]

        if len(unvisited_neighbors) == 0:
            front.pop(p_index)
            continue

        if len(unvisited_neighbors) == 1:
            next_p = unvisited_neighbors[0]
            front.pop(p_index)
        else:
            next_p = unvisited_neighbors[random.randint(0, len(unvisited_neighbors) - 1)]

        erase_wall(maze, Point((p.x + next_p.x) // 2, (p.y + next_p.y) // 2))
        front.append(next_p)
        visited.append(next_p)

    return maze
