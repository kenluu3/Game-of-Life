from copy import deepcopy

class Grid:
  def __init__(self, rows=0, cols=0):
    self.__rows = rows
    self.__cols = cols
    self.__matrix = [[0] * cols for _ in range(rows)]  

  def set(self, row, col, value):
    if row >= 0 and row < self.__rows and col >= 0 and col < self.__cols:
      self.__matrix[row][col] = value
  
  def get(self, row, col):
    if row >= 0 and row < self.__rows and col >= 0 and col < self.__cols:
      return self.__matrix[row][col]
  
  def copy(self):
    return deepcopy(self.__matrix)

  def cols(self):
    return self.__cols

  def rows(self):
    return self.__rows
    
  def print_grid(self):
    for row in range(self.__rows):
      for col in range(self.__cols):
        print(self.__matrix[row][col], end=' ')
      
      print()