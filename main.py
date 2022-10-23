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


def draw_heading(win, text):
    font = pygame.font.Font('assets/font/retro_game.ttf', 125)
    text_on_display = font.render(text, True, WHITE)
    text_rect = text_on_display.get_rect()
    text_rect.center = (WIDTH / 2, HEIGHT / 5)
    win.blit(text_on_display, text_rect)


def draw_button(win, text, y_pos):
    font = pygame.font.Font('assets/font/retro_game.ttf', 60)
    text_on_display = font.render(text, True, WHITE)
    text_rect = text_on_display.get_rect()
    text_rect.center = (WIDTH / 2, HEIGHT / 5 * y_pos)
    win.blit(text_on_display, text_rect)
    return text_rect


def main():
    run = True

    while run:
        pygame.time.Clock().tick(FPS)
        WIN.fill(DARK_GRAY)
        draw_heading(WIN, 'ATARI GAMES')

        mouse_pos = pygame.mouse.get_pos()

        pacman_rect = draw_button(WIN, 'PACMAN', 2)
        if pacman_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>PACMAN<', 2)

        pong_rect = draw_button(WIN, 'PONG', 3)
        if pong_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>PONG<', 3)

        space_rect = draw_button(WIN, 'SPACE INVADERS', 4)
        if space_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>SPACE INVADERS<', 4)

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


def gamemode_menu():
    run = True

    while run:
        pygame.time.Clock().tick(FPS)
        WIN.fill(DARK_GRAY)
        draw_heading(WIN, 'PONG')

        mouse_pos = pygame.mouse.get_pos()

        singleplayer_rect = draw_button(WIN, 'SINGLEPLAYER', 2)
        if singleplayer_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>SINGLEPLAYER<', 2)

        multiplayer_rect = draw_button(WIN, 'MULTIPLAYER', 3)
        if multiplayer_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>MULTIPLAYER<', 3)

        back_rect = draw_button(WIN, 'BACK', 4)
        if back_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>BACK<', 4)

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


def end_screen(text):
    run = True

    while run:
        pygame.time.Clock().tick(FPS)
        WIN.fill((0, 0, 0))

        mouse_pos = pygame.mouse.get_pos()

        draw_button(WIN, text, 2)

        back_rect = draw_button(WIN, 'BACK TO MENU', 3)
        if back_rect.collidepoint(mouse_pos):
            draw_button(WIN, '>BACK TO MENU<', 3)

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
