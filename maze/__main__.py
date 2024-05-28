import argparse
import random

from .generation.depth_first import generate as generate_depth_first
from .generation.prim import generate as generate_prim

from .point import Point
from .maze import Maze
from .render import render
from .path_finding import find_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    args = parser.parse_args()

    random.seed()

    maze = generate_prim(args.width, args.height)
    path = find_path(maze, Point(1, 1), Point(maze.width - 2, maze.height - 2))
    if len(path) == 0:
        print('path not found')

    render(maze, path)

    # maze2 = generate_depth_first(args.width, args.height)
    # path2 = find_path(maze2, Point(1, 1), Point(maze2.width - 2, maze2.height - 2))
    # if len(path2) == 0:
    #     print('path not found')

    # render(maze2, path2)


if __name__ == "__main__":
    main()
