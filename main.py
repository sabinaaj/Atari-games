import pygame

import pong
import space_invaders

pygame.init()

WIDTH, HEIGHT = 1400, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Atari games')

FPS = 60
WHITE = (255, 255, 255)
DARK_GRAY = (18, 18, 18)


# Draws given text on display
def draw_text(win, text, x, y, size):
    font = pygame.font.Font('assets/font/retro_game.ttf', size)
    text_on_display = font.render(text, True, WHITE)
    text_rect = text_on_display.get_rect()
    text_rect.center = (x, y)
    win.blit(text_on_display, text_rect)
    return text_rect


# Shows first screen of game menu, where you can choose game
def main():
    run = True

    while run:
        pygame.time.Clock().tick(FPS)
        WIN.fill(DARK_GRAY)
        draw_text(WIN, 'ATARI GAMES', WIDTH / 2, HEIGHT / 5, 125)

        mouse_pos = pygame.mouse.get_pos()

        pacman_rect = draw_text(WIN, 'PACMAN', WIDTH / 2, HEIGHT / 5 * 2, 60)
        if pacman_rect.collidepoint(mouse_pos):
            draw_text(WIN, '>PACMAN<', WIDTH / 2, HEIGHT / 5 * 2, 60)

        pong_rect = draw_text(WIN, 'PONG', WIDTH / 2, HEIGHT / 5 * 3, 60)
        if pong_rect.collidepoint(mouse_pos):
            draw_text(WIN, '>PONG<', WIDTH / 2, HEIGHT / 5 * 3, 60)

        space_rect = draw_text(WIN, 'SPACE INVADERS', WIDTH / 2, HEIGHT / 5 * 4, 60)
        if space_rect.collidepoint(mouse_pos):
            draw_text(WIN, '>SPACE INVADERS<', WIDTH / 2, HEIGHT / 5 * 4, 60)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pacman_rect.collidepoint(mouse_pos):
                    run = False
                if pong_rect.collidepoint(mouse_pos):
                    run = False
                    gamemode_menu()
                if space_rect.collidepoint(mouse_pos):
                    run = False
                    space_invaders.gameloop(WIN)


# Shows screen of menu, where you can choose how many players are playing
def gamemode_menu():
    run = True

    while run:
        pygame.time.Clock().tick(FPS)
        WIN.fill(DARK_GRAY)
        draw_text(WIN, 'PONG', WIDTH / 2, HEIGHT / 5, 125)

        mouse_pos = pygame.mouse.get_pos()

        singleplayer_rect = draw_text(WIN, 'SINGLEPLAYER', WIDTH / 2, HEIGHT / 5 * 2, 60)
        if singleplayer_rect.collidepoint(mouse_pos):
            draw_text(WIN, '>SINGLEPLAYER<', WIDTH / 2, HEIGHT / 5 * 2, 60)

        multiplayer_rect = draw_text(WIN, 'MULTIPLAYER', WIDTH / 2, HEIGHT / 5 * 3, 60)
        if multiplayer_rect.collidepoint(mouse_pos):
            draw_text(WIN, '>MULTIPLAYER<', WIDTH / 2, HEIGHT / 5 * 3, 60)

        back_rect = draw_text(WIN, 'BACK', WIDTH / 2, HEIGHT / 5 * 4, 60)
        if back_rect.collidepoint(mouse_pos):
            draw_text(WIN, '>BACK<', WIDTH / 2, HEIGHT / 5 * 4, 60)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if singleplayer_rect.collidepoint(mouse_pos):
                    run = False
                    pong.gameloop(WIN, False)
                if multiplayer_rect.collidepoint(mouse_pos):
                    run = False
                    pong.gameloop(WIN, True)
                if back_rect.collidepoint(mouse_pos):
                    run = False
                    main()


# Shows screen after game ends
def end_screen(text):
    run = True

    while run:
        pygame.time.Clock().tick(FPS)
        WIN.fill(DARK_GRAY)

        mouse_pos = pygame.mouse.get_pos()

        draw_text(WIN, text, WIDTH / 2, HEIGHT / 5 * 2, 60)

        back_rect = draw_text(WIN, 'BACK TO MENU', WIDTH / 2, HEIGHT / 5 * 3, 60)
        if back_rect.collidepoint(mouse_pos):
            draw_text(WIN, '>BACK TO MENU<', WIDTH / 2, HEIGHT / 5 * 3, 60)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mouse_pos):
                    run = False
                    main()


if __name__ == '__main__':
    main()
