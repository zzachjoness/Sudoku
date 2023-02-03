import random
import json



class Board():
  def __init__(self):
    self.data = []
    self.count = 0
  def reset(self):
    self.data = []
    self.count += 1

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
        count = 0
        while len(self.data[i]) < j + 1 :
          dice = random.randrange(len(choices))
          fc = choices[dice]
          if fc not in row_list: # fixed cell not in row
            if fc not in col_list: # fixed cell not in col
              self.data[i].append(fc)
              del choices[dice]
              last_len = len(choices)
          if len(choices) > 0 and count > len(choices)*10:
            self.reset()
            return False
          count += 1
    return True
  
  def iterate_gen(self):
    full_board = False
    while full_board == False:
      full_board = self.generate()
    with open('unique_boards.json', encoding='utf-8') as f:
      read_data = f.read()
    unique_boards = json.loads(read_data)
    if self.data not in unique_boards:
      unique_boards.append(self.data)
      print(f'there are {len(unique_boards)} ubs')
      with open('unique_boards.json', 'w', encoding='utf-8') as f:
        json.dump(unique_boards, f)

  def show(self):
    print(self.data)
  
