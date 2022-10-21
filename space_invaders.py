import pygame

def gameloop(win, multiplayer):
    run = True
    l_paddle = Paddle(40, HEIGHT // 2 - P_HEIGHT // 2)
    r_paddle = Paddle(WIDTH - P_WIDTH - 40, HEIGHT // 2 - P_HEIGHT // 2)
    ball = Ball(WIDTH // 2, HEIGHT // 2, choice([-B_SPEED, B_SPEED]), choice([-B_SPEED, 0, B_SPEED]))
    l_score, r_score = 0, 0

    while run:
        pygame.time.Clock().tick(FPS)
        draw(win, r_paddle, l_paddle, ball, r_score, l_score)

        keys = pygame.key.get_pressed()
        paddle_movement(keys, r_paddle, l_paddle, multiplayer)
        ball_movement(ball, r_paddle, l_paddle)
        if not multiplayer:
            r_paddle.ai_move(ball)

        if ball.x <= 0:
            reset(ball, r_paddle, l_paddle)
            r_score += 1
        if ball.x >= WIDTH:
            reset(ball, r_paddle, l_paddle)
            l_score += 1

        if l_score > MAX_SCORE:
            run = False
            if multiplayer:
                main.end_screen('LEFT PLAYER WON')
            else:
                main.end_screen('YOU WON')

        if r_score > MAX_SCORE:
            run = False
            if multiplayer:
                main.end_screen('RIGHT PLAYER WON')
            else:
                main.end_screen('YOU LOST')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()