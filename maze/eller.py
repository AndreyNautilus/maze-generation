from point import *
import array
import random

class Maze:
    BIT_RIGHT_WALL = 1
    BIT_DOWN_WALL = 2

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.index = lambda p : p.x + p.y * self.width

        self.items = array.array('i')
        for row in range(self.height):
            for col in range(self.width - 1):
                self.items.append(0)
            self.items.append(Maze.BIT_RIGHT_WALL)

        prevNumbers = None
        for row in range(1):
            if prevNumbers is None:
                curNumbers = range(1, 1 + width)
                #for col in range(width):
                #    self.items[self.index(Point(col, row))] = 0
            #else:
            #    curNumbers = prevNumbers
            #    for col in range(width):
            #        self.items(index(Point(col, row))) = self.items(index(Point(col, row - 1)))
            #        if self.items(index(Point(col, row))) & BIT_RIGHT_WALL:

            for col in range(width - 1):
                if random.randint(0, 100) > 50:
                    self.items[self.index(Point(col, row))] |= Maze.BIT_RIGHT_WALL
                else:
                    curNumbers[col + 1] = curNumbers[col]

            print curNumbers


    def drawMaze(self):
        s = ' '
        for col in range(self.width - 1):
            s += '__'
        print s + '_'
        for row in range(self.height):
            s = '|'
            for col in range(self.width):
                v = self.items[self.index(Point(col, row))]
                if v & Maze.BIT_DOWN_WALL != 0:
                    s += '_'
                else:
                    s += ' '
                if v & Maze.BIT_RIGHT_WALL != 0:
                    s += '|'
                else:
                    s += ' '
            print s


if __name__ == "__main__":
    random.seed()

    m = Maze(8, 4)
    m.drawMaze();