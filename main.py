import pygame
import sys

size = width, height = 1600, 1000
background_color = (220, 255, 255)
hint_flag = False

buttons_group = []


class Button():
    def __init__(self, x, y, width, height, screen, buttonText='Button', onclickFunction=None, button_color='#ffffff'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.button_color = button_color
        self.alreadyPressed = False
        self.onePress = False
        self.surface_pos = screen
        self.fillColors = {
            'normal': button_color,
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        buttons_group.append(self)

    def process(self):
        mousepos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousepos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.surface_pos.blit(self.buttonSurface, self.buttonRect)


def hint_show():
    global hint_flag
    if hint_flag:
        hint_flag = False
    else:
        hint_flag = True
        screen.fill(background_color)
        Button(1500, 30, 80, 80, screen, '?', hint_show)


if __name__ == '__main__':
    pygame.init()
    font = pygame.font.Font(None, 30)

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Guitar training simulator')
    screen.fill(background_color)
    Button(1500, 30, 80, 80, screen, '?', hint_show)

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for button in buttons_group:
            button.process()
        if hint_flag:
            hint_window = pygame.Surface((1200, 800))
            hint_window.fill('white')
            screen.blit(hint_window, (200, 100))




