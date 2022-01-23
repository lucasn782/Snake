import pygame, random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
display = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((120,255,120))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,20,10))

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
        
    
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break
    
    
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
    
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    display.fill((110,110,110))
    display.blit(apple, apple_pos)
    
    score_font = font.render('Pontos: %s' % (score), True, (240, 230, 0))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    display.blit(score_font, score_rect)

    creator_font = pygame.font.Font('freesansbold.ttf', 15)
    creator_screen = creator_font.render('lucasn782', True, (10, 20, 255))
    creator_rect = creator_screen.get_rect()
    creator_rect.midtop = (1110 / 2, 570)
    display.blit(creator_screen, creator_rect)
    
    for pos in snake:
        display.blit(snake_skin,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 35)
    game_over_screen = game_over_font.render('Fim de jogo!', True, (255, 20, 10))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 275)
    display.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()