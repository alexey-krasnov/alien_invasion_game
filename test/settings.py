class Settings():
    """класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """"инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (230, 230, 230)
        # Настройки корабля
        self.ship_speed = 5
        # параметры снаряда
        self.bullet_speed = 3
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60) # Темно серые снаряды
        self.bullet_allowed = 5