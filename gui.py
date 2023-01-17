import tkinter as tk
from tkinter import ttk


# Class for creating cells
class Cell():
    def __init__(self, v=None):
        self.value = v


# Function for creating a Frame of Cells
def mk_board(containter, cell):
    frame = ttk.Frame(containter)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.grid(column=cell % 3, row=cell//3)
    for i in range(9):
        field = ttk.Label(frame, text=cell*i+cell+i, width=5)
        field.grid(column=i % 3, row=i//3)

# Function for creating grid of Frames


def mk_grid(container):
    for i in range(9):
        mk_board(container, i)


# root window
root = tk.Tk()  # creates and application windon
root.geometry('400x400')
root.resizable(True, True)
root.title('Sudoku')
# set root grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

mk_grid(root)

root.mainloop()  # keeps the window visible on the screen

# object for creating cells
