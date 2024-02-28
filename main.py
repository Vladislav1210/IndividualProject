import io

import pygame
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from pygame.mixer import Sound


size = width, height = 1600, 1000
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
        font = pygame.font.Font(None, 30)
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


def retrn():
    sys.exit()


def play_fragment():
    pass


def note(event, mods, sound, sound_pm):
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


def enter_sandman():

    pygame.init()

    font2 = pygame.font.Font(None, 100)
    font3 = pygame.font.Font(None, 70)

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Enter Sandman')
    screen.fill('white')

    Button(1500, 20, 80, 80, screen, onclickFunction=retrn, buttonText='X', button_color='red')
    Button(10, 155, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')
    Button(10, 395, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')
    Button(10, 630, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')
    Button(10, 870, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')

    description = font2.render('Enter Sandman', True, (50, 50, 50))
    x4 = font3.render('x4', True, (50, 50, 50))
    x3 = font3.render('x3', True, (50, 50, 50))
    x7 = font3.render('x7', True, (50, 50, 50))
    screen.blit(description, (100, 10))

    es1 = pygame.image.load('pict/enter_sandman1.png')
    es2 = pygame.image.load('pict/enter_sandman2.png')
    es3 = pygame.image.load('pict/enter_sandman3.png')
    es35 = pygame.image.load('pict/enter_sandman3.5.png')
    es4 = pygame.image.load('pict/enter_sandman4.png')
    es5 = pygame.image.load('pict/enter_sandman5.png')
    screen.blit(es1, (70, 70))
    screen.blit(es2, (70, 302))
    screen.blit(es3, (70, 540))
    screen.blit(es35, (765, 540))
    screen.blit(es4, (70, 757))
    screen.blit(es5, (600, 755))

    screen.blit(x4, (750, 170))
    screen.blit(x4, (750, 400))
    screen.blit(x7, (730, 635))
    screen.blit(x3, (580, 860))
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
    sound_pm = {'a': Sound('pm_sound/0.6pm.wav'), 'q': Sound('pm_sound/0.5pm.wav'), '1': Sound('pm_sound/0.4pm.wav'),
                's': Sound('pm_sound/1.6pm.wav'), 'w': Sound('pm_sound/1.5pm.wav'), '2': Sound('pm_sound/1.4pm.wav'),
                'd': Sound('pm_sound/2.6pm.wav'), 'e': Sound('pm_sound/2.5pm.wav'), '3': Sound('pm_sound/2.4pm.wav'),
                'f': Sound('pm_sound/3.6pm.wav'), 'r': Sound('pm_sound/3.5pm.wav'), '4': Sound('pm_sound/3.4pm.wav'),
                'g': Sound('pm_sound/4.6pm.wav'), 't': Sound('pm_sound/4.5pm.wav'), '5': Sound('pm_sound/4.4pm.wav'),
                'h': Sound('pm_sound/5.6pm.wav'), 'y': Sound('pm_sound/5.5pm.wav'), '6': Sound('pm_sound/5.4pm.wav'),
                'j': Sound('pm_sound/6.6pm.wav'), 'u': Sound('pm_sound/6.5pm.wav'), '7': Sound('pm_sound/6.4pm.wav'),
                'k': Sound('pm_sound/7.6pm.wav'), 'i': Sound('pm_sound/7.5pm.wav'), '8': Sound('pm_sound/7.4pm.wav'),
                'l': Sound('pm_sound/8.6pm.wav'), 'o': Sound('pm_sound/8.5pm.wav'), '9': Sound('pm_sound/8.4pm.wav'),
                ';': Sound('pm_sound/9.6pm.wav'), 'p': Sound('pm_sound/9.5pm.wav'), '0': Sound('pm_sound/9.4pm.wav')
                }

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            for button in buttons_group:
                button.process()

            mods = pygame.key.get_mods()
            note(event, mods, sound, sound_pm)


def du_hast():
    pygame.init()

    font2 = pygame.font.Font(None, 100)
    font3 = pygame.font.Font(None, 70)

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Du Hast')
    screen.fill('white')

    Button(1500, 20, 80, 80, screen, onclickFunction=retrn, buttonText='X', button_color='red')
    Button(10, 355, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')
    Button(10, 595, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')

    description = font2.render('Du Hast', True, (50, 50, 50))

    x3 = font3.render('x3', True, (50, 50, 50))
    screen.blit(description, (100, 10))

    es1 = pygame.image.load('pict/du_hast1.png')
    es2 = pygame.image.load('pict/du_hast2.png')

    screen.blit(es1, (70, 270))
    screen.blit(es2, (70, 502))

    screen.blit(x3, (1500, 350))
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
    sound_pm = {'a': Sound('pm_sound/0.6pm.wav'), 'q': Sound('pm_sound/0.5pm.wav'), '1': Sound('pm_sound/0.4pm.wav'),
                's': Sound('pm_sound/1.6pm.wav'), 'w': Sound('pm_sound/1.5pm.wav'), '2': Sound('pm_sound/1.4pm.wav'),
                'd': Sound('pm_sound/2.6pm.wav'), 'e': Sound('pm_sound/2.5pm.wav'), '3': Sound('pm_sound/2.4pm.wav'),
                'f': Sound('pm_sound/3.6pm.wav'), 'r': Sound('pm_sound/3.5pm.wav'), '4': Sound('pm_sound/3.4pm.wav'),
                'g': Sound('pm_sound/4.6pm.wav'), 't': Sound('pm_sound/4.5pm.wav'), '5': Sound('pm_sound/4.4pm.wav'),
                'h': Sound('pm_sound/5.6pm.wav'), 'y': Sound('pm_sound/5.5pm.wav'), '6': Sound('pm_sound/5.4pm.wav'),
                'j': Sound('pm_sound/6.6pm.wav'), 'u': Sound('pm_sound/6.5pm.wav'), '7': Sound('pm_sound/6.4pm.wav'),
                'k': Sound('pm_sound/7.6pm.wav'), 'i': Sound('pm_sound/7.5pm.wav'), '8': Sound('pm_sound/7.4pm.wav'),
                'l': Sound('pm_sound/8.6pm.wav'), 'o': Sound('pm_sound/8.5pm.wav'), '9': Sound('pm_sound/8.4pm.wav'),
                ';': Sound('pm_sound/9.6pm.wav'), 'p': Sound('pm_sound/9.5pm.wav'), '0': Sound('pm_sound/9.4pm.wav')
                }

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            for button in buttons_group:
                button.process()

            mods = pygame.key.get_mods()
            note(event, mods, sound, sound_pm)


def one():

    pygame.init()

    font2 = pygame.font.Font(None, 100)
    font3 = pygame.font.Font(None, 70)

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('One')
    screen.fill('white')

    Button(1500, 20, 80, 80, screen, onclickFunction=retrn, buttonText='X', button_color='red')
    Button(10, 155, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')
    Button(10, 395, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')
    Button(10, 635, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')

    description = font2.render('One', True, (50, 50, 50))
    x2 = font3.render('x2', True, (50, 50, 50))
    x5 = font3.render('x5', True, (50, 50, 50))
    screen.blit(description, (100, 10))

    es1 = pygame.image.load('pict/one1.png')
    es2 = pygame.image.load('pict/one2.png')
    es3 = pygame.image.load('pict/one3.png')

    screen.blit(es1, (70, 70))
    screen.blit(es2, (70, 302))
    screen.blit(es3, (70, 550))

    screen.blit(x2, (870, 170))
    screen.blit(x5, (1100, 640))

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
    sound_pm = {'a': Sound('pm_sound/0.6pm.wav'), 'q': Sound('pm_sound/0.5pm.wav'), '1': Sound('pm_sound/0.4pm.wav'),
                's': Sound('pm_sound/1.6pm.wav'), 'w': Sound('pm_sound/1.5pm.wav'), '2': Sound('pm_sound/1.4pm.wav'),
                'd': Sound('pm_sound/2.6pm.wav'), 'e': Sound('pm_sound/2.5pm.wav'), '3': Sound('pm_sound/2.4pm.wav'),
                'f': Sound('pm_sound/3.6pm.wav'), 'r': Sound('pm_sound/3.5pm.wav'), '4': Sound('pm_sound/3.4pm.wav'),
                'g': Sound('pm_sound/4.6pm.wav'), 't': Sound('pm_sound/4.5pm.wav'), '5': Sound('pm_sound/4.4pm.wav'),
                'h': Sound('pm_sound/5.6pm.wav'), 'y': Sound('pm_sound/5.5pm.wav'), '6': Sound('pm_sound/5.4pm.wav'),
                'j': Sound('pm_sound/6.6pm.wav'), 'u': Sound('pm_sound/6.5pm.wav'), '7': Sound('pm_sound/6.4pm.wav'),
                'k': Sound('pm_sound/7.6pm.wav'), 'i': Sound('pm_sound/7.5pm.wav'), '8': Sound('pm_sound/7.4pm.wav'),
                'l': Sound('pm_sound/8.6pm.wav'), 'o': Sound('pm_sound/8.5pm.wav'), '9': Sound('pm_sound/8.4pm.wav'),
                ';': Sound('pm_sound/9.6pm.wav'), 'p': Sound('pm_sound/9.5pm.wav'), '0': Sound('pm_sound/9.4pm.wav')
                }

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            for button in buttons_group:
                button.process()

            mods = pygame.key.get_mods()
            note(event, mods, sound, sound_pm)


def holier_than_thou():

    pygame.init()

    font2 = pygame.font.Font(None, 100)
    font3 = pygame.font.Font(None, 70)

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Holier Than Thou')
    screen.fill('white')

    Button(1500, 20, 80, 80, screen, onclickFunction=retrn, buttonText='X', button_color='red')
    Button(10, 155, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')
    Button(10, 395, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')
    Button(10, 630, 50, 50, screen, onclickFunction=play_fragment, buttonText='|>', button_color='grey')

    description = font2.render('Holier Than Thou', True, (50, 50, 50))
    x23 = font3.render('x23', True, (50, 50, 50))
    x3 = font3.render('x3', True, (50, 50, 50))
    screen.blit(description, (100, 10))

    es1 = pygame.image.load('pict/holier_than_thou1.png')
    es2 = pygame.image.load('pict/holier_than_thou2.png')
    es3 = pygame.image.load('pict/holier_than_thou3.png')

    screen.blit(es1, (70, 70))
    screen.blit(es2, (70, 302))
    screen.blit(es3, (70, 540))

    screen.blit(x23, (690, 170))
    screen.blit(x3, (1120, 635))

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
    sound_pm = {'a': Sound('pm_sound/0.6pm.wav'), 'q': Sound('pm_sound/0.5pm.wav'), '1': Sound('pm_sound/0.4pm.wav'),
                's': Sound('pm_sound/1.6pm.wav'), 'w': Sound('pm_sound/1.5pm.wav'), '2': Sound('pm_sound/1.4pm.wav'),
                'd': Sound('pm_sound/2.6pm.wav'), 'e': Sound('pm_sound/2.5pm.wav'), '3': Sound('pm_sound/2.4pm.wav'),
                'f': Sound('pm_sound/3.6pm.wav'), 'r': Sound('pm_sound/3.5pm.wav'), '4': Sound('pm_sound/3.4pm.wav'),
                'g': Sound('pm_sound/4.6pm.wav'), 't': Sound('pm_sound/4.5pm.wav'), '5': Sound('pm_sound/4.4pm.wav'),
                'h': Sound('pm_sound/5.6pm.wav'), 'y': Sound('pm_sound/5.5pm.wav'), '6': Sound('pm_sound/5.4pm.wav'),
                'j': Sound('pm_sound/6.6pm.wav'), 'u': Sound('pm_sound/6.5pm.wav'), '7': Sound('pm_sound/6.4pm.wav'),
                'k': Sound('pm_sound/7.6pm.wav'), 'i': Sound('pm_sound/7.5pm.wav'), '8': Sound('pm_sound/7.4pm.wav'),
                'l': Sound('pm_sound/8.6pm.wav'), 'o': Sound('pm_sound/8.5pm.wav'), '9': Sound('pm_sound/8.4pm.wav'),
                ';': Sound('pm_sound/9.6pm.wav'), 'p': Sound('pm_sound/9.5pm.wav'), '0': Sound('pm_sound/9.4pm.wav')
                }

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            for button in buttons_group:
                button.process()

            mods = pygame.key.get_mods()
            note(event, mods, sound, sound_pm)


def free_play():
    pygame.init()

    font2 = pygame.font.Font(None, 100)
    font3 = pygame.font.Font(None, 70)

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Свободная игра')
    screen.fill('white')

    Button(1500, 20, 80, 80, screen, onclickFunction=retrn, buttonText='X', button_color='red')

    description = font2.render('Свободная игра', True, (50, 50, 50))
    x = font3.render('Здесь можно свободно сыграть что угодно', True, (50, 50, 50))
    screen.blit(description, (100, 10))

    es1 = pygame.image.load('pict/grif_gitari.png')

    screen.blit(es1, (100, 300))

    screen.blit(x, (100, 700))

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
    sound_pm = {'a': Sound('pm_sound/0.6pm.wav'), 'q': Sound('pm_sound/0.5pm.wav'), '1': Sound('pm_sound/0.4pm.wav'),
                's': Sound('pm_sound/1.6pm.wav'), 'w': Sound('pm_sound/1.5pm.wav'), '2': Sound('pm_sound/1.4pm.wav'),
                'd': Sound('pm_sound/2.6pm.wav'), 'e': Sound('pm_sound/2.5pm.wav'), '3': Sound('pm_sound/2.4pm.wav'),
                'f': Sound('pm_sound/3.6pm.wav'), 'r': Sound('pm_sound/3.5pm.wav'), '4': Sound('pm_sound/3.4pm.wav'),
                'g': Sound('pm_sound/4.6pm.wav'), 't': Sound('pm_sound/4.5pm.wav'), '5': Sound('pm_sound/4.4pm.wav'),
                'h': Sound('pm_sound/5.6pm.wav'), 'y': Sound('pm_sound/5.5pm.wav'), '6': Sound('pm_sound/5.4pm.wav'),
                'j': Sound('pm_sound/6.6pm.wav'), 'u': Sound('pm_sound/6.5pm.wav'), '7': Sound('pm_sound/6.4pm.wav'),
                'k': Sound('pm_sound/7.6pm.wav'), 'i': Sound('pm_sound/7.5pm.wav'), '8': Sound('pm_sound/7.4pm.wav'),
                'l': Sound('pm_sound/8.6pm.wav'), 'o': Sound('pm_sound/8.5pm.wav'), '9': Sound('pm_sound/8.4pm.wav'),
                ';': Sound('pm_sound/9.6pm.wav'), 'p': Sound('pm_sound/9.5pm.wav'), '0': Sound('pm_sound/9.4pm.wav')
                }

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            for button in buttons_group:
                button.process()

            mods = pygame.key.get_mods()
            note(event, mods, sound, sound_pm)


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/MainMenu.ui', self)
        self.setFixedSize(*size)
        self.enter_sandman_song.clicked.connect(enter_sandman)
        self.du_hast_song.clicked.connect(du_hast)
        self.one_song.clicked.connect(one)
        self.holier_than_thou_song.clicked.connect(holier_than_thou)
        self.free_play_button.clicked.connect(free_play)
        self.hint_button.clicked.connect(self.hint_show)

    def hint_show(self):
        self.hw = HintWindow()
        self.setCentralWidget(self.hw)
        self.hw.show()
        self.mm = MainMenu()
        self.mm.setVisible(False)


class HintWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/HintWindow.ui', self)
        self.setFixedSize(*size)
        self.exit_button.clicked.connect(self.exit)
        self.pict2.setPixmap(QPixmap('pict/hint_pict1.png'))
        self.pict1.setPixmap(QPixmap('pict/grif_gitari.png'))

    def exit(self):
        self.mm = MainMenu()
        self.setCentralWidget(self.mm)
        self.mm.show()
        self.hw = HintWindow()
        self.hw.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec())








