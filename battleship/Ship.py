#!/usr/bin/python
# vim: set fileencoding=utf-8

from .Cell import Cell


class Ship(object):
    names = ['Boat', 'Submarine', 'Destroyer', 'Battleship', 'Carrier']

    def __init__(self, cells=[]):
        self.cells = cells
        self.length = len(cells)
        try:
            self.name = self.names[self.length - 1]
        except IndexError:
            self.name = "UFO"
        if self.length > 1:
            dx = cells[1].x - cells[0].x
            dy = cells[1].y - cells[0].y
            if dx > 0:
                self.direction = "H"
            elif dy > 0:
                self.direction = "V"
        else:
            self.direction = "N"
        self.area = self.find_area()

    def composite(self, x, y, state):
        return Cell(x, y, state)

    def create_cells(self, start_x, start_y, length, direction, state):
        cells = [None] * length
        for i in range(0, length):
            if direction == "V":
                x = start_x
                y = start_y + i
            elif direction == "H":
                x = start_x + i
                y = start_y
            cells[i] = self.composite(x, y, state)

    def create(self, start_x, start_y, length, direction, state='ship'):
        self.length = length
        self.cells = [None] * length
        for i in range(0, length):
            if direction == "V":
                x = start_x
                y = start_y + i
            elif direction == "H":
                x = start_x + i
                y = start_y
            self.cells[i] = self.composite(x, y, state)
        try:
            self.name = self.names[self.length - 1]
        except IndexError:
            self.name = "UFO"
        self.direction = direction
        self.area = self.find_area()

    def get_rotated_direction(self):
        if self.direction == "V":
            return "H"
        elif self.direction == "H":
            return "V"
        return "N"

    def find_area(self):
        area = []
        for c in self.cells:
            #print(c.x, c.y)
            area += self.get_near(c, 1, self.cells + area)
        return area

    def get_near(self, center, radius, engaged=None):
        near = []
        if not engaged:
            engaged = [center]
        else:
            engaged = engaged[:]
            engaged.append(center)

        for x in range(center.x + radius, center.x - radius - 1, -1):
            for y in range(center.y + radius, center.y - radius - 1, -1):
                new = True
                for e in engaged:
                    if x == e.x and y == e.y:
                        new = False
                        break
                if new:
                    cell = self.composite(x, y, 'near')
                    near.append(cell)
                    engaged.append(cell)

        return near
