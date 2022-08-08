import copy
import pygame as pg

bg_color = (140, 140, 140)
cell_dead = (25, 25, 25)
cell_color_active = (0, 255, 0)
cell_color_disabled = (255, 0, 0)
block_size = 10

def num_alive(matrix, r, c):
  rows = len(matrix)
  cols = len(matrix[0])
  
  neighbors = [
    [-1,-1], [0,-1], [1,-1], 
    [-1,0], [1,0], 
    [-1,1], [0,1], [1,1]
  ]
  
  num_neighbours = 0
  
  for dir_x, dir_y in neighbors:
    x_mod = dir_x + r
    y_mod = dir_y + c
    
    if x_mod >= 0 and x_mod <= rows - 1 and y_mod >= 0 and y_mod <= cols - 1:
      if matrix[x_mod][y_mod] == 1:
        num_neighbours += 1
          
  return num_neighbours

def game_of_life(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  
  old_matrix = copy.deepcopy(matrix)
  
  for r in range(rows):
    for c in range(cols):
      neighbors = num_alive(old_matrix, r, c)
          
      if old_matrix[r][c] == 1:
        if neighbors == 2 or neighbors == 3:
          matrix[r][c] = 1
        else:
          matrix[r][c] = 0
      else:
        if neighbors == 3:
          matrix[r][c] = 1
        
  return matrix
              
def grid(window, matrix, playing=True):
  rows = len(matrix)
  cols = len(matrix[0])
  
  if playing:
    matrix = game_of_life(matrix)
  
  for r in range(rows):
    for c in range(cols):
      if matrix[r][c] == 0:
        pg.draw.rect(window, cell_dead, (r * 10, c * 10, block_size - 1, block_size - 1))
      else:
        if playing:
          pg.draw.rect(window, cell_color_active, (r * 10, c * 10, block_size - 1, block_size - 1))
        else:
          pg.draw.rect(window, cell_color_disabled, (r * 10, c * 10, block_size - 1, block_size - 1))

def main():  
  pg.init()
  size = (800, 600)  
  
  matrix = [[0] * 60 for i in range(80)] 
  
  fps = 5
  window = pg.display.set_mode(size)
  clock = pg.time.Clock()
  pg.display.set_caption('Game of Life')
  
  running = True
  playing = False
  while running:
    clock.tick(fps)
    
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False    
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE:
          playing = not playing
    
    if pg.mouse.get_pressed()[0]:
      (update_x, update_y) = pg.mouse.get_pos()
      matrix[update_x // 10][ update_y // 10] = 1
    
    window.fill(bg_color)
    grid(window, matrix, playing)
        
    pg.display.update()
      
  pg.quit()
  
  return 0

if __name__ == '__main__':
  main()
  
'''
  [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
'''