import pygame


from settings import GREEN
from settings import SIZE_PLAYER
from settings import WHITE
from settings import width
from settings import height
from settings import height_player
from settings import with_player

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)  

        self.width = 40
        self.heigth = 40  

        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.speed = 300
        self.direction = 0
        
        self.surface = pygame.Surface(SIZE_PLAYER, pygame.SRCALPHA, 32)
        self.rect = self.surface.get_rect()
        
        self.surface.fill(WHITE)
        pygame.draw.circle(self.surface, GREEN, (25,25), 25)
        


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

        if self.pos_x >= (width - with_player):
            self.pos_x = width - with_player

        if self.pos_y <= 0:
            self.pos_y = 0

        if self.pos_y >= (height -height_player):
            self.pos_y = height - height_player