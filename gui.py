from tkinter import *
import generate_Sudoku as gs


# Class for creating cells
class Cell():
    def __init__(self, v=None):
        self.value = v


# Function for creating a Frame of Cells
def mk_board(containter, cell, data):
    frame = Frame(containter)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.grid(column=cell % 3, row=cell//3)
    for i in range(9):
        field = Label(frame, background='#0c3800', text=data[i], padx=10, pady=10, width=1,border=1, relief='sunken') #padding=10 removed
        field.grid(column=i % 3, row=i//3)

# Function for creating grid of Frames
def mk_grid(container):
    board = gs.Board()
    board.iterate_gen()
    for i in range(9):
        mk_board(container, i, board.data[i])

#root window
root = Tk()  # creates and application window
root.title('Sudoku')
root.geometry('{}x{}'.format(460,600))
#root.resizable(True, True)

# create all of the main containers
top_frame = Frame(root, bg='cyan', width=450, height=50, pady=3)
center_frame = Frame(root, bg='lavender', width=450, height=300, pady=3)
btm_frame = Frame(root, bg='gray2', width=450, height=50, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky='ew')
center_frame.grid(row=1, sticky='nsew')
btm_frame.grid(row=2,stick='ew') #test row 2 vs row 3 vs row 4

# create widgets for the top frame
new_board_button = Button(top_frame, bg='red', text="New Board", command=lambda: mk_grid(center_frame))

# layout the widgets for the top frame
new_board_button.grid(row=0) #test with colspan


# create widgets for the btm frame
close_window = Button(btm_frame, text="Close Window", command=lambda: root.quit())

# layout widgets for the btm frame
close_window.grid(row=0, column=2)

root.mainloop()  # keeps the window visible on the screen

# object for creating cells
