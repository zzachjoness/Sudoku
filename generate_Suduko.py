import random

def say_hello():
  print("hi from generate")

class Board():
  def __init__(self):
    self.data = []
    self.msg = 'hi'
    
  def get_row(sub_block,row):
    row_list = []
    sb = sub_block + 1
    board_col = sb // 3
    return row_list


  def generate(self):
    for i in range(9):
      self.data.append([])
      for j in range(1,10):
        unique_number = False
        sub_block = i
        fc_loc = j
        row = j // 3
        col = j % 3
        while unique_number == False:
          fc = random.randrange(1,10,1) # fixed cell = random number 1-9(inclusive)
          if fc not in self.data[sub_block]: # fixed cell no in sub-block
            if fc not in get_row(sub_block,row): # fixec cell not in row
              if fc not in get_col(sub_block,col): # fixed cell not in col
                unique_number = True
                self.data[i].append(fc)

  def show(self):
    print(self.msg,self.data)
  