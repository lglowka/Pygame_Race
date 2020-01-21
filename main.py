import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((600, 601))

# Title and logo
pygame.display.set_caption("Race")
icon = pygame.image.load("formula.png")
pygame.display.set_icon(icon)

# Background
bg = pygame.image.load("bg.png")

# Player
player_Img = pygame.image.load("player.png")
playerX = 370
playerY = 480
player_dX = 0
player_dY = 0

# Cars
y = 0
op_Img = []
opX = []
opY = []
op_dY = []
num_of_op = 3
for i in range(num_of_op):
    op_Img.append(pygame.image.load("op.png"))
    opX.append(random.randint(81, 453))
    opY.append(y)
    op_dY.append(2)
    y -= 200

# Point
point_Img = pygame.image.load("star.png")
pointX = random.randint(81, 453)
pointY = -50
point_dY = 2


def player(x, y):
    screen.blit(player_Img, (x, y))


def op(x, y, i):
    screen.blit(op_Img[i], (x, y))


def star(x, y):
    screen.blit(point_Img, (x, y))


def isPoint(pointX, pointY, playerX, playerY):
    distance = math.sqrt((math.pow((pointX - playerX), 2)) + math.pow((pointY - playerY), 2))
    if distance < 27:
        return True
    else:
        return False


def isCollision(opX, opY, playerX, playerY):
    col = math.sqrt((math.pow((opX - playerX), 2)) + math.pow((opY - playerY), 2))
    if col < 40 or playerX > 500 or playerX < 50:
        return True
    else:
        return False


# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


# Game Over
end = 0
game_over_font = pygame.font.Font("freesansbold.ttf", 64)


def game_over_text():
    game_over = game_over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game_over, (100, 200))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        # Player movement
        # if keystroke is pressed check whether its right, left, up or down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_dX = 5

            if event.key == pygame.K_LEFT:
                player_dX = -5

            if event.key == pygame.K_UP:
                player_dY = -5

            if event.key == pygame.K_DOWN:
                player_dY = 5

        if event.type == pygame.KEYUP:
            player_dX = 0
            player_dY = 0

    playerX += player_dX
    playerY += player_dY

    # Op movement

    for i in range(num_of_op):
        opY[i] += op_dY[i]
        if opY[i] > 610:
            opY[i] = 0
            opX[i] = random.randint(81, 453)
        # Collision
        collision = isCollision(opX[i], opY[i], playerX, playerY)
        if collision:
            end += 1
        if end > 0:
            for k in range(num_of_op):
                opY[k] = 2000
                op_dY[k] = 0
                point_dY = 0
                pointY = 2000
            game_over_text()
            break

        op(opX[i], opY[i], i)

    # Star
    pointY += point_dY
    star(pointX, pointY)
    if pointY > 600:
        pointY = -50
        pointX = random.randint(81, 453)

    player(playerX, playerY)
    # Point
    point = isPoint(pointX, pointY, playerX, playerY)
    if point:
        pointY = -50
        pointX = random.randint(81, 453)
        score_value += 10

    show_score(textX, textY)
    pygame.display.update()
pygame.quit()
