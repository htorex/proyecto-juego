import pygame
import sys


from hero import Player
from bullet import Bullet
from enemy import Enemy
from field import Field
from settings import SIZE
from settings import WHITE


pygame.init()

game = True

screen = pygame.display.set_mode(SIZE)


pygame.display.set_caption("Proyecto")

clock = pygame.time.Clock()

field_C = Field(39,22)

player = Player(250, 390)
enemy = Enemy(200, 150)
bullet = Bullet(240, 285)


background = pygame.image.load("asset/fut1.png").convert()


while game:
    clock.tick(200)  
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
            sys.exit()
    
    
    

    key_pressed = pygame.key.get_pressed()
    

    if key_pressed[pygame.K_w]:
        player.up() 
    
    if key_pressed[pygame.K_d]:
        player.rigth()

    if key_pressed[pygame.K_s]:
        player.down()

    if key_pressed[pygame.K_a]:
        player.left()

    key_pressed_enemy = pygame.key.get_pressed()
    

    if key_pressed_enemy[pygame.K_UP]:
        enemy.up() 
    
    if key_pressed_enemy[pygame.K_RIGHT]:
        enemy.rigth()

    if key_pressed_enemy[pygame.K_DOWN]:
        enemy.down()

    if key_pressed_enemy[pygame.K_LEFT]:
        enemy.left()
    
    



    # Pantalla
    field_C.draw(screen)
    screen.fill(WHITE)
    screen.blit(background,[0, 0])
    

    # Jugadores
    player.draw(screen)
    enemy.draw(screen)
    bullet.draw(screen) 
    bullet.move()


    pygame.display.flip()
