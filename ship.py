import pygame


class Ship():
    """класс для управления кораблем"""
    def __init__(self, ai):
        """Инициализирует корабль и заадет его начальную позицию"""
        self.screen = ai.screen
        self.settings = ai.settings  # создаем атрибут settings для использования в update
        self.screen_rect = ai.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты центра корабля в новом атрибуте self.x
        self.x = float(self.rect.x)
        # Флаг перемещения вправо и влево
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        # обновляется атрибут х объекта ship а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Place s ship in the midbottom"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)