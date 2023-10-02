import pygame
from No import *

no_selected = 0
user_text = ""

pygame.init()
clock = pygame.time.Clock()

display = pygame.display.set_mode((800, 400))

while True:
    display.fill("black")
    mouse_pos = pygame.mouse.get_pos()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    if pygame.mouse.get_pressed()[0]:
        no = No(mouse_pos)
    # pygame.draw.line(display, "white", feixe.origem, [feixe.origem[0] + x, feixe.origem[1] + y])
    pygame.draw.circle(display, "white", mouse_pos, 2)

    pygame.display.update()
    clock.tick(60)
