from six import add_move

from pieces import *

WHITE = 0
BLACK = 1


def correct_cords(x, y):
    return (0 <= x <= 7) and (0 <= y <= 7)


class Board:
    def __init__(self):
        self.board = [
            [Rook(1), Knight(1), Bishop(1), King(1), Queen(1), Bishop(1), Knight(1), Rook(1)],
            [Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0)],
            [Rook(0), Knight(0), Bishop(0), King(0), Queen(0), Bishop(0), Knight(0), Rook(0)],
        ]
        self.cpc = WHITE

    def get_board(self):
        return self.board

    def get_color(self):
        return self.cpc

    def is_way_clear(self, sx, sy, x, y):
        if isinstance(self.board[sx][sy], Knight):
            if self.board[x][y] is None or self.board[x][y].color != self.board[sx][sy].color:
                return True
            else:
                return False

        # !!!!!!!!!!

        return False

    def move_piece(self, sx, sy, x, y):
        if correct_cords(x, y) and (self.board[sx][sy] is not None) and (self.board[sx][sy].color == self.cpc) \
                and not (sx == x and sy == y) and self.is_way_clear(sx, sy, x, y):
            pass

    def is_under_attack(self, x, y, color):
        return
