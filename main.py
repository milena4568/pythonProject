import pygame
import random
# Эта программа будет случайным образом генерировать прямоугольники разных цветов и размеров на экране.
# Инициализация Pygame
pygame.init()

# Параметры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Случайные прямоугольники")

# Функция для генерации случайного цвета
"""
Функция возвращает случайный цвет в формате RGB, 
каждая компонента (красная, зеленая, синяя) находится в диапазоне от 0 до 255.
"""
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Основной цикл программы
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Генерация случайного прямоугольника
    width = random.randint(20, 20)
    # Случайная ширина прямоугольника от 20 до 100 пикселей.
    height = random.randint(20, 20)
    # Случайная высота прямоугольника от 20 до 100 пикселей.
    pos = (random.randint(0, screen_width - width), random.randint(0, screen_height - height))
    # Случайная позиция верхнего левого угла прямоугольника так, чтобы он не выходил за пределы экрана.
    color = random_color()
    # Генерация случайного цвета для прямоугольника.

    # Отрисовка прямоугольника
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height))
    """"
    Отрисовка прямоугольника заданным цветом (color) и размерами (width и height) 
    на заданных координатах (pos) на экране (screen).
    """
    pygame.display.flip()
    clock.tick(10)

pygame.quit()

