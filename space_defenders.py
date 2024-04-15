import pygame
import random
import math
from pygame import mixer

# Инициализируем Pygame
pygame.init()

# Создаем экран
screen = pygame.display.set_mode((800, 600))

# Название и иконка
pygame.display.set_caption("Космические Защитники")
icon = pygame.image.load('pics/ufo.png')  # Укажите путь к вашему файлу иконки
pygame.display.set_icon(icon)


font_style = pygame.font.Font("MenorahGrotesk-Semi.ttf", 20)
score_font = pygame.font.Font("MenorahGrotesk-Semi.ttf", 20)

# Фоновая музыка
mixer.music.load('pics/background.wav')  # Укажите путь к файлу фоновой музыки
mixer.music.play(-1)

# Игрок
playerImg = pygame.image.load('pics/player.png')  # Укажите путь к изображению игрока
playerX = 370
playerY = 560
playerX_change = 0

# Враг
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('pics/enemy.png'))  # Укажите путь к изображению врага
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(0, 50))
    enemyX_change.append(2)
    enemyY_change.append(20)

# Пуля
bulletImg = pygame.image.load('pics/bullet.png')
bulletImg = pygame.transform.rotate(bulletImg, 90)  # Укажите путь к изображению пули
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.6
bullet_state = "ready"  # "ready" - пуля готова к выстрелу; "fire" - пуля движется

score = 0

font = pygame.font.Font('freesansbold.ttf', 32)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score_display = font.render("Убито врагов: " + str(score), True, (255, 0, 0))
    screen.blit(score_display, (x, y))


def game_over_text():
    game_over_display = game_over_font.render("Игра закончена", True, (255, 0, 0))
    screen.blit(game_over_display, (200, 250))


# Отрисовка игрока
def player(x, y):
    screen.blit(playerImg, (x, y))


# Отрисовка врага
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Выстрел пули
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 0.1, y + 0.2))


# Проверка столкновения
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Игровой цикл
running = True
start_time = pygame.time.get_ticks() // 1000
game_time = 60
while running:
    screen.fill((255, 255, 255))
    current_time = pygame.time.get_ticks() // 1000
    remaining_time = game_time - (current_time - start_time)
    if remaining_time <= 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Управление
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('pics/laser.wav')  # Укажите путь к звуку выстрела
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Границы экрана для игрока
    if playerX <= 0:
        playerX = 0
    elif playerX >= 760:
        playerX = 760

    # Движение врага
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 760:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        # Столкновение
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('pics/explosion.wav')  # Укажите путь к звуку взрыва
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 700)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Движение пули
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(10, 10)
    timer_display = font.render("Оставшееся время: " + str(remaining_time), True, (255, 0, 0))
    screen.blit(timer_display, (430, 10))
    if remaining_time <= 0:
        game_over_text()
        pygame.display.update()
        pygame.time.delay(2000)  # Задержка перед перезапуском игры
        score = 0
        start_time = pygame.time.get_ticks() // 1000
        for i in range(num_of_enemies):
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(0, 50)
        remaining_time = game_time

    pygame.display.update()
