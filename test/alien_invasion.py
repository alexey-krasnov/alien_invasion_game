import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion():
    """Class to rule resources and behavior of the game"""
    def __init__(self):
        """Initialize game and build game resources"""
        pygame.init()
        self.settings = Settings()
        # игра в полноэкранном режиме
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_heigth = self.screen.get_rect().height
        # игра в отдельном окне
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # создаем экземпляр корабля
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def run_game(self):
        """Start of the main cycle of the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self._update_bullets()


    def _check_events(self):  # Вспомогательный метод, с символом _, работают внтури класса, а не через экземпляр
        # Check the keyboard and mouse actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Если клавиша нажата то перемещается корабль
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # Если клавиша отжата, то перемещение приостанавливается
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """реагирует на нажатие клавиш"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:  # Игра закрывается если нажата ESc
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """реагирует на отпускание клавиш"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции и уничтожает старые снаряды"""
        # Обновление позиций снарядов
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.topright >= self.settings.screen_width:
                self.bullets.remove(bullet)
            # print(len(self.bullets)) # Смотреть в терминале число активных снарядов на экране


    def _update_screen(self):  # Вспомогательный метод, с символом _, работают внтури класса, а не через экземпляр
        # Обновляет изображение на экране и отображает новый экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Show the last screen
        pygame.display.flip()


if __name__ == '__main__':
    # Create an exemplar and start the game
    ai = AlienInvasion()
    ai.run_game()
