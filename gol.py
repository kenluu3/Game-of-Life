import pygame as pg
from grid import Grid

class GameOfLife:
  def __init__(self, cell_size=15, screen_size=(1440, 720)):
    pg.init()
    
    self.__update_map = {
      0: (0, 0),
      1: (1, 0),
      2: (0, 1),
      3: (1, 1),
    }
    
    self.__colors = {
      'bg': (255, 255, 255),
      'dead': (25, 25, 25),
      'alive_active': (0, 255, 0),
      'alive_inactive': (255, 0, 0),
    }
    
    self.__fps = 5
    self.__screen_size = screen_size
    self.__cell_size = cell_size
    self.__graphics = pg.display.set_mode(screen_size)
    self.__grid = Grid(screen_size[0] // cell_size, screen_size[1] // cell_size)
    self.__active = False
    
    pg.display.set_caption("Conway's Game of Life")
  
  def __del__(self):
    pg.quit()
  
  def game_state(self):
    return self.__grid

  def __neighbors(self, row, col):
    total_neighbors = 0
    
    neighboring_cells = [
      (-1, -1), (0, -1), (1, -1),
      (-1, 0), (1, 0),
      (-1, 1), (0, 1), (1, 1),
    ]
    
    for neighbor_row, neighbor_col in neighboring_cells:
      new_row = neighbor_row + row
      new_col = neighbor_col + col
      
      if new_row >= 0 and new_row < self.__grid.rows() and new_col >= 0 and new_col < self.__grid.cols():
        if self.__update_map[self.__grid.get(new_row, new_col)][0] == 1:
          total_neighbors += 1
          
    return total_neighbors

  def __update(self):            
    for row in range(self.__grid.rows()):
      for col in range(self.__grid.cols()):
        neighbors = self.__neighbors(row, col)
        
        if self.__update_map[self.__grid.get(row, col)][0] == 1:
          if neighbors < 2 or neighbors > 3:
            self.__grid.set(row, col, 1)
          else:
            self.__grid.set(row, col, 3)
        else:
          if neighbors == 3:
            self.__grid.set(row, col, 2)
    
    for row in range(self.__grid.rows()):
      for col in range(self.__grid.cols()):
        self.__grid.set(row, col, self.__update_map[self.__grid.get(row, col)][1])

  def __render(self):
    self.__graphics.fill(self.__colors['bg'])
    
    for row in range(self.__grid.rows()):
      for col in range(self.__grid.cols()):
        render_rect = (row * self.__cell_size, col * self.__cell_size, self.__cell_size - 1, self.__cell_size - 1)
        color = self.__colors['dead']
        
        if self.__grid.get(row, col) == 1:
          if self.__active:
            color = self.__colors['alive_active']
          else:
            color = self.__colors['alive_inactive']
        
        pg.draw.rect(self.__graphics, color, render_rect)
      
    pg.display.update()
    
  def start_game(self):
    clock = pg.time.Clock()
    
    running = True
    
    while running:
      clock.tick(self.__fps)
      
      for event in pg.event.get():
        if event.type == pg.QUIT:
          running = not running
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_SPACE:
            self.__active = not self.__active
      
      if pg.mouse.get_pressed()[0]:
        cell_row, cell_col = pg.mouse.get_pos()
        self.__grid.set(cell_row // self.__cell_size, cell_col // self.__cell_size, 1)
      
      if self.__active:
        self.__update()
        
      self.__render()
      
        
          
    