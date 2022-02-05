import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем"""
    def __init__(self, ai):
        """создает объект снарядом в текущей позиции корабля"""
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.color = self.settings.bullet_color

        # Создание снаряда в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = ai.ship.rect.midleft  # Атрибуту midtop снаряда присваивается значение midtop корабля

        # позиция снаряда хранится в вещественном формате
        self.x = float(self.rect.x) # верхний край снаряда совмещается с верхним краем прямоугольника корабля

    def update(self):
        """Перемещает снаряд вверх по экрану"""
        # обновление позиции снаряда в вещественном формате
        self.x += self.settings.bullet_speed
        # Обновление позиции прямоугольника
        self.rect.x = self.x

    def draw_bullet(self):
        """"Выводит снаряды на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
