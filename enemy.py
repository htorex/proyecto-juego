import pygame


from settings import RED
from settings import SIZE_ENEMY
from settings import YELLOW
from settings import width
from settings import height
from settings import height_enemy
from settings import width_enemy
from settings import LATERAL_SIZE

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)     

        self.width = 40
        self.heigth = 40  

        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.speed = 300
        self.direction = 0
        
        self.surface = pygame.Surface(SIZE_ENEMY, pygame.SRCALPHA, 32)
        self.rect = self.surface.get_rect()
        
        self.surface.fill(YELLOW)
        pygame.draw.circle(self.surface, RED, (25, 25), 25)


    def draw(self, surface):
        self.validate_move()

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        surface.blit(self.surface, self.rect)

    def up(self):
        self.pos_y -= 1


    def down(self):
        self.pos_y += 1


    def rigth(self):
        self.pos_x += 1


    def left(self):
        self.pos_x -= 1


    def move(self):
        self.validate_move()

        if self.direction == 0:
            self.pos_y -= self.speed
        
        elif self.direction == 1:
            self.pos_x += self.speed
        
        elif self.direction == 2:
            self.pos_y += self.speed
        
        elif self.direction == 3:
            self.pos_x -=  self.speed

    def validate_move(self):

        if self.pos_x <= 0:
            self.pos_x = 0

        if self.pos_x >= (width - width_enemy):
            self.pos_x = width - width_enemy

        if self.pos_y <= 0:
            self.pos_y = 0

        if self.pos_y >= (height - height_enemy):
            self.pos_y = height - height_enemy

