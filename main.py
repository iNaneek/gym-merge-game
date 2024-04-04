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

pictureBackground = pygame.transform.scale(pygame.image.load('Gym Background.png'), (1000, 500))
class Bros:
    ranks = (
        (60, pygame.transform.scale(pygame.image.load('Bench - Bar.png'), (60, 60))),
        (80, pygame.transform.scale(pygame.image.load('Bench - 10.png'), (80, 80))),
        (100, pygame.transform.scale(pygame.image.load('Bench - 25.png'), (100, 100))),
        (150, pygame.transform.scale(pygame.image.load('Bench - 45.png'), (150, 150))),
        (200, pygame.transform.scale(pygame.image.load('Bench - 2x45.png'), (200, 200)))
    )
    def __init__(self, rank):
        self.pos = [random.randint(0, 1000), random.randint(0, 500)]
        #print(self.pos)
        self.rank = rank
        self.onMouse = False
        self.size = self.ranks[self.rank][0]\
        
    def findRank(self):
        self.size = self.ranks[self.rank][0]

    def drawSelf(self):
        screen.blit(self.ranks[self.rank][1], (self.pos[0] - self.size / 2, self.pos[1] - self.size / 2))
    
    def move(self):
        self.pos[0] += random.randint(-100, 100)
        self.pos[1] += random.randint(-100, 100)


brosDict = {}

brosDict[len(brosDict)] = Bros(0)
brosDict[len(brosDict)] = Bros(0)


selected = False
while running:
    screen.fill((255, 255, 255))  # fills screen background
    screen.blit(pictureBackground, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                brosDict[list(brosDict)[-1] + 1] = Bros(0)
        mouseClick = pygame.mouse.get_pressed(num_buttons=3)[0]
        if mouseClick == True:
            mousePos = pygame.mouse.get_pos()
            for bro in brosDict.values():
                if abs(bro.pos[0] - mousePos[0]) < bro.size / 2 and abs(bro.pos[1] - mousePos[1]) < bro.size / 2 and selected == False:
                    bro.onMouse = True
                    selected = True
                    break
        if mouseClick == False:
            for bro in brosDict.values():
                bro.onMouse = False
            selected = False
    
    for bro in brosDict.values():
        if bro.onMouse == True:
            bro.pos = mousePos
        bro.drawSelf()

    toMerge = None
    for k1 in brosDict.keys():
        for k2 in brosDict.keys():
            if k1 != k2 and abs(brosDict[k1].pos[0] - brosDict[k2].pos[0]) + abs(brosDict[k1].pos[1] - brosDict[k2].pos[1]) < 30:
                toMerge = (k1, k2)
    if toMerge:
        if brosDict[toMerge[0]].rank == brosDict[toMerge[1]].rank and brosDict[toMerge[0]].rank != 4:
            brosDict[toMerge[0]].rank += 1
            brosDict[toMerge[0]].findRank()
            brosDict.pop(toMerge[1]) #

        
    
    pygame.draw.circle(screen, (255, 0, 0), (500, 250), 3)
    

    pygame.display.update()
    clock.tick(60)
    #print('frame')
