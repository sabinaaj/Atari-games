import pygame

WIDTH, HEIGHT = 1400, 1000
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def gameloop(win):
    run = True

    while run:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()