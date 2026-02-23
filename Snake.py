import pygame
import time
from random import *
#wtf
#another_shii
def get_apple():
    apple = (randrange(20, 600, 20), randrange(20, 400, 20))
    return apple

def dead():
    global horizontal, vertical, screen_size
    if (int(horizontal) >= 600 or int(horizontal) <= 0) or (int(vertical) >= 400 or int(vertical) <= 0):
        return True

pygame.init()
screen = pygame.display.set_mode((600, 400 ))
speed = 0.08
horizontal, vertical = 100, 200
clock = pygame.time.Clock()
snake = (20, 20)
k_word = ''
apple_cord = get_apple()
button_pressed = False
direction = True
running = True

while running:
    clock.tick(10)
    pygame.draw.rect(screen, 'green', (*apple_cord, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            button_pressed = True

            if key[pygame.K_UP]: #minus y
                k_word = 'y'
                direction = True

            if key[pygame.K_DOWN]: #plus y
                k_word = 'y'
                direction = False

            if key[pygame.K_RIGHT]: #plus x
                k_word = 'x'
                direction = True

            if key[pygame.K_LEFT]: #minus x
                k_word = 'x'
                direction = False

    if dead():
        running = False

    if horizontal == apple_cord[0] and vertical == apple_cord[-1]:
        screen.fill('black')
        apple_cord = get_apple()
        pygame.draw.rect(screen, 'green', (*apple_cord, 20, 20))
        pygame.display.flip()

    if button_pressed:  #moves

        if direction:

            if k_word == 'y':
                pygame.draw.rect(screen, 'red', (horizontal, vertical, *snake,))
                vertical -= 20
                pygame.display.flip()
                screen.fill('black')

            elif k_word == 'x':
                pygame.draw.rect(screen, 'red', (horizontal, vertical, *snake,))
                horizontal += 20
                pygame.display.flip()
                screen.fill('black')

        elif not direction:

            if k_word == 'y':
                pygame.draw.rect(screen, 'red', (horizontal, vertical, *snake,))
                vertical += 20
                pygame.display.flip()
                screen.fill('black')


            elif k_word == 'x':
                pygame.draw.rect(screen, 'red', (horizontal, vertical, *snake,))
                horizontal -= 20
                pygame.display.flip()
                screen.fill('black')

    else:
        pygame.draw.rect(screen,'red',(horizontal, vertical, *snake,))
        horizontal+=20
        pygame.display.flip()
        screen.fill('black')

if dead():
    font = pygame.font.SysFont(None, 50)
    text_surface = font.render("YOU LOST", True, (255, 255, 255))
    time.sleep(1)
    screen.fill('blue')
    screen.blit(text_surface, (200, 150))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()

pygame.quit()
