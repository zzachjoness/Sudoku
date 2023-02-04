from tkinter import *
import generate_Sudoku as gs


# Class for creating cells
class Cell():
    def __init__(self, v=None):
        self.value = v

# list for color matching numbers
colors = ['white smoke', 'light coral', 'khaki', 'pink', 'peach puff', 'lemon chiffon', 'steel blue2', 'plum2', 'pale green3']

# Function for creating a Frame of Cells
def mk_board(container, cell, data):
    brd_frame = Frame(container, borderwidth=.5, relief='solid')
    brd_frame.columnconfigure(0, weight=1, minsize=50)
    brd_frame.columnconfigure(1, weight=2, minsize=50)
    brd_frame.columnconfigure(2, weight=1, minsize=50)
    brd_frame.rowconfigure(0, weight=1, minsize=50)
    brd_frame.rowconfigure(1, weight=1, minsize=50)
    brd_frame.rowconfigure(2, weight=1, minsize=50)
    brd_frame.grid(column=cell % 3, row=cell//3, sticky='nsew')
    for i in range(9):
        number = data[i]
        field = Label(brd_frame, text=number, borderwidth=.5, relief='raised') #, background=colors[number-1]) #padding=10 removed
        field.grid(column=i % 3, row=i//3, sticky='nsew')

# Function for creating grid of Frames
def mk_grid(container):
    board = gs.Board()
    board.iterate_gen()
    board_frame = Frame(container, bg='white', borderwidth=1, relief='solid')
    board_frame.grid(row=0)
    for i in range(9):
        mk_board(board_frame, i, board.data[i])

#root window
root = Tk()  # creates and application window
root.title('Sudoku')
root.geometry('{}x{}'.format(800,550))
#root.resizable(True, True)

# create all of the main containers
top_frame = Frame(root, bg='cyan', width=550, height=150, pady=3)
center_frame = Frame(root, bg='lavender', width=550, height=300, pady=3)
btm_frame = Frame(root, bg='gray2', width=550, height=50, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky='ew')
center_frame.grid(row=1, sticky='nsew')
btm_frame.grid(row=2,stick='ew')


# create subframes for center frame
options_frame = Frame(center_frame, borderwidth=.5, relief=SOLID, background='light coral')
options_frame.grid(column=1, sticky='nsew')

# create widgets for the top frame
new_board_button = Button(top_frame, bg='red', text="New Board", height=2, width=10, command=lambda: mk_grid(center_frame))

# layout the widgets for the top frame
new_board_button.grid(row=0) #test with colspan

# create widgets for the center frame
mk_grid(center_frame)

# create widgets for the options frame
options_title = Label(options_frame, text='OPTIONS').grid(row=0, columnspan=3, sticky='nsew')
undo_button = Button(options_frame, text='undo').grid(row=1, column=0, sticky='nsew')
erase_button = Button(options_frame, text='erase').grid(row=1, column=1, sticky='nsew')
notes_button = Button(options_frame, text='notes').grid(row=1, column=2, sticky='nsew')



# create widgets for the btm frame
close_window = Button(btm_frame, text="Close Window", command=lambda: root.quit())

# layout widgets for the btm frame
close_window.grid(row=0, column=2)

root.mainloop()  # keeps the window visible on the screen
