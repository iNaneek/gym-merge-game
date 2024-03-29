import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('MERGING BIOG MUSCLESSDS GAMES')
clock = pygame.time.Clock()
testFont = pygame.font.Font(None, 85)
background = pygame.Surface((820, 820))
background.fill((42, 42, 255))#sets up the window
running = True #when set as false, the window closes. used in whileloop further down

class Bros:
    def __init__(self, rank):
        self.pos = [random.randint(0, 1000), random.randint(0, 500)]
        #print(self.pos)
        self.rank = rank
        self.onMouse = False
    def drawSelf(self):
        pygame.draw.circle(screen, (0, 0, 0), self.pos, 20)
    
    def move(self):
        self.pos[0] += random.randint(-100, 100)
        self.pos[1] += random.randint(-100, 100)


brosDict = {}

brosDict[len(brosDict)] = Bros(0)



while running:
    screen.fill((255, 255, 255))  # fills screen background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                brosDict[len(brosDict)] = Bros(0)
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            mousePos = pygame.mouse.get_pos()
            for bro in brosDict:
                if abs(bro.pos[0] - mousePos[0]) < 10 and abs(bro.pos[1] - mousePos[1]) < 10:
                    print("rahh")
    
    for i in brosDict:
        brosDict[i].drawSelf()
    
    pygame.draw.circle(screen, (255, 0, 0), (500, 250), 3)

    pygame.display.update()
    clock.tick(60)
    #print('frame')
