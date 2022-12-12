import pygame
import sys

import score 
from hero import Player
from bullet import Bullet
from enemy import Enemy
from field import Field
from field import SupField
from settings import SIZE
from settings import WHITE
from settings import YELLOW
from settings import RED
from settings import GREEN
from settings import fuente1
from settings import fuente2
from settings import font


pygame.init()
pygame.font.init()

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
puntosup = 0
puntobajo = 0

score_txt = int(score.archivo())


counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)


background = pygame.image.load("asset/fut1.png").convert()


while game:
    clock.tick(100)  

    
    for event in pygame.event.get():

        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Se acabo!'

        if event.type == pygame.QUIT:
            game = False
    
    if counter >= 0:
        punto_sup = fuente1.render(str(puntosup), 0, YELLOW)
        punto_bajo = fuente2.render(str(puntobajo), 0, RED)
        
        if pygame.sprite.collide_rect(bullet, field_sup) and bullet.toc_up:         
            bullet.toc_up = False
            puntosup += 1
            

        if (not pygame.sprite.collide_rect(bullet, field_sup)) and (not bullet.toc_up):         
            bullet.toc_up = True
            

        if pygame.sprite.collide_rect(bullet, field_inf) and bullet.toc_dow:
            bullet.toc_dow = False
            puntobajo += 1
            
        
        if (not pygame.sprite.collide_rect(bullet, field_inf)) and (not bullet.toc_dow):
            bullet.toc_dow = True

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
        
    
        # Pantalla
        field_C.draw(screen)
        screen.fill(WHITE)
        screen.blit(background,[0, 0])
        

        # puntos o msj
        screen.blit(punto_sup, (240, 250))
        screen.blit(punto_bajo, (240, 315))
        screen.blit(font.render(f"Tiempo: {text}", True, GREEN), (60, 610))
        screen.blit(font.render(f"Maximo: {score_txt}", True, GREEN), (280, 640))


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

        if (puntosup + puntobajo) > score_txt:
            screen.blit(font.render("Se hicieron mas goles ", True, GREEN), (120, 660))

                
        pygame.display.flip()

    
            

if score_txt < (puntosup + puntobajo):
    resultado = (puntosup + puntobajo)
    score.escribir(resultado)