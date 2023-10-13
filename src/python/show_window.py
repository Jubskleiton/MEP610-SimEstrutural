import pygame
from Elemento import *

pygame.NOFRAME = True
pygame.RESIZABLE = True


def show(elements: [Elemento], dislocation, gls):
    scale = 100
    desl_scale = 1

    pygame.init()
    clock = pygame.time.Clock()

    display = pygame.display.set_mode((600, 400))

    while True:
        display.fill("black")
        mouse_pos = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    desl_scale += 1
                if evento.key == pygame.K_s:
                    desl_scale -= 1
                print(desl_scale)
        if pygame.mouse.get_pressed()[0]:
            print(mouse_pos)
        # pygame.draw.circle(display, "white", mouse_pos, 2)

        draw_elements(display, elements, scale)

        draw_elements(display, elements, scale, ds=dislocation, gls=gls, desl_scale=desl_scale)

        pygame.display.update()
        clock.tick(60)


def draw_elements(display, elements: list[Elemento], scale, ds: list[float]=False, gls: list[Gl]=False, desl_scale=1):
    if ds is False:
        for element in elements:
            pygame.draw.line(display, "white", [display.get_width()/2 + (element.no1.gl[0].pos * scale),  display.get_height()/2 - (element.no1.gl[1].pos * scale)], [display.get_width()/2 + (element.no2.gl[0].pos * scale), display.get_height()/2 - (element.no2.gl[1].pos * scale)])
            pygame.draw.circle(display, "white", [display.get_width()/2 + (element.no1.gl[0].pos * scale), display.get_height()/2 - (element.no1.gl[1].pos * scale)], 2)
            pygame.draw.circle(display, "white", [display.get_width()/2 + (element.no2.gl[0].pos * scale), display.get_height()/2 - (element.no2.gl[1].pos * scale)], 2)
    else:
        for i, element in enumerate(elements):
            pygame.draw.line(display, "red", [display.get_width()/2 + (element.no1.gl[0].pos * scale + ds[gls.index(element.no1.gl[0])] * desl_scale), display.get_height()/2 - (element.no1.gl[1].pos * scale + ds[gls.index(element.no1.gl[1])] * desl_scale)], [display.get_width()/2 + (element.no2.gl[0].pos * scale + ds[gls.index(element.no2.gl[0])] * desl_scale), display.get_height()/2 - (element.no2.gl[1].pos * scale + ds[gls.index(element.no2.gl[1])] * desl_scale)])
            pygame.draw.circle(display, "red", [display.get_width()/2 + (element.no1.gl[0].pos * scale + ds[gls.index(element.no1.gl[0])] * desl_scale), display.get_height()/2 - (element.no1.gl[1].pos * scale + ds[gls.index(element.no1.gl[1])] * desl_scale)], 2)
            pygame.draw.circle(display, "red", [display.get_width() / 2 + (element.no2.gl[0].pos * scale + ds[gls.index(element.no2.gl[0])] * desl_scale), display.get_height()/2 - (element.no2.gl[1].pos * scale + ds[gls.index(element.no2.gl[1])] * desl_scale)], 2)

