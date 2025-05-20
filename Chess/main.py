import tkinter
from tkinter import PhotoImage
from tkinter import messagebox as mb

from board import *

LIGHT = '#ec972a'
DARK = '#372207'
G_LIGHT = '#08f02b'
G_DARK = '#0b9e21'
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
master.iconbitmap('sprites/icon.ico')
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
    canvas.delete('all')
    t = b.get_board()
    for x in range(8):
        for y in range(8):
            bg = cell_color(x, y)

            lt = (WIDTH // 8 * y, HEIGHT // 8 * x)
            rb = (WIDTH // 8 * (y + 1), HEIGHT // 8 * (x + 1))
            canvas.create_rectangle(lt, rb, fill=bg)
            if b.chosen is not None:
                if (x, y) == b.chosen:
                    if cell_color(x, y) == LIGHT:
                        cl = G_LIGHT
                    else:
                        cl = G_DARK
                    canvas.create_rectangle(lt, rb, fill=cl)

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


def click(event):
    x, y = event.y // (HEIGHT // 8), event.x // (WIDTH // 8)
    cell = b.get_board()[x][y]
    if b.chosen is None:
        if cell is not None and cell.get_color() == b.cpc:
            b.chosen = (x, y)
            print_board()
    else:
        if (x, y) == b.chosen:
            b.chosen = None
            print_board()
        else:
            if b.move_piece(b.chosen[0], b.chosen[1], x, y):
                b.chosen = None
                if b.cpc == WHITE:
                    master.title('Chess  -  Ход белых')
                else:
                    master.title('Chess  -  Ход чёрных')
                print_board()

                if b.cpc == BLACK and b.is_under_attack(b.w_king_cords[0], b.w_king_cords[1], WHITE):
                    msg = 'Чёрные победили'
                    mb.showinfo('Окончание игры', msg)
                elif b.cpc == WHITE and b.is_under_attack(b.b_king_cords[0], b.b_king_cords[1], BLACK):
                    msg = 'Белые победили'
                    mb.showinfo('Окончание игры', msg)


canvas.bind('<Button-1>', click)
master.title('Chess  -  Ход белых')
print_board()

canvas.pack(expand=True, fill=tkinter.BOTH)
master.mainloop()
