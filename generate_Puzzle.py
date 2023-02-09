import random
import copy
import json

class Puzzle():

    nbn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]

    def __init__(self, board):
        self.solution = copy.deepcopy(board)
        self.puzzle = board
        self.difficulty = 0
    
    def show(self):
        print('puzzle solution: ',id(self.solution), ' - ', self.solution)
        print('puzzle id: ',id(self.puzzle), ' - ', self.puzzle)
        print('difficluty ', self.difficulty)

    def save_puzzle(self):
        with open('unique_Puzzles.JSON', encoding='utf-8') as f:
            read_data = f.read()

    def remove_spaces(self):
        for i in range(56):
            rn = random.randrange(len(self.nbn)) #random number
            rc = self.nbn[rn] #random cell for removal
            del self.nbn[rn]
            # function for finding cell via rc
            i = rc // 9
            j = rc % 9
            self.puzzle[i][j] = ''


def create_Puzzle():

    with open('unique_Boards.JSON', encoding='utf-8') as f:
        read_data = f.read()
    boards = json.loads(read_data)
    rn = random.randrange(len(boards))
    board = boards[rn]
    # 9 x 9 array => 81 cells, hardest solveable problem 17 knowns
    # expert leave 23-25 cells -> remove 56 cells
    puzzle = Puzzle(board)
    puzzle.remove_spaces()
    add_puzzle_obj = {'solution': puzzle.solution, 'puzzle': puzzle.puzzle}
    with open('unique_Puzzles.JSON', encoding='utf-8') as f:
        unique_puzzles = f.read()
    unique_puzzles_list = json.loads(unique_puzzles)
    unique_puzzles_list.append(add_puzzle_obj)
    with open('unique_Puzzles.JSON', 'w', encoding='utf-8') as f:
        json.dump(unique_puzzles_list, f)
    

create_Puzzle()