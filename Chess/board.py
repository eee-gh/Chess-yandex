from pieces import *

WHITE = 0
BLACK = 1


def correct_cords(x, y):
    return (0 <= x <= 7) and (0 <= y <= 7)


class Board:
    def __init__(self):
        self.board = [
            [Rook(1), Knight(1), Bishop(1), Queen(1), King(1), Bishop(1), Knight(1), Rook(1)],
            [Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0)],
            [Rook(0), Knight(0), Bishop(0), Queen(0), King(0), Bishop(0), Knight(0), Rook(0)],
        ]
        self.w_king_cords = (7, 4)
        self.b_king_cords = (0, 4)
        self.cpc = WHITE
        self.chosen = None

    def get_board(self):
        return self.board

    def get_color(self):
        return self.cpc

    def is_way_clear(self, sx, sy, x, y, board):
        if sx == x and sy == y:
            return False

        if isinstance(board[sx][sy], Knight):
            if board[x][y] is None or board[x][y].get_color() != board[sx][sy].get_color():
                return True
            else:
                return False

        if isinstance(board[sx][sy], King):
            if self.is_under_attack(x, y, board[sx][sy].get_color()):
                return False

        if (sx == x) or (sy == y):

            if sx == x:
                mn, mx = min(sy, y), max(sy, y)
                for ny in range(mn, mx + 1):
                    if sy == ny:
                        continue
                    if not isinstance(board[sx][sy], Pawn):
                        if ny == mn or ny == mx:
                            if (board[x][ny] is not None
                                    and board[x][ny].get_color() != board[sx][sy].get_color()):
                                continue
                    if board[x][ny] is not None:
                        return False

            else:
                mn, mx = min(sx, x), max(sx, x)
                for nx in range(mn, mx + 1):
                    if sx == nx:
                        continue
                    if not isinstance(board[sx][sy], Pawn):
                        if nx == mn or nx == mx:
                            if (board[nx][y] is not None
                                    and board[nx][y].get_color() != board[sx][sy].get_color()):
                                continue
                    if board[nx][y] is not None:
                        return False

        else:
            if isinstance(board[sx][sy], Pawn):
                if sy == y:
                    if board[x][y] is None:
                        return True
                    return False
                else:
                    if (board[x][y] is not None and board[x][y].get_color() != board[sx][sy].get_color()
                            and abs(sy - y) == 1 and abs(sx - x) == 1):
                        return True
                    return False

            lb = abs(sx - x)
            if x > sx and y > sy:
                for i in range(1, lb + 1):
                    if i == lb:
                        if (board[sx + i][sy + i] is not None
                                and board[sx + i][sy + i].get_color() != board[sx][sy].get_color()):
                            continue
                    if board[sx + i][sy + i] is not None:
                        return False

            elif x > sx and y < sy:
                for i in range(1, lb + 1):
                    if i == lb:
                        if (board[sx + i][sy - i] is not None
                                and board[sx + i][sy - i].get_color() != board[sx][sy].get_color()):
                            continue
                    if board[sx + i][sy - i] is not None:
                        return False

            elif x < sx and y > sy:
                for i in range(1, lb + 1):
                    if i == lb:
                        if (board[sx - i][sy + i] is not None
                                and board[sx - i][sy + i].get_color() != board[sx][sy].get_color()):
                            continue
                    if board[sx - i][sy + i] is not None:
                        return False

            else:
                for i in range(1, lb + 1):
                    if i == lb:
                        if (board[sx - i][sy - i] is not None
                                and board[sx - i][sy - i].get_color() != board[sx][sy].get_color()):
                            continue
                    if board[sx - i][sy - i] is not None:
                        return False

        return True

    def move_piece(self, sx, sy, x, y):
        if correct_cords(x, y) and (self.board[sx][sy] is not None) and (self.board[sx][sy].can_move(sx, sy, x, y)) \
                and (self.board[sx][sy].color == self.cpc) \
                and self.is_way_clear(sx, sy, x, y, self.board):
            self.board[x][y] = self.board[sx][sy]
            self.board[sx][sy] = None
            if (isinstance(self.board[x][y], Pawn) or isinstance(self.board[x][y], Rook)
                    or isinstance(self.board[x][y], Knight)):
                self.board[x][y].did_not_move = False

            if isinstance(self.board[x][y], Pawn):
                if self.board[x][y].get_color() == WHITE and x == 0:
                    self.board[x][y] = Queen(WHITE)
                elif self.board[x][y].get_color() == BLACK and x == 7:
                    self.board[x][y] = Queen(BLACK)

            if isinstance(self.board[x][y], King):
                if self.board[x][y].get_color() == WHITE:
                    self.w_king_cords = (x, y)
                else:
                    self.b_king_cords = (x, y)

            self.cpc = abs(self.cpc - 1)
            return True
        return False

    def is_under_attack(self, sx, sy, color):
        b = [[y for y in x] for x in self.board]
        if color == WHITE:
            b[self.w_king_cords[0]][self.w_king_cords[1]] = None
            b[sx][sy] = King(WHITE)
        else:
            b[self.b_king_cords[0]][self.b_king_cords[1]] = None
            b[sx][sy] = King(BLACK)

        for x in range(8):
            for y in range(8):
                if (b[x][y] is not None and b[x][y].get_color() != color and
                        b[x][y].can_move(x, y, sx, sy)):
                    if not isinstance(b[x][y], King):
                        if self.is_way_clear(x, y, sx, sy, b):
                            return True
        return False
