#!/usr/bin/env python

import pygame
from pygame.locals import *  # buat jaga-jaga
import sys
import random
import time
#import 



class FlappyBird:
    def __init__(self):
        try:
         self.arg1 = sys.argv[1]
        except:
            self.arg1 = None
        print("""
``````##``````##````````````````````````````````````````````````````````````````
``````##`````##`````######`````##```````````````##``####``##```#####````````````
``````##````##`````#``````#`````##`````````````##```####``##``#````##```````````
``````##```##`````#````````#`````##```````````##``````````####``````#```````````
``````##``##`````#``````````#`````##`````````##`````####``##````````#```````````
``````##`##`````#```#########``````##```````##``````####``##````````#```````````
``````####```````#``````````````````##`````##```````####``##````````#```````````
``````####````````#``````````````````##```##````````####``##````````#```````````
``````##`##````````#``````````````````##`##`````````####``##````````#```````````
``````##``##````````#########``````````##```````````####``##````````#```````````
``````##```##```````````````````````````````````````````````````````````````````
``````##````##``````````````````````````````````````````````````````````````````
``````##`````##`````````````````````````````````````````````````````````````````
``````##``````##````````````````````````````````````````````````````````````````

""")
        time.sleep(2)
        magicword = input('sebutkan mantranya... ')
        if magicword.lower() != 'alakadabra':
         print('salah mantra!!!...kan jadi error')
         sys.exit()
        self.screen = pygame.display.set_mode((400, 708))
        #self.screen = pygame.display.set_mode((720, 1280))
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("flapkev/dasar.png").convert()
        self.birdSprites = [pygame.image.load("flapkev/hidup1.png").convert_alpha(),
                            pygame.image.load("flapkev/hidup2.png").convert_alpha(),
                            pygame.image.load("flapkev/mati.png")]
        self.wallUp = pygame.image.load("flapkev/bawah.png").convert_alpha()
        self.wallDown = pygame.image.load("flapkev/atas.png").convert_alpha()
        self.gap = 130
        self.wallx = 400
        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-110, 110)

    def updateWalls(self):
        self.wallx -= 2
        if self.wallx < -80:
            self.wallx = 400
            self.counter += 1
            self.offset = random.randint(-110, 110)

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())
        if upRect.colliderect(self.bird):
            if self.arg1 == 'kebal':
             self.dead = False #True
            else:
             self.dead = True
        if downRect.colliderect(self.bird):
            if self.arg1 == 'kebal':
             self.dead = False #True
            else:
                self.dead = True
        if not 0 < self.bird[1] < 720:
            self.bird[1] = 50
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(-110, 110)
            self.gravity = 5

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #while (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                   
                       
                    
                    self.gravity = 5
                    self.jumpSpeed = 10
                    
                    self.jump = 17

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.wallUp,
                             (self.wallx, 360 + self.gap - self.offset))
            self.screen.blit(self.wallDown,
                             (self.wallx, 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter),
                                         -1,
                                         (255, 255, 255)),
                             (200, 50))
            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1
            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
            if not self.dead:
                self.sprite = 0
            self.updateWalls()
            self.birdUpdate()
            pygame.display.update()


FlappyBird().run()





