import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1920, 1000))
pygame.display.set_caption('MERGING BIOG MUSCLESSDS GAMES')
clock = pygame.time.Clock()
testFont = pygame.font.Font(None, 85)
background = pygame.Surface((820, 820))
background.fill((42, 42, 255))#sets up the window
running = True #when set as false, the window closes. used in whileloop further down

class Bros:
    def __init__(self, rank):
        self.pos = [random.randint(0, 1920), random.randint(0, 1000)]
        #print(self.pos)
        self.rank = rank
    def drawSelf(self):
        pygame.draw.circle(screen, (0, 0, 0), self.pos, 100)
    
    def move(self):
        self.pos[0] += random.randint(-100, 100)
        self.pos[1] += random.randint(-100, 100)




b1 = Bros(0)

while running:
    screen.fill((255, 255, 255))  # fills screen background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                b1.move()
    
    b1.drawSelf()
    
    pygame.draw.circle(screen, (255, 0, 0), (960, 500), 3)

    pygame.display.update()
    clock.tick(60)
    #print('frame')
