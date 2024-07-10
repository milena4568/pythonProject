import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 70  # Размер сетки
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Цвета
BACKGROUND_COLOR = (71, 74, 81)
WHITE = (255, 255, 255)

# Создание окна
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка на Pygame')

# Загрузка изображений и изменение их размеров
snake_segment_img = pygame.image.load('s.png')
food_img = pygame.image.load('j.png')

# Изменение размера изображений под сетку
snake_segment_img = pygame.transform.scale(snake_segment_img, (GRID_SIZE, GRID_SIZE))
food_img = pygame.transform.scale(food_img, (GRID_SIZE, GRID_SIZE))

# Инициализация змейки и еды
snake_positions = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
snake_length = 1
score = 0

# Генерация позиции еды на сетке
food_position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

# Функция для отрисовки змейки
def draw_snake(surface, positions, sprite):
    for p in positions:
        surface.blit(sprite, p)

# Функция для отрисовки еды
def draw_food(surface, position, sprite):
    surface.blit(sprite, position)

# Основная функция игры
def main():
    global snake_positions, snake_direction, snake_length, score, food_position
    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont("monospace", 16)

    running = True
    while running:
        clock.tick(5)  # Уменьшаем скорость движения змейки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_UP:
                    if snake_direction != (0, 1):
                        snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    if snake_direction != (0, -1):
                        snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    if snake_direction != (1, 0):
                        snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    if snake_direction != (-1, 0):
                        snake_direction = (1, 0)

        head_x, head_y = snake_positions[0]
        delta_x, delta_y = snake_direction
        new_head = ((head_x + (delta_x * GRID_SIZE)) % WIDTH, (head_y + (delta_y * GRID_SIZE)) % HEIGHT)

        # Проверка на столкновение с границами окна
        if new_head in snake_positions[1:] or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            snake_positions = [(WIDTH // 2, HEIGHT // 2)]
            snake_direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
            snake_length = 1
            score = 0
        else:
            snake_positions.insert(0, new_head)
            if len(snake_positions) > snake_length:
                snake_positions.pop()

        # Проверка на столкновение с едой
        if snake_positions[0] == food_position:
            snake_length += 1
            score += 1
            food_position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

        win.fill(BACKGROUND_COLOR)  # Устанавливаем цвет фона
        draw_snake(win, snake_positions, snake_segment_img)
        draw_food(win, food_position, food_img)

        score_text = score_font.render("Счет: " + str(score), True, WHITE)
        win.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()

main()
