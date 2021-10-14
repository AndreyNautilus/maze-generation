from point import *
import array
import random

class Maze:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.index = lambda p : int(p.x + p.y * self.width)

        self.items = array.array('i')
        for row in range(self.height):
            for col in range(self.width):
                if row % 2 == 1 and col % 2 == 1:
                    self.items.append(0)
                else:
                    self.items.append(1)

        path = [Point(1, 1)]
        self.visit(path[0])
        while len(path) > 0:
            curPoint = path[len(path) - 1]
            points = unvisitedNeighbors(self, curPoint)

            if len(points) == 0:
                path.pop()
                continue

            nextPoint = points[random.randint(0, len(points) - 1)]
            self.visit(nextPoint)
            self.setSpace((curPoint.x + nextPoint.x) / 2, (curPoint.y + nextPoint.y) / 2)
            path.append(nextPoint)

        self.cleanMeta()

    def findPath(self, start, end):
        #print("from " + str(start) + " to " + str(end))
        path = [start]
        self.visit(path[0])
        while len(path) > 0:
            curPoint = path[len(path) - 1]
            points = unvisitedNeighbors(self, curPoint, 1)

            if len(points) == 0:
                path.pop()
                continue

            if end in points:
                path.append(end)
                break

            nextPoint = min(points, key=lambda p: (p - end).normSq())
            self.visit(nextPoint)
            path.append(nextPoint)

        self.cleanMeta()
        return path

    BIT_VISITED = 2

    def visit(self, point):
        self.items[self.index(point)] |= Maze.BIT_VISITED

    def visited(self, point):
        return self.item(point) & Maze.BIT_VISITED != 0

    def setSpace(self, x, y):
        idx = self.index(Point(x, y))
        self.items[idx] = self.items[idx] >> 1 << 1

    def isInside(self, point):
        return 0 <= point.x and point.x < self.width and 0 <= point.y and point.y < self.height

    def item(self, point):
        if self.isInside(point):
            return self.items[self.index(point)]
        return None

    def cleanMeta(self):
        for row in range(self.height):
            for col in range(self.width):
                self.items[self.index(Point(col, row))] &= 1

    def printMap(self):
        print(str(self.width) + 'x' + str(self.height))
        for row in range(self.height):
            s = ''
            for col in range(self.width):
                s += str(self.item(Point(col, row)))
            print(s)

    def printMaze(self):
        for row in range(self.height):
            s = ''
            for col in range(self.width):
                v = self.item(Point(col, row)) % 2
                if   v == 1: s += '*'
                elif v == 0: s += ' '
                else:        s += '?'
            print(s)

    def drawMaze(self):
        for row in range(self.height):
            s = ''
            for col in range(self.width):
                v = self.item(Point(col, row))
                if v % 2 == 0:
                    if v % 4 / 2 == 1:
                        s += '*'
                    else:
                        s += ' '
                else:
                    isWall = lambda v : v is None or v % 2 == 1

                    up    = self.item(Point(col    , row - 1))
                    down  = self.item(Point(col    , row + 1))
                    left  = self.item(Point(col - 1, row    ))
                    right = self.item(Point(col + 1, row    ))

                    if (isWall(up) or isWall(down)) and (isWall(left) or isWall(right)):
                        s += '+'
                    elif not (isWall(up) or isWall(down)):
                        s += '-'
                    else:
                        s += '|'

            print(s)


def unvisitedNeighbors(map, point, dist = 2):
    isSpace = lambda p : p is not None and p % 2 == 0
    return [ p for p in [
        Point(point.x - dist, point.y),
        Point(point.x, point.y - dist),
        Point(point.x + dist, point.y),
        Point(point.x, point.y + dist)] if map.isInside(p) and isSpace(map.item(p)) and not map.visited(p)]

if __name__ == "__main__":
    random.seed()

    maze = Maze(91, 21)
    #maze = Maze(11, 15)

    path = maze.findPath(Point(1, 1), Point(maze.width - 2, maze.height - 2))
    if len(path) == 0:
        print('path not found')
    for p in path:
        maze.visit(p)

    maze.drawMaze()
