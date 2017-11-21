from cell import Cell
from player import *
import itertools
EMPTY = 0
P1s = 1
P2s = 2
DEAD = 3
DEADP = 4


class Column:
    def __init__(self,x,height,dead_cells):
        self.row = []
        for h in range(height):
            self.row.append(Cell(x, h, dead_cells))


class Board:
    def __init__(self,height,dead_cells):
        self.column = []
        self.maxH = 0
        self.player = []
        self.turn = 0
        for i in range(len(height)):
            if height[i] > self.maxH:
                self.maxH = height[i]
            self.column.append(Column(i,height[i],dead_cells))

    def add_player(self,type):
        if type == 0:
            self.player.append(Robot(len(self.player)))
        if type == 1:
            self.player.append(Human(len(self.player)))

    def get_turn(self,inc):
        self.turn = (self.turn + inc)%2
        return (self.turn + inc)%2

    def print_board(self):
        # [::-1] reverses the below range
        for i in range(self.maxH)[::-1]:
            print()
            for c in self.column:
                if len(c.row) > i:
                    if c.row[i].status == EMPTY:
                        print("_", end=" ")
                    if c.row[i].status == P1s:
                        print("1", end=" ")
                    if c.row[i].status == P2s:
                        print("2", end=" ")
                    if c.row[i].status == DEAD:
                        print("-", end=" ")
                    if c.row[i].status == DEADP:
                        print("=", end=" ")
                else:
                    print("  ", end="")
        print("\n\n\n")

    def play_piece(self,player, column):
        for c in self.column[column].row:
            if c.status == EMPTY:
                c.status = player+1
                break
            if c.status == DEAD:
                c.status = DEADP
                break

    def check_for_winner(self):
        try:
            for i in range(self.maxH):
                for r in self.column:
                    for c in r.row:
                        if c.status == P1s or c.status == P2s:
                            if self.check_diag(c):
                                return True
                            if  self.check_vert(c):
                                return True
                            if  self.check_hor(c):
                                return True
        except IndexError:
            return False

    def check_diag(self,cell):
        return self.check_diag_up(cell) or self.check_diag_down(cell)

    def check_diag_up(self,cell):
        if (cell.status == self.column[cell.x + 1].row[cell.y + 1].status and
            cell.status == self.column[cell.x + 2].row[cell.y + 2].status and
            cell.status == self.column[cell.x + 3].row[cell.y + 3].status):
                return True
        else:
            return False

    def check_diag_down(self,cell):
        if (cell.status == self.column[cell.x - 1].row[cell.y + 1].status and
            cell.status == self.column[cell.x - 2].row[cell.y + 2].status and
            cell.status == self.column[cell.x - 3].row[cell.y + 3].status):
                return True

        else:
            return False

    def check_vert(self,cell):
        consecutive = 0
        r = self.column[cell.x].row
        for c in itertools.islice(r,cell.y,len(r)-1):
            if c.status == cell.status:
                consecutive += 1
                print(consecutive, end="")
                if consecutive == 4:

                    return True
            else:
                return False
        return False

    def check_hor(self,cell):
        consecutive = 0
        for c in itertools.islice(self.column,cell.y,len(self.column)-1):
            if c.row[cell.y].status == cell.status:
                consecutive += 1
                print (consecutive, end=" ")
                if consecutive == 3:
                    return True
            else:
                return False
        return False

