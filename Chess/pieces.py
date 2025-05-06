class Piece:
    def __init__(self, c: int):
        self.color = c

    def get_color(self):
        return self.color

    def can_move(self, sx, sy, x, y):
        return


class Pawn(Piece):
    def __init__(self, c: int):
        super().__init__(c)
        self.on_first_row = True

    def can_move(self, sx, sy, x, y):
        if self.color:
            if x - sx == 1 or (self.on_first_row and x - sx == 2):
                return True
            return False
        else:
            if sx - x == 1 or (self.on_first_row and sx - x == 2):
                return True
            return False

    def is_on_border(self, x):
        if self.color:
            return x == 7
        else:
            return x == 0


class Rook(Piece):
    def __init__(self, c: int):
        super().__init__(c)
        self.did_not_move = True

    def can_move(self, sx, sy, x, y):
        return (sx == x) or (sy == y)

    def can_do_castling(self):
        return self.did_not_move


class Knight(Piece):
    def can_move(self, sx, sy, x, y):
        if (abs(x - sx) == 2 and abs(y - sy) == 1) or (abs(x - sx) == 1 and abs(y - sy) == 2):
            return True
        return False


class Bishop(Piece):
    def can_move(self, sx, sy, x, y):
        if abs(x - sx) == abs(y - sy):
            return True
        return False


class Queen(Piece):
    def can_move(self, sx, sy, x, y):
        if (abs(x - sx) == abs(y - sy)) or ((x == sx) or (y == sy)):
            return True
        return False


class King(Piece):
    def __init__(self, c: int):
        super().__init__(c)
        self.did_not_move = True

    def can_move(self, sx, sy, x, y):
        if abs(x - sx) <= 1 and abs(y - sy) <= 1:
            return True
        return False
