import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion():
    """Class to rule resources and behavior of the game"""
    def __init__(self):
        """Initialize game and build game resources"""
        pygame.init()
        self.settings = Settings()
        # game in full screen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_heigth = self.screen.get_rect().height
        # game in separate window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien Invasion")

        # Make instances to save statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)  # Make ship instance
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start of the main cycle of the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        # Check the keyboard and mouse actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # If the key is pressed, the ship moves
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # If the key is released, the movement is suspended
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Starts new game when Play is pressed"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # reset game settings
            self.settings.initialize_dynamic_settings()
            # reset game statistics
            self.stats.reset_stats()
            self.stats.game_active = True

            # Clear aliens and bullets lists
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and place ship at center
            self._create_fleet()
            self.ship.center_ship()

            # hide mouse
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:  # Game closes if ESc is pressed
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and include it in a group bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Refresh positions and destroy old bullets"""
        # Обновление позиций снарядов
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets)) # Смотреть в терминале число активных снарядов на экране
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # проверка попаданий в пришельца
        # при обнаружении попадания удалить снаряд и пришельца
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_aliens(self):
        """обновляет позиции всех пришелцев во флоте"""
        self.aliens.update()
        self._check_fleet_edges()
        # Check collision alien-ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Check if alliens at the midbottom of the screen
        self._check_aleins_bottom()

    def _ship_hit(self):
        """Processing of chip collision "with the aliens"""
        if self.stats.ships_left > 0:
            # Reduce ships_left
            self.stats.ships_left -=1

            # Deletion of alien list and bullets list
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and position of the ship in center
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aleins_bottom(self):
        """Check if aliens are at the midbottom of screeen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # The same as during collision with ship
                self._ship_hit()
                break

    def _create_fleet(self):
        """Создание флота вторжения"""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2*alien_width)
        """Определение количества рядов помещающихся на экране"""
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_heigth - 3 * alien_height - ship_height
        number_rows = available_space_y // (2 * alien_height)
        # Создание первого ряда пришельцев
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        # Создание пришельца и размещение его в ряду
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):  # Вспомогательный метод, с символом _, работают внтури класса, а не через экземпляр
        # Обновляет изображение на экране и отображает новый экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        # Button Play will be shown if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Show the last screen
        pygame.display.flip()


if __name__ == '__main__':
    # Create an instance and start the game
    ai = AlienInvasion()
    ai.run_game()
