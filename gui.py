from tkinter import *
from tkinter import ttk
import json
import random
import generate_Sudoku as gs


# Class for creating cells
class Cell():
    def __init__(self, v=None):
        self.value = v

# list for color matching numbers
colors = ['white smoke', 'light coral', 'khaki', 'pink', 'peach puff', 'lemon chiffon', 'steel blue2', 'plum2', 'pale green3']

# list of board cells buttons
board_cells = []

# Function for updating board buttons
# NOT SURE IF THIS IS REQUIRED/USABLE
'''def update_cell(cell, i, n):
    print(f'cell{cell}, i{i}, num{n}')
    cell_button = board_cells[cell*9 +i]
    cell_button.config(text=n+1) # need to take input from options section
    board_cells[cell*9+i] = cell_button'''
# function for coloring active button cell
def set_active_cell(button, board, cell):
    print(board,cell)
    global selected_button
    if selected_button is not None:
        selected_button.config(bg='yellow')
    button.config(bg='light blue')
    selected_button = button


### CHANGE SELECTED BUTTON
def change_selected_button(button):
    global selected_button
    if selected_button is not None:
        selected_button.config(bg='white')
    button.config(highlightbackground='light blue')
    selected_button = button


# Function for creating a Frame of Cells
def mk_board(container, cell, data):
    brd_frame = Frame(container, borderwidth=.5, relief='solid')
    brd_frame.columnconfigure(0, weight=1, minsize=50)
    brd_frame.columnconfigure(1, weight=1, minsize=50)
    brd_frame.columnconfigure(2, weight=1, minsize=50)
    brd_frame.rowconfigure(0, weight=1, minsize=50)
    brd_frame.rowconfigure(1, weight=1, minsize=50)
    brd_frame.rowconfigure(2, weight=1, minsize=50)
    brd_frame.grid(column=cell % 3, row=cell//3, sticky='nsew')
    for i in range(9):
        number = data[i]
        user_guess = int
        #### FIELD WILL NEED TO BE A LABEL OR A CUSTOM BUTTON CLASS ####
        field = Button(brd_frame, highlightthickness=0, border=0, borderwidth=0,height=3,width=3, highlightbackground='white smoke', text=number)
        field.grid(column=i % 3, row=i//3, sticky='nsew')
        field.config(command=lambda button=field, i=i: set_active_cell(button, cell, i ))
        board_cells.append(field)

# Function for creating grid of Frames
def mk_grid(container):
    with open('unique_Puzzles.JSON', encoding='utf-8') as f:
        unique_puzzles = f.read()
    unique_puzzles_list = json.loads(unique_puzzles)
    rn = random.randrange(len(unique_puzzles_list)-1)
    random_puzzle = unique_puzzles_list[rn]
    board_frame = Frame(container, bg='white', borderwidth=1, relief='solid')
    board_frame.grid(row=0)
    for i in range(9):
        mk_board(board_frame, i, random_puzzle['puzzle'][i])

#root window
root = Tk()  # creates and application window
root.title('Sudoku')
root.geometry('{}x{}'.format(800,600))
#root.resizable(True, True)
# set selected button to None
selected_button = None
# create all of the main containers
top_frame = Frame(root, bg='cyan', width=550, height=150, pady=3)
center_frame = Frame(root, bg='lavender', width=550, height=200, pady=3)
btm_frame = Frame(root, bg='gray2', width=550, height=50, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky='ew')
center_frame.grid(row=1, sticky='nsew')
btm_frame.grid(row=2,stick='ew')


# create subframes for center frame
options_frame = Frame(center_frame, borderwidth=.5, relief=SOLID)
options_frame.grid(column=1, sticky='nsew')

# create subframes for options frame
button_frame = Frame(options_frame)
button_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='ns')
number_select_frame = Frame(options_frame)
number_select_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

# create widgets for the top frame
new_board_button = Button(top_frame, bg='red', text="New Board", height=2, width=10, command=lambda: mk_grid(center_frame))

# layout the widgets for the top frame
new_board_button.grid(row=0) #test with colspan

# create widgets for the center frame
mk_grid(center_frame)

# create widgets for the options frame
options_title = Label(options_frame, text='OPTIONS').grid(row=0, columnspan=3, sticky='ns')
undo_button = Button(button_frame, width=5, text='undo').grid(row=0, column=0, sticky='ns')
erase_button = Button(button_frame,width=5,  text='erase').grid(row=0, column=1, sticky='ns')
notes_button = Button(button_frame,width=5,  text='notes').grid(row=0, column=2, sticky='ns')
one = Button(number_select_frame, text=1, height= 5, width=5)
one.grid(row=0, column=0, sticky='nsew')
one.config(command= lambda button=one: change_selected_button(button))
two = Button(number_select_frame, text=2, height= 5, width=5)
two.grid(row=0, column=1, sticky='nsew')
two.config(command= lambda button=two: change_selected_button(button))
three = Button(number_select_frame, text=3, height= 5, width=5).grid(row=0, column=2, sticky='nsew')
four = Button(number_select_frame, text=4, height= 5, width=5).grid(row=1, column=0, sticky='nsew')
five = Button(number_select_frame, text=5, height= 5, width=5).grid(row=1, column=1, sticky='nsew')
six = Button(number_select_frame, text=6, height= 5, width=5).grid(row=1, column=2, sticky='nsew')
seven = Button(number_select_frame, text=7, height= 5, width=5).grid(row=2, column=0, sticky='nsew')
eight = Button(number_select_frame, text=8, height= 5, width=5).grid(row=2, column=1, sticky='nsew')
nine = Button(number_select_frame, text=9, height= 5, width=5).grid(row=2, column=2, sticky='nsew')

# create widgets for the btm frame
close_window = Button(btm_frame, text="Close Window", command=lambda: root.quit())

# layout widgets for the btm frame
close_window.grid(row=0, column=2)

root.mainloop()  # keeps the window visible on the screen
