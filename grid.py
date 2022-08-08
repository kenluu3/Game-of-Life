from copy import deepcopy

class Grid:
  def __init__(self, rows=0, cols=0):
    self.rows = rows
    self.cols = cols
    self.matrix = [[0] * cols for _ in range(rows)]  

  def set(self, row, col, value):
    if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
      self.matrix[row, col] = value
  
  def get(self, row, col):
    if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
      return self.matrix[row, col]
  
  def copy(self):
    return deepcopy(self.matrix)

  def cols(self):
    return self.cols

  def rows(self):
    return self.rows
    
  def print_grid(self):
    for row in range(self.rows):
      for col in range(self.cols):
        print(self.matrix[row][col], end=' ')
      
      print()