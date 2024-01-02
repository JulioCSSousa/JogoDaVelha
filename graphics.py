import pygame


def board_screen():
    pygame.init()
    x = 800
    y = 600
    screen = pygame.display.set_mode((x, y))
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption('./images/jogo_velha.png')
    board = pygame.image.load('./images/jogo_da_velha.png')
    board = pygame.transform.scale(board, (600, 480))
    while running:
        screen.blit(board, (100, 50))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

