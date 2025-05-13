import tkinter
from shutil import which
from tkinter import PhotoImage

from board import *

LIGHT = '#ec972a'
DARK = '#372207'
WHITE = 0
BLACK = 1


def cell_color(xn, yn):
    if (xn + yn) % 2:
        return DARK
    return LIGHT


b = Board()
master = tkinter.Tk()
master.title('Chess')
master.geometry('600x600')
master.resizable(height=False, width=False)

white_pieces = {
    'k': PhotoImage(file='sprites/white/king.png'), 'q': PhotoImage(file='sprites/white/queen.png'),
    'r': PhotoImage(file='sprites/white/rook.png'), 'b': PhotoImage(file='sprites/white/bishop.png'),
    'n': PhotoImage(file='sprites/white/knight.png'), 'p': PhotoImage(file='sprites/white/pawn.png')
}

black_pieces = {
    'k': PhotoImage(file='sprites/black/king.png'), 'q': PhotoImage(file='sprites/black/queen.png'),
    'r': PhotoImage(file='sprites/black/rook.png'), 'b': PhotoImage(file='sprites/black/bishop.png'),
    'n': PhotoImage(file='sprites/black/knight.png'), 'p': PhotoImage(file='sprites/black/pawn.png')
}

canvas = tkinter.Canvas(master, bg='#0aa935', height=600, width=600)


def print_board():
    t = b.get_board()
    for x in range(8):
        for y in range(8):
            bg = cell_color(x, y)
            if t[x][y] is not None:
                px = 600 / 8 * y
                py = 600 / 8 * x
                if t[x][y].get_color() == WHITE:
                    tm = white_pieces
                else:
                    tm = black_pieces

                if isinstance(t[x][y], King):
                    (tkinter.Label(master, image=tm['k'], background=bg)
                     .place(x=px, y=py, height=75, width=75))
                elif isinstance(t[x][y], Queen):
                    (tkinter.Label(master, image=tm['q'], background=bg)
                     .place(x=px, y=py, height=75, width=75))
                elif isinstance(t[x][y], Rook):
                    (tkinter.Label(master, image=tm['r'], background=bg)
                     .place(x=px, y=py, height=75, width=75))
                elif isinstance(t[x][y], Bishop):
                    (tkinter.Label(master, image=tm['b'], background=bg)
                     .place(x=px, y=py, height=75, width=75))
                elif isinstance(t[x][y], Knight):
                    (tkinter.Label(master, image=tm['n'], background=bg)
                     .place(x=px, y=py, height=75, width=75))
                else:
                    (tkinter.Label(master, image=tm['p'], background=bg)
                     .place(x=px, y=py, height=75, width=75))

            else:
                canvas.create_rectangle((600 / 8 * y, 600 / 8 * x), (600 / 8 * (y + 1), 600 / 8 * (x + 1)), fill=bg)

print_board()

canvas.pack()
master.mainloop()
