#### ---- LIBRARIES ---- ####
import random
import pygame
import tsk
pygame.init()

#### ------------------------------- ####
#### ---- GET FILENAME FUNCTION ---- ####
#### ------------------------------- ####
def get_filename(num):
    if num == 0:
        return "SmallBrownRock.png"
    elif num == 1:
        return "RoundGemBlue.png"
    elif num == 2:
        return "RoundGemBrown.png"
    elif num == 3:
        return "RoundGemPink.png"
    elif num == 4:
        return "RoundGemRed.png"

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("Desert.jpg", 0, 0)

images = []
for i in range(6):
    new_pic = random.randint(1, 4)
    images.append(new_pic)

random_rock = random.randint(0, len(images) - 1)
images[random_rock] = 0

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    #### ---- DRAW ---- ####
    background.draw()

    for i in range(len(images)):
        x = 90 + (i * 150)
        filename = get_filename(images[i])
        sprite = tsk.Sprite(filename, x, 0)
        sprite.center_y = 280
        sprite.draw()

    pygame.display.flip()
