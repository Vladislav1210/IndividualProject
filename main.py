import io

import pygame
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from pygame.mixer import Sound


size = width, height = 1600, 1000
background_color = (220, 255, 255)
hint_flag = False
description_text = 'Симулятор тренировки игры на гитаре'

buttons_group = []


class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)


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


def song_show():
    app = QApplication(sys.argv)
    ex = Window1()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    pygame.init()

    font = pygame.font.Font(None, 30)
    font2 = pygame.font.Font(None, 100)

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Guitar training simulator')
    screen.fill(background_color)

    Button(1500, 30, 80, 80, screen, '?', hint_show)
    Button(400, 500, 130, 60, screen, 'песня', song_show)
    description = font2.render(description_text, True, (100, 100, 100))
    screen.blit(description, (100, 30))
    # common
    sound = {'a': Sound('sound/0.6.wav'), 'q': Sound('sound/0.5.wav'), '1': Sound('sound/0.4.wav'),
             's': Sound('sound/1.6.wav'), 'w': Sound('sound/1.5.wav'), '2': Sound('sound/1.4.wav'),
             'd': Sound('sound/2.6.wav'), 'e': Sound('sound/2.5.wav'), '3': Sound('sound/2.4.wav'),
             'f': Sound('sound/3.6.wav'), 'r': Sound('sound/3.5.wav'), '4': Sound('sound/3.4.wav'),
             'g': Sound('sound/4.6.wav'), 't': Sound('sound/4.5.wav'), '5': Sound('sound/4.4.wav'),
             'h': Sound('sound/5.6.wav'), 'y': Sound('sound/5.5.wav'), '6': Sound('sound/5.4.wav'),
             'j': Sound('sound/6.6.wav'), 'u': Sound('sound/6.5.wav'), '7': Sound('sound/6.4.wav'),
             'k': Sound('sound/7.6.wav'), 'i': Sound('sound/7.5.wav'), '8': Sound('sound/7.4.wav'),
             'l': Sound('sound/8.6.wav'), 'o': Sound('sound/8.5.wav'), '9': Sound('sound/8.4.wav'),
             ';': Sound('sound/9.6.wav'), 'p': Sound('sound/9.5.wav'), '0': Sound('sound/9.4.wav')
             }
    # palm_mute
    '''sound_pm = {'a': Sound(''), 'q': Sound(''), '1': Sound(''),
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

    sound_pm = {'a': Sound('pm_sound/0.6pm.wav'), 's': Sound('pm_sound/1.6pm.wav'), 'd': Sound('pm_sound/2.6pm.wav'),
                'f': Sound('pm_sound/3.6pm.wav'), 'g': Sound('pm_sound/4.6pm.wav'), 'h': Sound('pm_sound/5.6pm.wav'),
                'j': Sound('pm_sound/6.6pm.wav'), 'k': Sound('pm_sound/7.6pm.wav'), 'l': Sound('pm_sound/8.6pm.wav'),
                ';': Sound('pm_sound/9.6pm.wav')}
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








