import pygame as pg
from grid import Grid

class GameOfLife:
  def __init__(self, cell_size=20, screen_size=(1280, 720)):
    pg.init()
    
    self.__colors = {
      'bg': (255, 255, 255),
      'dead': (25, 25, 25),
      'alive_active': (0, 255, 0),
      'alive_inactive': (255, 0, 0),
    }
    
    self.__screen_size = screen_size
    self.__cell_size = cell_size
    self.__graphics = pg.display.set_mode(screen_size)
    self.__grid = Grid(screen_size[1] // cell_size, screen_size[0] // cell_size)
    self.__active = False
    
    pg.display.set_caption("Conway's Game of Life")
  
  def __del__(self):
    pg.quit()
  
  def state(self):
    return self.__grid

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
      
      if new_row >= 0 and new_row < self.__grid.rows and new_col >= 0 and new_col < self.__grid.cols:
        if self.__grid.get(new_row, new_col) == 1:
          total_neighbors += 1
          
    return total_neighbors
  
  def __update(self):    
    prev_state = self.__grid.copy()
    
    for row in range(self.__grid.rows()):
      for col in range(self.__grid.cols()):
        neighbors = self.__neighbors(row, col)
        
        if prev_state[row, col] == 1:
          if neighbors < 2 or neighbors > 3:
            self.__grid.set(row, col, 0)
        else:
          if neighbors == 3:
            self.__grid.set(row, col, 1)
  
  def __render(self):
    self.__graphics.fill(self.__colors['bg'])
    
    for row in range(self.grid.rows()):
      for col in range(self.grid.cols()):
        render_rect = (row * self.__cell_size, col * self.__cell_size, self.__cell_size - 1, self.__cell_size - 1)
        color = self.__colors['dead']
        
        if self.__grid.get(row, col) == 1:
          if self.__active:
            color = self.__colors['alive_active']
          else:
            color = self.__colors['alive_inactive']
        
        pg.draw.rect(self.__graphics, render_rect, color)  