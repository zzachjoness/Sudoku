import random

def say_hello():
  print("hi from generate")

class Board():
  def __init__(self):
    self.data = []
    self.msg = 'hi'

  def get_row(self, sub_block,row):
    board_col = sub_block % 3
    if board_col == 0:
      return []
    print(self.data)
    row_list = []
    sb_row = (row // 3) * 3
    for i in range(sub_block - board_col, sub_block):
      print('i: ', i)
      if len(self.data) >= i:
        for j in range(sb_row, sb_row + 3):
          if len(self.data[i]) >= j:
            row_list.append(self.data[i][j])
    print('should be done, here is your row list: ', row_list)
    return row_list
  
  def get_col(self, sub_block,col):
    if len(self.data) <= 1:
      return []
    col_list = []
    board_row = (sub_block % 3)
    sb_row = (col // 3)
    for i in range(board_row, board_row + 7, 3):
      if len(self.data) >= i:
        for j in range(sb_row, sb_row + 7, 3):
          if len(self.data[i]) >= j:
            col_list.append(self.data[i][j])
            print(col_list)
    return col_list


  def generate(self):
    for i in range(9):
      self.data.append([])
      for j in range(9):
        print('running new loop, j: ', j)
        sub_block = i
        fc = j
        row = j // 3
        col = j % 3
        row_list = self.get_row(sub_block, row)
        col_list = self.get_col(sub_block, col)
        while len(self.data[i]) < j + 1 :
          fc = random.randrange(1,10,1) # fixed cell = random number 1-9(inclusive)
          if fc not in self.data[sub_block]: # fixed cell no in sub-block
            if fc not in row_list: # fixed cell not in row
              if fc not in col_list: # fixed cell not in col
                self.data[i].append(fc)
    print(self.data)

  def show(self):
    print(self.msg,self.data)


one = Board()
one.generate()

