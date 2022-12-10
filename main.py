import pygame
import sys


from hero import Player
from bullet import Bullet
from enemy import Enemy
from field import Field
from field import SupField
from settings import SIZE
from settings import WHITE
from settings import YELLOW
# from settings import fuente1
# from settings import fuente2


pygame.init()

game = True

screen = pygame.display.set_mode(SIZE)


pygame.display.set_caption("Proyecto")

clock = pygame.time.Clock()
# Campo
field_C = Field(39,22)
field_sup = SupField(200,20)
field_inf = SupField(200, 570)

# Jugadores
player = Player(250, 390)
enemy = Enemy(200, 150)
bullet = Bullet(240, 285)

#Puntuacion
#punto_sup = fuente1.render("0", 0)
#punto_bajo = fuente2.render("1", 0)

background = pygame.image.load("asset/fut1.png").convert()


while game:
    clock.tick(100)  
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
            sys.exit()
    
    
    
    # Movimientos Player 1 
    key_pressed = pygame.key.get_pressed()
    

    if key_pressed[pygame.K_w]:
        player.up() 
    
    if key_pressed[pygame.K_d]:
        player.rigth()

    if key_pressed[pygame.K_s]:
        player.down()

    if key_pressed[pygame.K_a]:
        player.left()


    # Movimientos Player 2 
    key_pressed_enemy = pygame.key.get_pressed()
    

    if key_pressed_enemy[pygame.K_UP]:
        enemy.up() 
    
    if key_pressed_enemy[pygame.K_RIGHT]:
        enemy.rigth()

    if key_pressed_enemy[pygame.K_DOWN]:
        enemy.down()

    if key_pressed_enemy[pygame.K_LEFT]:
        enemy.left()
    
    
    # Rebote con player 1 y player 2
    

   


    # Pantalla
    field_C.draw(screen)
    screen.fill(WHITE)
    screen.blit(background,[0, 0])
    
    # puntos o msj
    #screen.blit(punto_sup, (200, 200))

    # Zona Punto
    field_sup.draw(screen)
    field_inf.draw(screen)

    # Jugadores
    player.draw(screen)
    enemy.draw(screen)
    bullet.draw(screen) 
    bullet.move()
    player.touch(bullet)
    enemy.touch(bullet)
    pygame.display.flip()
