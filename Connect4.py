from board import Board
from cell import Cell

B = Board([9, 14, 7, 8, 8, 11, 10, 7], [Cell(1, 1), Cell(2, 2)])

B.print_board()
B.add_player(0)
B.add_player(1)
while not(B.check_for_winner()):
    B.play_piece(B.get_turn(1)%2,B.player[B.get_turn(0)%2].get_input())
    B.print_board()
print("winner")