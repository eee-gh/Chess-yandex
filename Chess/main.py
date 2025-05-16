import tkinter
from tkinter import PhotoImage

from board import *

LIGHT = '#ec972a'
DARK = '#372207'
WHITE = 0
BLACK = 1
WIDTH = 560
HEIGHT = 560


def cell_color(xn, yn):
    if (xn + yn) % 2:
        return DARK
    return LIGHT


b = Board()
master = tkinter.Tk()
master.title('Chess')
master.geometry(f'{WIDTH}x{HEIGHT}')
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

canvas = tkinter.Canvas(master, bg='#0aa935', relief=tkinter.FLAT)


def print_board():
    t = b.get_board()
    for x in range(8):
        for y in range(8):
            bg = cell_color(x, y)

            lt = (WIDTH // 8 * y, HEIGHT // 8 * x)
            rb = (WIDTH // 8 * (y + 1), HEIGHT // 8 * (x + 1))
            canvas.create_rectangle(lt, rb, fill=bg)

            if t[x][y] is not None:
                px = HEIGHT // 8 * y
                py = WIDTH // 8 * x
                if t[x][y].get_color() == WHITE:
                    tm = white_pieces
                else:
                    tm = black_pieces

                if isinstance(t[x][y], King):
                    canvas.create_image(px, py, anchor=tkinter.NW, image=tm['k'])
                elif isinstance(t[x][y], Queen):
                    canvas.create_image(px, py, anchor=tkinter.NW, image=tm['q'])
                elif isinstance(t[x][y], Rook):
                    canvas.create_image(px, py, anchor=tkinter.NW, image=tm['r'])
                elif isinstance(t[x][y], Bishop):
                    canvas.create_image(px, py, anchor=tkinter.NW, image=tm['b'])
                elif isinstance(t[x][y], Knight):
                    canvas.create_image(px, py, anchor=tkinter.NW, image=tm['n'])
                else:
                    canvas.create_image(px, py, anchor=tkinter.NW, image=tm['p'])


canvas.pack(expand=True, fill=tkinter.BOTH)
master.mainloop()
