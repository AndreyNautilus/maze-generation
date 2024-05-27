import argparse
import random

from .generation.point import Point
from .generation.greedy import generate as generate_greedy
from .generation.render import render
from .generation.path_finding import findPath


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    args = parser.parse_args()

    random.seed()

    maze = generate_greedy(args.width, args.height)
    path = findPath(maze, Point(1, 1), Point(maze.width - 2, maze.height - 2))
    if len(path) == 0:
        print('path not found')

    render(maze, path)


if __name__ == "__main__":
    main()
