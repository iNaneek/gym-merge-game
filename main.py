import pygame
import random

pygame.init()
screen = pygame.display.set_mode((820, 820))
pygame.display.set_caption('2048')
clock = pygame.time.Clock()
testFont = pygame.font.Font(None, 85)
background = pygame.Surface((820, 820))
background.fill((42, 42, 42))#sets up the window
running = True #when set as false, the window closes. used in whileloop further down

class Goat():
    def __init__():
        self.pos = (random.randint(0, 10), random.randint(0, 10))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                pass
    
    screen.fill((0, 0, 0))  # fills screen background

    pygame.draw.circle(screen, (255, 0, 0), (500, 500), 3)

    pygame.display.update()
    clock.tick(60)
    #print('frame')
