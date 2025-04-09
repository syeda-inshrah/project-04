import pygame

pygame.init()

width , height = 400 , 400
cell_size = 40
erase_size = 20 

blue = (0, 0 , 255)
white = (255 , 255 , 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("erase tools")

def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, white, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, white, (0, y), (width, y))

running = True
while running:
    screen.fill(blue)
    draw_grid()

    mouse_x , mouse_y = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
      react_x = (mouse_x // cell_size) * cell_size
      react_y = (mouse_y // cell_size) * cell_size
      pygame.draw.rect(screen , white , (react_x , react_y , cell_size , cell_size))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    pygame.display.flip()

pygame.quit()