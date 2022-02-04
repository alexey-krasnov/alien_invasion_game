import pygame


class Ship():
    """класс для управления кораблем"""
    def __init__(self, ai):
        """Инициализирует корабль и заадет его начальную позицию"""
        self.screen = ai.screen
        self.settings = ai.settings  # создаем атрибут settings для использования в update
        self.screen_rect = ai.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image_load = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.flip(self.image_load, True, False)
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у левого края экрана
        self.rect.midleft = self.screen_rect.midleft
        # Сохранение вещественной координаты центра корабля в новом атрибуте self.y
        self.y = float(self.rect.y)
        # Флаг перемещения вверх и вниз
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        # обновляется атрибут y объекта ship а не rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
