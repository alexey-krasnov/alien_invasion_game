import pygame.font


class Button:

    def __init__(self, ai, msg):
        """Initialize attributes of button"""
        # msg - text of button
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()

        # Size and properties of the buttons
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0) # green
        self.text_color = (255, 255, 255) # White color
        self.font = pygame.font.SysFont(None, 48)

        # Build object rect of button and align at center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message of button is created only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transform 'msg' text into rectangle and align text at center"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Image empty button and show the text"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
