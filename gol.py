from grid import Grid

class GameOfLife:
  def __init__(self, dimensions=(60,80)):
    self.grid = Grid(dimensions[0], dimensions[1])
    self.active = False
    
  def __neighbors(self, row, col):
    total_neighbors = 0
    
    neighboring_cells = [
      [-1, -1], [0, -1], [1, -1]
      [-1, 0], [1, 0]
      [-1, 1], [0, 1], [1, 1]
    ]
    
    for neighbor_row, neighbor_col in neighboring_cells:
      new_row = neighbor_row + row
      new_col = neighbor_col + col
      
      if new_row >= 0 and new_row < self.grid.rows and new_col >= 0 and new_col < self.grid.cols:
        if self.grid.get(new_row, new_col) == 1:
          total_neighbors += 1
          
    return total_neighbors
  
  def update(self):
    prev_state = self.grid.copy()
    
    for row in range(self.grid.rows()):
      for col in range(self.grid.cols()):
        neighbors = self.__neighbors(row, col)
        
        if prev_state[row, col] == 1:
          if neighbors < 2 or neighbors > 3:
            self.grid.set(row, col, 0)
        else:
          if neighbors == 3:
            self.grid.set(row, col, 1)