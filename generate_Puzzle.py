import random
import json

class Puzzle():

    def __init__(self, board):
        self.solution = board
        self.puzzle = []
        self.difficulty = 0
    
    def show(self):
        print('solution: ', self.solution)
        print('puzzle: ', self.puzzle)
        print('difficluty ', self.difficulty)

    def save_puzzle(self):
        with open('unique_Boards.JSON', encoding='utf-8') as f:
            read_data = f.read()
        print(f.read)



def create_Puzzle():

    with open('unique_Boards.JSON', encoding='utf-8') as f:
        read_data = f.read()
    boards = json.loads(read_data)
    rn = random.randrange(len(boards))
    board = boards[rn]
    print(board)
    # 9 x 9 array => 81 cells, hardest solveable problem 17 knowns
    # expert leave 23-25 cells
    # replace number with NONE
    # save solution and puzzle together in same object
    

create_Puzzle()