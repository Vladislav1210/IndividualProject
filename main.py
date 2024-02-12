import pygame
import sys
from pygame.mixer import Sound

size = width, height = 1600, 1000
background_color = (220, 255, 255)
hint_flag = False
description_text = 'Симулятор тренировки игры на гитаре'

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
        screen.blit(description, (100, 30))
    else:
        hint_flag = True


if __name__ == '__main__':
    pygame.init()

    font = pygame.font.Font(None, 30)
    font2 = pygame.font.Font(None, 100)

    image = pygame.image.load('tinker.jpg')
    image_rect = image.get_rect(bottomright=(1000, 500))

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Guitar training simulator')
    screen.fill(background_color)

    Button(1500, 30, 80, 80, screen, '?', hint_show)
    description = font2.render(description_text, True, (100, 100, 100))
    screen.blit(description, (100, 30))
    # common
    '''sound = {'a': Sound(''), 'q': Sound(''), '1': Sound(''),
             's': Sound(''), 'w': Sound(''), '2': Sound(''),
             'd': Sound(''), 'e': Sound(''), '3': Sound(''),
             'f': Sound(''), 'r': Sound(''), '4': Sound(''),
             'g': Sound(''), 't': Sound(''), '5': Sound(''),
             'h': Sound(''), 'y': Sound(''), '6': Sound(''),
             'j': Sound(''), 'u': Sound(''), '7': Sound(''),
             'k': Sound(''), 'i': Sound(''), '8': Sound(''),
             'l': Sound(''), 'o': Sound(''), '9': Sound(''),
             ';': Sound(''), 'p': Sound(''), '0': Sound('')
             }
    # palm_mute
    sound_pm = {'a': Sound(''), 'q': Sound(''), '1': Sound(''),
                's': Sound(''), 'w': Sound(''), '2': Sound(''),
                'd': Sound(''), 'e': Sound(''), '3': Sound(''),
                'f': Sound(''), 'r': Sound(''), '4': Sound(''),
                'g': Sound(''), 't': Sound(''), '5': Sound(''),
                'h': Sound(''), 'y': Sound(''), '6': Sound(''),
                'j': Sound(''), 'u': Sound(''), '7': Sound(''),
                'k': Sound(''), 'i': Sound(''), '8': Sound(''),
                'l': Sound(''), 'o': Sound(''), '9': Sound(''),
                ';': Sound(''), 'p': Sound(''), '0': Sound('')
                }'''
    sound = {'a': Sound('1.wav.mp3')}
    sound_pm = {'a': Sound('2.wav')}

    while True:
        pygame.display.flip()
        screen.blit(description, (100, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            for button in buttons_group:
                button.process()
            if hint_flag:
                hint_window = pygame.Surface((1200, 800))
                hint_window.fill('white')
                pygame.draw.rect(hint_window, "red", (500, 400, 50, 50))
                screen.blit(hint_window, (200, 100))
                hint_window.blit(image, (100, 20))

            mods = pygame.key.get_mods()

            # palm_mute
            if event.type == pygame.KEYDOWN and mods & pygame.KMOD_SHIFT:
                # 6 string
                if event.key == pygame.K_a:
                    sound_pm['a'].play()
                if event.key == pygame.K_s:
                    sound_pm['s'].play()
                if event.key == pygame.K_d:
                    sound_pm['d'].play()
                if event.key == pygame.K_f:
                    sound_pm['f'].play()
                if event.key == pygame.K_g:
                    sound_pm['g'].play()
                if event.key == pygame.K_h:
                    sound_pm['h'].play()
                if event.key == pygame.K_j:
                    sound_pm['j'].play()
                if event.key == pygame.K_k:
                    sound_pm['k'].play()
                if event.key == pygame.K_l:
                    sound_pm['l'].play()
                if event.key == pygame.K_SEMICOLON:
                    sound_pm[';'].play()
                # 5 string
                if event.key == pygame.K_q:
                    sound_pm['q'].play()
                if event.key == pygame.K_w:
                    sound_pm['w'].play()
                if event.key == pygame.K_e:
                    sound_pm['e'].play()
                if event.key == pygame.K_r:
                    sound_pm['r'].play()
                if event.key == pygame.K_t:
                    sound_pm['t'].play()
                if event.key == pygame.K_y:
                    sound_pm['y'].play()
                if event.key == pygame.K_u:
                    sound_pm['u'].play()
                if event.key == pygame.K_i:
                    sound_pm['i'].play()
                if event.key == pygame.K_o:
                    sound_pm['o'].play()
                if event.key == pygame.K_p:
                    sound_pm['p'].play()
                # 4 string
                if event.key == pygame.K_1:
                    sound_pm['1'].play()
                if event.key == pygame.K_2:
                    sound_pm['2'].play()
                if event.key == pygame.K_3:
                    sound_pm['3'].play()
                if event.key == pygame.K_4:
                    sound_pm['4'].play()
                if event.key == pygame.K_5:
                    sound_pm['5'].play()
                if event.key == pygame.K_6:
                    sound_pm['6'].play()
                if event.key == pygame.K_7:
                    sound_pm['7'].play()
                if event.key == pygame.K_8:
                    sound_pm['8'].play()
                if event.key == pygame.K_9:
                    sound_pm['9'].play()
                if event.key == pygame.K_0:
                    sound_pm['0'].play()
            # common
            elif event.type == pygame.KEYDOWN:
                # 6 string
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
                if event.key == pygame.K_SEMICOLON:
                    sound[';'].play()
                # 5 string
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
                if event.key == pygame.K_p:
                    sound['p'].play()
                # 4 string
                if event.key == pygame.K_1:
                    sound['1'].play()
                if event.key == pygame.K_2:
                    sound['2'].play()
                if event.key == pygame.K_3:
                    sound['3'].play()
                if event.key == pygame.K_4:
                    sound['4'].play()
                if event.key == pygame.K_5:
                    sound['5'].play()
                if event.key == pygame.K_6:
                    sound['6'].play()
                if event.key == pygame.K_7:
                    sound['7'].play()
                if event.key == pygame.K_8:
                    sound['8'].play()
                if event.key == pygame.K_9:
                    sound['9'].play()
                if event.key == pygame.K_0:
                    sound['0'].play()

            if event.type == pygame.KEYUP:
                # 6 string
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
                if event.key == pygame.K_SEMICOLON:
                    sound[';'].stop()
                # 5 string
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
                if event.key == pygame.K_p:
                    sound['p'].stop()
                # 4 string
                if event.key == pygame.K_1:
                    sound['1'].stop()
                if event.key == pygame.K_2:
                    sound['2'].stop()
                if event.key == pygame.K_3:
                    sound['3'].stop()
                if event.key == pygame.K_4:
                    sound['4'].stop()
                if event.key == pygame.K_5:
                    sound['5'].stop()
                if event.key == pygame.K_6:
                    sound['6'].stop()
                if event.key == pygame.K_7:
                    sound['7'].stop()
                if event.key == pygame.K_8:
                    sound['8'].stop()
                if event.key == pygame.K_9:
                    sound['9'].stop()
                if event.key == pygame.K_0:
                    sound['0'].stop()

            if event.type == pygame.KEYUP and mods & pygame.KMOD_SHIFT:
                if event.key == pygame.K_a:
                    sound_pm['a'].stop()






