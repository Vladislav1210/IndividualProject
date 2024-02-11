import pygame
import sys
from pygame.mixer import Sound

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
        screen.fill(background_color)

    else:
        hint_flag = True


if __name__ == '__main__':
    pygame.init()
    font = pygame.font.Font(None, 30)

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Guitar training simulator')
    screen.fill(background_color)
    Button(1500, 30, 80, 80, screen, '?', hint_show)
    # common
    sound = {'z': Sound(''), 'a': Sound(''), 'q': Sound(''),
             'x': Sound(''), 's': Sound(''), 'w': Sound(''),
             'c': Sound(''), 'd': Sound(''), 'e': Sound(''),
             'v': Sound(''), 'f': Sound(''), 'r': Sound(''),
             'b': Sound(''), 'g': Sound(''), 't': Sound(''),
             'n': Sound(''), 'h': Sound(''), 'y': Sound(''),
             'm': Sound(''), 'j': Sound(''), 'u': Sound(''),
             ',': Sound(''), 'k': Sound(''), 'i': Sound(''),
             '.': Sound(''), 'l': Sound(''), 'o': Sound('')
             }
    # palm_mute
    sound_pm = {'z': Sound(''), 'a': Sound(''), 'q': Sound(''),
                'x': Sound(''), 's': Sound(''), 'w': Sound(''),
                'c': Sound(''), 'd': Sound(''), 'e': Sound(''),
                'v': Sound(''), 'f': Sound(''), 'r': Sound(''),
                'b': Sound(''), 'g': Sound(''), 't': Sound(''),
                'n': Sound(''), 'h': Sound(''), 'y': Sound(''),
                'm': Sound(''), 'j': Sound(''), 'u': Sound(''),
                ',': Sound(''), 'k': Sound(''), 'i': Sound(''),
                '.': Sound(''), 'l': Sound(''), 'o': Sound('')
                }

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # 6 string
                if event.key == pygame.K_z:
                    sound['z'].play()
                if event.key == pygame.K_x:
                    sound['x'].play()
                if event.key == pygame.K_c:
                    sound['c'].play()
                if event.key == pygame.K_v:
                    sound['v'].play()
                if event.key == pygame.K_b:
                    sound['b'].play()
                if event.key == pygame.K_n:
                    sound['n'].play()
                if event.key == pygame.K_m:
                    sound['m'].play()
                if event.key == pygame.K_COMMA:
                    sound[','].play()
                if event.key == pygame.K_PERIOD:
                    sound['.'].play()
                # 5 string
                if event.key == pygame.K_a:
                    sound['a'].play()
                if event.key == pygame.K_s:
                    sound['s'].play()
                if event.key == pygame.K_d:
                    sound['d'].play()
                if event.key == pygame.K_f:
                    sound['f'].play()
                if event.key == pygame.K_g:
                    sound['g'].play()
                if event.key == pygame.K_h:
                    sound['h'].play()
                if event.key == pygame.K_j:
                    sound['j'].play()
                if event.key == pygame.K_k:
                    sound['k'].play()
                if event.key == pygame.K_l:
                    sound['l'].play()
                # 4 string
                if event.key == pygame.K_q:
                    sound['q'].play()
                if event.key == pygame.K_w:
                    sound['w'].play()
                if event.key == pygame.K_e:
                    sound['e'].play()
                if event.key == pygame.K_r:
                    sound['r'].play()
                if event.key == pygame.K_t:
                    sound['t'].play()
                if event.key == pygame.K_y:
                    sound['y'].play()
                if event.key == pygame.K_u:
                    sound['u'].play()
                if event.key == pygame.K_i:
                    sound['i'].play()
                if event.key == pygame.K_o:
                    sound['o'].play()

            if event.type == pygame.KEYUP:
                # 6 string
                if event.key == pygame.K_z:
                    sound['z'].stop()
                if event.key == pygame.K_x:
                    sound['x'].stop()
                if event.key == pygame.K_c:
                    sound['c'].stop()
                if event.key == pygame.K_v:
                    sound['v'].stop()
                if event.key == pygame.K_b:
                    sound['b'].stop()
                if event.key == pygame.K_n:
                    sound['n'].stop()
                if event.key == pygame.K_m:
                    sound['m'].stop()
                if event.key == pygame.K_COMMA:
                    sound[','].stop()
                if event.key == pygame.K_PERIOD:
                    sound['.'].stop()
                # 5 string
                if event.key == pygame.K_a:
                    sound['a'].stop()
                if event.key == pygame.K_s:
                    sound['s'].stop()
                if event.key == pygame.K_d:
                    sound['d'].stop()
                if event.key == pygame.K_f:
                    sound['f'].stop()
                if event.key == pygame.K_g:
                    sound['g'].stop()
                if event.key == pygame.K_h:
                    sound['h'].stop()
                if event.key == pygame.K_j:
                    sound['j'].stop()
                if event.key == pygame.K_k:
                    sound['k'].stop()
                if event.key == pygame.K_l:
                    sound['l'].stop()
                # 4 string
                if event.key == pygame.K_q:
                    sound['q'].stop()
                if event.key == pygame.K_w:
                    sound['w'].stop()
                if event.key == pygame.K_e:
                    sound['e'].stop()
                if event.key == pygame.K_r:
                    sound['r'].stop()
                if event.key == pygame.K_t:
                    sound['t'].stop()
                if event.key == pygame.K_y:
                    sound['y'].stop()
                if event.key == pygame.K_u:
                    sound['u'].stop()
                if event.key == pygame.K_i:
                    sound['i'].stop()
                if event.key == pygame.K_o:
                    sound['o'].stop()

            if event.type == pygame.KEYDOWN and event.key == pygame.KMOD_SHIFT:
                if event.key == pygame.K_z:
                    sound['z'].play()
            if event.type == pygame.KEYUP and event.key == pygame.KMOD_SHIFT:
                if event.key == pygame.K_z:
                    sound['z'].stop()

        for button in buttons_group:
            button.process()
        if hint_flag:
            hint_window = pygame.Surface((1200, 800))
            hint_window.fill('white')
            pygame.draw.rect(hint_window, "red", (500, 400, 50, 50))
            screen.blit(hint_window, (200, 100))




