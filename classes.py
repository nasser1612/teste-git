import pygame
from pygame import image
from pygame.locals import *
pygame.init()

class Statue():
    def __init__(self, posx, posy, sprites, sprite_duration, downtime, starts_at=0):
        self.images = sprites

        self.sprite_duration = sprite_duration
        self.downtime = downtime
        self.frame_count = starts_at
        self.timer = 0
        self.changing = False
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def change_image(self):
        self.frame_count += 1
        if self.frame_count == self.sprite_duration:
            self.index += 1
            # animation finished
            if self.index >= len(self.images):
                self.index = 0
                self.changing = False
            self.image = self.images[self.index]
            self.frame_count = 0

    def will_change(self):
        self.timer += 1
        if self.timer == self.downtime or self.changing:
            self.changing = True
            self.change_image()
            self.timer = 0

    def update(self):
        self.will_change()