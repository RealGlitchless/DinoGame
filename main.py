import random
import pygame
import os
import sys
import ctypes

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)

# Get window width and height and set to window size
size = width, height = 500, 300

# Set windows size
screen = pygame.display.set_mode(size)
# Get root
root = os.path.dirname(sys.modules['__main__'].__file__)
# Set title
pygame.display.set_caption('Dino Game')
# Get Clock
clock = pygame.time.Clock()
screen.fill(white)


def mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


isRunning = True
while isRunning:
    dino = pygame.image.load("dino.png")
    # Dino starting pos
    dinopos_x = 40
    dinopos_y = height - 55
    tempDino = dinopos_y

    obstaclepos_x = width
    obstaclepos_y = height - 30

    obstaclepos_x2 = obstaclepos_x * 2
    obstaclepos_y2 = height - 30

    scrollSpeed = 60
    score = 0
    highScore = 0
    randomHeight = 0
    randomHeight2 = 0

    gameRunning = True
    while gameRunning:
        clock.tick(scrollSpeed)  # framerate

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        playerKey = pygame.key.get_pressed()
        if playerKey[pygame.K_SPACE]:
            if not dinopos_y == 120 and tempDino >= dinopos_y:
                dinopos_y -= 5
                tempDino = dinopos_y

            else:
                dinopos_y += 5

        else:
            dinopos_y += 5

        if dinopos_y > (height - 55):
            dinopos_y = height - 55
            tempDino = dinopos_y

        if obstaclepos_x >= width:
            randomHeight = random.randint(30, 100)

        if obstaclepos_x2 >= width:
            randomHeight2 = random.randint(30, 100)

        score += 1
        screen.fill(white)
        obstaclepos_x -= 5
        obstaclepos_x2 -= 5

        obstacleRect = pygame.Surface((obstaclepos_x, obstaclepos_y))
        obstacleRect = obstacleRect.get_rect()
        obstacleRect = obstacleRect.move(obstaclepos_x, obstaclepos_y)
        obstacle = pygame.draw.rect(screen, black, (obstaclepos_x, obstaclepos_y - randomHeight + 30, 10, randomHeight))

        obstacleRect2 = pygame.Surface((obstaclepos_x2, obstaclepos_y2))
        obstacleRect2 = obstacleRect2.get_rect()
        obstacleRect2 = obstacleRect2.move(obstaclepos_x2, obstaclepos_y2)
        obstacle2 = pygame.draw.rect(screen, black, (obstaclepos_x2, obstaclepos_y2 - randomHeight2 + 30, 10, randomHeight2))

        dinoRect = dino.get_rect()
        dinoRect = dinoRect.move(dinopos_x, dinopos_y)
        screen.blit(dino, (dinopos_x, dinopos_y))

        font = pygame.font.SysFont(None, 48)
        scoreText = font.render(f'{score}', True, black)
        textRect = scoreText.get_rect()
        textRect.center = (width // 2, height // 7)
        screen.blit(scoreText, textRect)  # draws score

        pygame.display.update()

        if score % 500 == 0:
            scrollSpeed += 15

        if obstaclepos_x <= 10:
            obstaclepos_x = obstaclepos_x2 * 2

        if obstaclepos_x2 <= 10:
            obstaclepos_x2 = obstaclepos_x * 2

        if pygame.Rect.colliderect(dinoRect, obstacleRect):
            break

        if pygame.Rect.colliderect(dinoRect, obstacleRect2):
            break

    # Display gameover and popup with score
    pygame.display.update()
    if score > highScore:
        highScore = score

    choice = mbox('Game Over',
                  f'You scored {score}\n'
                  f'Your current highscore is {highScore}\n'
                  'Do you want to play again?', 4)

    YES = 6
    NO = 7
    if choice == YES:
        continue

    if choice == NO:
        isRunning = False
