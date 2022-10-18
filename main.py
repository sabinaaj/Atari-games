import pygame

import pong

pygame.init()

WIDTH, HEIGHT = 1400, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Atari games')

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_heading(win):
    font = pygame.font.Font(None, 150)
    text_on_display = font.render('ATARI GAMES', True, WHITE)
    text_rect = text_on_display.get_rect()
    text_rect.center = (WIDTH / 2, HEIGHT / 5)
    win.blit(text_on_display, text_rect)


def draw_button(win, text, y_pos):
    font = pygame.font.Font(None, 75)
    text_on_display = font.render(text, True, WHITE)
    text_rect = text_on_display.get_rect()
    text_rect.center = (WIDTH / 2, HEIGHT / 5 * y_pos)
    win.blit(text_on_display, text_rect)
    return text_rect

def gamemode_menu(chosen_game):
    run = True

    while run:
        pygame.time.Clock().tick(FPS)
        WIN.fill(BLACK)

        mouse_pos = pygame.mouse.get_pos()

        singleplayer_rect = draw_button(WIN, 'SINGLEPLAYER', 2)
        if singleplayer_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>SINGLEPLAYER<',  2)

        multiplayer_rect = draw_button(WIN, 'MULTIPLAYER',  3)
        if multiplayer_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>MULTIPLAYER<',  3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if singleplayer_rect.collidepoint(mouse_pos):
                    pong.gameloop(WIN)
                if multiplayer_rect.collidepoint(mouse_pos):
                    pong.gameloop(WIN)

        pygame.display.update()


def main():
    run = True

    while run:
        pygame.time.Clock().tick(FPS)
        WIN.fill((0, 0, 0))
        draw_heading(WIN)

        mouse_pos = pygame.mouse.get_pos()

        pacman_rect = draw_button(WIN, 'PACMAN',  2)
        if pacman_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>PACMAN<',  2)

        pong_rect = draw_button(WIN, 'PONG',  3)
        if pong_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>PONG<',  3)

        space_rect = draw_button(WIN, 'SPACE INVADERS',  4)
        if space_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>SPACE INVADERS<',  4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pacman_rect.collidepoint(mouse_pos):
                    gamemode_menu(1)
                if pong_rect.collidepoint(mouse_pos):
                    gamemode_menu(2)
                if space_rect.collidepoint(mouse_pos):
                    gamemode_menu(3)

        pygame.display.update()


if __name__ == '__main__':
    main()
