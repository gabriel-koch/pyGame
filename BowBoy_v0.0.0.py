# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:05:29 2018

@author: Koch
"""

import pygame as pg 

#initialize
pg.init()



#Global Variables
ScreenX, ScreenY = (800,600)
screen = pg.display.set_mode((ScreenX, ScreenY))
done = False


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((60,60))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = ScreenX/2
        self.rect.centery = ScreenY/3
        self.spdX, self.spdY = 0, 0


class tiles(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((800,60))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = ScreenX/2
        self.rect.centery = 200



#Game loop
while not done:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                    done = True
    



    
    p1 = Player()
    all_sprites = pg.sprite.Group()
    


    # Atualização
    all_sprites.update()

    #Camera
    all_sprites.add(p1)

    # Desenhar
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()