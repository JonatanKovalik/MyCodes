import pygame

boolean = True
pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("My firs game!")

plrcolor = 'white'
plr_x = 100
plr_y = 200
plr_width = 200
plr_height = 100

while boolean: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boolean = False
    screen.fill((0,0,0))
    pygame.draw.rect(screen, plrcolor, (plr_x, plr_y, plr_width, plr_height))
    pygame.display.flip()
pygame.quit()