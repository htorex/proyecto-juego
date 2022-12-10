import pygame
import random


from settings import SIZE_BULLET
from settings import RED
from settings import WHITE
from settings import width_field
from settings import height_field
from settings import width_bullet
from settings import height_bullet

class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.width = width_bullet
        self.heigth = height_bullet

        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.speed = 30
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

        
        self.surface = pygame.Surface(SIZE_BULLET, pygame.SRCALPHA, 32)
        self.rect = self.surface.get_rect()
        
        self.surface.fill(WHITE)
        pygame.draw.circle(self.surface, RED, (12.5, 12.5), 12.5)
        
    
    def draw(self, surface):
        

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y


        surface.blit(self.surface, self.rect)


    def move(self):
        self.validate_move()

        self.pos_x += self.dir_x
        self.pos_y += self.dir_y

                


    def validate_move(self):

        if self.pos_x >= 39:
            self.dir_x = -self.dir_x

        if self.pos_x <= width_field:
            self.dir_x = -self.dir_x

        if self.pos_y >= 22:
            self.dir_y = -self.dir_y
        
        if self.pos_y <= height_field:
            self.dir_y = -self.dir_y

    