#!/usr/bin/python
# vim: set fileencoding=utf-8


class Cell(object):

    # states = {'fog','empty', 'ship', 'miss', 'near', 'fate'}
    
    def __init__(self, x, y, state = None, ship = None):
        self.x = x
        self.y = y
        self.state = None
        if state:
            self.state = state
        self.ship = None
        if ship:
            self.ship = ship

    def set_state(self, state):
        self.state = state
        
    def draw(self):
        s = ""
        if self.state == 'empty':
            s = "."
        elif self.state == 'ship':
            s = "x"
        elif self.state == 'near':
            s = "*"
        elif self.state == 'fate':
            s = "%"
        elif self.state == 'miss':
            s = "o"
        elif self.state == 'fog':
            s = "~"
        return s
        

