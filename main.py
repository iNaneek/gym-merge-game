import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Gym Merge Game')
clock = pygame.time.Clock()
running = True #when set as false, the window closes. used in whileloop further down

pictureBackground = pygame.transform.scale(pygame.image.load('Gym Background.png'), (1000, 500))
class Character:
    rankOptions = (
        (100, pygame.transform.scale(pygame.image.load('crack.png'), (100, 100))),
        (60, pygame.transform.scale(pygame.image.load('Bench - Bar.png'), (60, 60))),
        (80, pygame.transform.scale(pygame.image.load('Bench - 10.png'), (80, 80))),
        (100, pygame.transform.scale(pygame.image.load('Bench - 25.png'), (100, 100))),
        (150, pygame.transform.scale(pygame.image.load('Bench - 45.png'), (150, 150))),
        (200, pygame.transform.scale(pygame.image.load('Bench - 2x45.png'), (200, 200)))
    )
    def __init__(self, rank):
        self.position = [random.randint(0, 1000), random.randint(0, 500)]
        self.rank = rank
        self.onMouse = False
        self.size = self.rankOptions[self.rank][0]
        
    def rankChange(self):
        self.size = self.rankOptions[self.rank][0]

    def drawSelf(self):
        screen.blit(self.rankOptions[self.rank][1], (self.position[0] - self.size / 2, self.position[1] - self.size / 2))

def findRahVal(allCharacter):
    for k1 in allCharacter.keys():
        for k2 in allCharacter.keys():
            if k1 != k2 and abs(allCharacter[k1].position[0] - allCharacter[k2].position[0]) + abs(allCharacter[k1].position[1] - allCharacter[k2].position[1]) < 30:
                return (k1, k2)


characterDictionary = {}

characterDictionary[len(characterDictionary)] = Character(0)
characterDictionary[len(characterDictionary)] = Character(0)

timer = 0
mouseHolding = False
while running:
    screen.fill((255, 255, 255))  # fills screen background
    screen.blit(pictureBackground, (0, 0))

    timer += 1

    if timer%100 == 1:
        characterDictionary[list(characterDictionary)[-1] + 1] = Character(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #exit()

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                characterDictionary[list(characterDictionary)[-1] + 1] = Character(0)
        
        mouseClick = pygame.mouse.get_pressed(num_buttons=3)[0]
        if mouseClick == True:
            mousePosition = pygame.mouse.get_pos()
            for character in characterDictionary.values():
                if abs(character.position[0] - mousePosition[0]) < character.size / 2 and abs(character.position[1] - mousePosition[1]) < character.size / 2 and mouseHolding == False:
                    if character.rank == 0:
                        character.rank = 1
                        character.rankChange()
                        break
                    character.onMouse = True
                    mouseHolding = True
                    break
        
        if mouseClick == False:
            for character in characterDictionary.values():
                character.onMouse = False
            mouseHolding = False
    
    for character in characterDictionary.values():
        if character.onMouse == True:
            character.position = mousePosition
        character.drawSelf()


    rahVal = findRahVal(characterDictionary)

    if rahVal:
        if characterDictionary[rahVal[0]].rank == characterDictionary[rahVal[1]].rank and characterDictionary[rahVal[0]].rank != 5:
            characterDictionary[rahVal[0]].rank += 1
            characterDictionary[rahVal[0]].rankChange()
            characterDictionary.pop(rahVal[1]) 
    

    pygame.display.update()
    clock.tick(60)

