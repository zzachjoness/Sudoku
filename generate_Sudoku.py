import random

def say_hello():
  print("hi from generate")

class Board():
  def __init__(self):
    self.data = []
    self.msg = 'hi'
  def reset(self):
    self.data = []

  def get_row(self, sub_block,fc):
    board_col = sub_block % 3
    sb_row = fc // 3 # sub_block row based upon position of fixed cell
    if board_col == 0:
      return []
    row_list = []
    for i in range(sub_block - board_col, sub_block):
      if len(self.data) >= i:
        for j in range(sb_row * 3, sb_row * 3 + 3):
          if len(self.data[i]) >= j:
            row_list.append(self.data[i][j])  
    return row_list
  
  def get_col(self, sub_block, fc):
    board_row = sub_block // 3
    if board_row == 0:
      return []
    col_list = []
    sb_col = fc % 3
    for i in range(sub_block - board_row * 3, sub_block, 3):
      if len(self.data) >= i:
        for j in range(sb_col, sb_col + 7, 3):
          if len(self.data[i]) >= j:
            col_list.append(self.data[i][j])
    return col_list

  # next to do, if failure, start over
  def generate(self):
    for i in range(9):
      self.data.append([])
      choices = [1,2,3,4,5,6,7,8,9]
      last_len = len(choices)
      for j in range(9):
        sub_block = i
        fc = j
        row_list = self.get_row(sub_block, fc)
        col_list = self.get_col(sub_block, fc)
        while len(self.data[i]) < j + 1 :
          dice = random.randrange(len(choices))
          fc = choices[dice]
          if fc not in row_list: # fixed cell not in row
            if fc not in col_list: # fixed cell not in col
              self.data[i].append(fc)
              del choices[dice]
              last_len = len(choices)
          print(last_len)
        
    print('done: ',self.data)

  def show(self):
    print(self.msg,self.data)


one = Board()
one.generate()

