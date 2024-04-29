import pygame
import random

#Initialize the game window
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Gym Merge Game')
clock = pygame.time.Clock()
running = True #when set as false, the window closes. used in while loop further down

#Defines the background
pictureBackground = pygame.transform.scale(pygame.image.load('Gym Background.png'), (1000, 500))

#Creates a class for each type of character with the size, proper image, and image size
class Character:
    rankOptions = (
        (100, pygame.transform.scale(pygame.image.load('Protein Powder.png'), (100, 100))),
        (60, pygame.transform.scale(pygame.image.load('Bench - Bar.png'), (60, 60))),
        (80, pygame.transform.scale(pygame.image.load('Bench - 10.png'), (80, 80))),
        (100, pygame.transform.scale(pygame.image.load('Bench - 25.png'), (100, 100))),
        (150, pygame.transform.scale(pygame.image.load('Bench - 45.png'), (150, 150))),
        (200, pygame.transform.scale(pygame.image.load('Bench - 2x45.png'), (200, 200)))
    )
    
    #When a new character is made, this function creates the object
    def __init__(self, rank):
        self.position = [random.randint(0, 1000), random.randint(0, 500)]
        self.rank = rank
        self.onMouse = False
        self.size = self.rankOptions[self.rank][0]
        
    #Changes the rank of an Object when the character is being changed    
    def rankChange(self):
        self.size = self.rankOptions[self.rank][0]

    #Draws the Character on its position on the screen
    def drawSelf(self):
        screen.blit(self.rankOptions[self.rank][1], (self.position[0] - self.size / 2, self.position[1] - self.size / 2))

#Finds any characters of the same rank at the same position and returns them.
def findRahVal(allCharacter):
    for k1 in allCharacter.keys():
        for k2 in allCharacter.keys():
            if k1 != k2 and abs(allCharacter[k1].position[0] - allCharacter[k2].position[0]) + abs(allCharacter[k1].position[1] - allCharacter[k2].position[1]) < 30:
                return (k1, k2)

#Initializes the Dictionary that holds each object on screen
characterDictionary = {}

#Spawns 2 jars of Protein Powder at the start
characterDictionary[len(characterDictionary)] = Character(0)
characterDictionary[len(characterDictionary)] = Character(0)

timer = 0
mouseHolding = False
while running:
    #Puts the background on the screen
    screen.fill((255, 255, 255))  # fills screen background
    screen.blit(pictureBackground, (0, 0))

    timer += 1

    #Spawns Protein Powder every 100 Frames
    if timer%100 == 1:
        characterDictionary[list(characterDictionary)[-1] + 1] = Character(0)

    #Quits the game if the close button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #exit()

        #Spawns a jar of Protein Powder if the spacebar is pressed
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                characterDictionary[list(characterDictionary)[-1] + 1] = Character(0)
        
        
        #Allows for characters to be grabbed and sets a range for the space where they react to the mouse
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
        
        #Stops holding characters once the mouse is not clicked
        if mouseClick == False:
            for character in characterDictionary.values():
                character.onMouse = False
            mouseHolding = False
    
    #Moves any clicked character to the position of the mouse
    for character in characterDictionary.values():
        if character.onMouse == True:
            character.position = mousePosition
        character.drawSelf()

    #Finds any characters that need to be merged
    rahVal = findRahVal(characterDictionary)

    #Using previously found characters, one item is deleted and the other ranks up, effectively merging the two. Also makes sure that characters don't merge above the maximum rank
    if rahVal:
        if characterDictionary[rahVal[0]].rank == characterDictionary[rahVal[1]].rank and characterDictionary[rahVal[0]].rank != 5:
            characterDictionary[rahVal[0]].rank += 1
            characterDictionary[rahVal[0]].rankChange()
            characterDictionary.pop(rahVal[1]) 
    
    #Updates the screen and sets the framerate to 60 FPS
    pygame.display.update()
    clock.tick(60)
