import pygame

from settings import LATERAL_SIZE
from settings import SUP_SIZE
from settings import WHITE
from settings import FIELD_ZISE


class LeftField(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)  

        self.width = 40
        self.heigth = 40  

        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.speed = 300
        self.direction = 0
        
        self.surface = pygame.Surface(LATERAL_SIZE, pygame.SRCALPHA, 32)
        self.rect = self.surface.get_rect()

        self.surface.fill(WHITE)
        pygame.draw.rect(self.surface, WHITE, [25, 25, 700,700], 0)

    
    def Draw(self, surface):
        

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        surface.blit(self.surface, self.rect)


class SupField(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)  

        self.width = 40
        self.heigth = 40  

        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.speed = 300
        self.direction = 0
        
        self.surface = pygame.Surface(SUP_SIZE, pygame.SRCALPHA, 32)
        self.rect = self.surface.get_rect()

        self.surface.fill(WHITE)
        pygame.draw.rect(self.surface, WHITE, [250, 250, 25,25], 0)

    
    def Draw(self, surface):
        

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        surface.blit(self.surface, self.rect)


class Field(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)  

        self.width = 40
        self.heigth = 40  

        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.speed = 300
        self.direction = 0
        
        self.surface = pygame.Surface(FIELD_ZISE, pygame.SRCALPHA, 32)
        self.rect = self.surface.get_rect()

        self.surface.fill(WHITE)
        pygame.draw.rect(self.surface, WHITE, [250, 250, 25,25], 0)

    
    def draw(self, surface):
        

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        surface.blit(self.surface, self.rect)