from random import choice

import main
from constants import *

P_WIDTH, P_HEIGHT = 40, 250
P_SPEED = 5
B_RADIUS = 14
B_SPEED = 8
MAX_SCORE = 10


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, P_WIDTH, P_HEIGHT))

    def move(self, up):
        # paddle go up
        if up and self.y >= 0:
            self.y -= P_SPEED
        # paddle go down
        elif not up and self.y + P_HEIGHT <= HEIGHT:
            self.y += P_SPEED

    def ai_move(self, ball):
        y_middle = self.y + P_HEIGHT // 2

        # ball is under the paddle
        if ball.y > self.y + P_HEIGHT:
            self.move(False)
        # ball is above the paddle
        elif ball.y < self.y:
            self.move(True)
        # ball is in 2/4 of the paddle
        elif self.y + P_HEIGHT // 4 * 2 < ball.y <= y_middle:
            self.move(True)
        # ball is in 3/4 of the paddle
        elif P_HEIGHT + P_HEIGHT // 4 * 3 < ball.y < y_middle:
            self.move(False)

    # Handle ball and paddle collision
    def ball_collision(self, ball):
        ball.x_speed *= -1
        y_middle = self.y + P_HEIGHT // 2
        difference_in_y = y_middle - ball.y
        y_speed = difference_in_y // ((P_HEIGHT // 2) // B_SPEED)
        ball.y_speed = -1 * y_speed


class Ball:
    def __init__(self, x, y, x_speed, y_speed):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), B_RADIUS)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed


class Game:
    def __init__(self):
        self.l_paddle = Paddle(40, HEIGHT // 2 - P_HEIGHT // 2)
        self.r_paddle = Paddle(WIDTH - P_WIDTH - 40, HEIGHT // 2 - P_HEIGHT // 2)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2, choice([-B_SPEED, B_SPEED]), choice([-B_SPEED, 0, B_SPEED]))
        self.l_score = self.r_score = 0

    def draw(self, win):
        win.fill(DARK_GRAY)

        self.r_paddle.draw(win)
        self.l_paddle.draw(win)

        self.ball.draw(win)

        win.blit(BACK, (20, 20))

        main.draw_text(win, str(self.l_score), WIDTH // 2 - 75, 50, 100)
        main.draw_text(win, str(self.r_score), WIDTH // 2 + 75, 50, 100)

        # Draws divider in the middle
        for idx in range(40):
            if idx % 2 == 1:
                pygame.draw.rect(win, WHITE, (WIDTH // 2 - 5, HEIGHT // 40 * idx - HEIGHT // 80, 10, HEIGHT // 40))

        pygame.display.update()

    # Checks what keys are pressed and move paddles
    def paddle_movement(self, keys, multiplayer):
        if keys[pygame.K_w]:
            self.l_paddle.move(True)
        if keys[pygame.K_s]:
            self.l_paddle.move(False)
        if keys[pygame.K_UP] and multiplayer:
            self.r_paddle.move(True)
        if keys[pygame.K_DOWN] and multiplayer:
            self.r_paddle.move(False)

        if not multiplayer:
            self.r_paddle.ai_move(self.ball)

    def ball_movement(self):
        if self.ball.y - B_RADIUS <= B_SPEED or self.ball.y + B_RADIUS >= HEIGHT - B_SPEED:
            self.ball.y_speed *= -1

        if self.ball.x_speed < 0:
            if self.l_paddle.y <= self.ball.y <= self.l_paddle.y + P_HEIGHT:  # if paddle touches the ball
                if self.ball.x - B_RADIUS <= self.l_paddle.x + P_WIDTH:
                    self.l_paddle.ball_collision(self.ball)
        else:
            if self.r_paddle.y <= self.ball.y <= self.r_paddle.y + P_HEIGHT:
                if self.ball.x + B_RADIUS >= self.r_paddle.x:
                    self.r_paddle.ball_collision(self.ball)

        self.ball.move()

    # Changes coordinates and ball speed to default values
    def reset(self):
        self.l_paddle.x, self.l_paddle.y = 40, HEIGHT // 2 - P_HEIGHT // 2
        self.r_paddle.x, self.r_paddle.y = WIDTH - P_WIDTH - 40, HEIGHT // 2 - P_HEIGHT // 2
        self.ball.x, self.ball.y = WIDTH // 2, HEIGHT // 2
        self.ball.x_speed, self.ball.y_speed = choice([-B_SPEED, B_SPEED]), choice([-B_SPEED, 0, B_SPEED])

    def score_handler(self, multiplayer):
        if self.ball.x <= 0:
            self.reset()
            self.r_score += 1
        if self.ball.x >= WIDTH:
            self.reset()
            self.l_score += 1

        if self.l_score >= MAX_SCORE:
            if multiplayer:
                main.end_screen('LEFT PLAYER WON')
            else:
                main.end_screen('YOU WON')
            return False

        if self.r_score >= MAX_SCORE:
            if multiplayer:
                main.end_screen('RIGHT PLAYER WON')
            else:
                main.end_screen('YOU LOST')
            return False
        return True


# Initializes paddles and ball and handle gameloop
def gameloop(win, multiplayer):
    run = True
    game = Game()

    while run:
        pygame.time.Clock().tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        back_rec = pygame.Rect(20, 20, BACK_WIDTH, BACK_HEIGHT)

        game.draw(win)

        keys = pygame.key.get_pressed()
        game.paddle_movement(keys, multiplayer)
        game.ball_movement()
        if not game.score_handler(multiplayer):
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rec.collidepoint(mouse_pos):
                    run = False
                    main.main()
