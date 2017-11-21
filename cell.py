

EMPTY = 0
Xs = 1
Os = 2
DEAD = 3


class Cell:
    def __init__(self,x,y,dead_cell=False):
        self.x = x
        self.y = y
        self.status = EMPTY
        if dead_cell:
            for i in dead_cell:
                if i.x == self.x and i.y == self.y:
                    self.status = DEAD
                    break

    def print_coords(self):
        print(self.x, " ", self.y, "\n" )

