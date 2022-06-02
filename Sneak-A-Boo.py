""" 
LESSON: 6.2 - Return Values
EXERCISE: Sneak-A-Boo
"""

#### ---- LIBRARIES ---- ####
import tsk
from random import randint
import pygame
pygame.init()



#### ----------------------------------- ####
#### ---- GET NEW LOCATION FUNCTION ---- ####
#### ----------------------------------- ####



def get_loc_p():
    return (randint(0, 1018 - 353), randint(0, 573 - 330))

def get_loc_g(loc_x, loc_y, speed, c):
    x, y = (loc_x, loc_y)
    if tsk.is_key_down(pygame.K_DOWN):
        y += speed * c.get_time()*2
    if tsk.is_key_down(pygame.K_UP):
        y -= speed * c.get_time()*2
    if tsk.is_key_down(pygame.K_LEFT):
        x -= speed * c.get_time()*2
    if tsk.is_key_down(pygame.K_RIGHT):
        x += speed * c.get_time()*2
    return (x, y)
#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# --- Setup --- #

w = pygame.display.set_mode([1018, 573])
ghost = tsk.Sprite("Ghost.png", 0, 0)
bg = tsk.Sprite("LivingRoom.jpg", 0, 0)
x, y = get_loc_p()
pson = tsk.Sprite("PersonReading.png", x, y)
x, y = (100, 100)
visible = True
timer = 0

c = pygame.time.Clock()
r = pygame.Rect(0, 0, 50, 1000)
s = 0.1

# --- Sprites --- #




# --- Variables --- #



playing = True
#### ---- MAIN LOOP ---- ####
while r.y < 573 and playing:
    r.y += int(s * c.get_time())
    timer += c.get_time()

    # --- Event Loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False



    # --- Calculate new ghost position --- #
    x, y = get_loc_g(x, y, s, c)



    # --- Move the timer bar down --- #
    if timer > 750 and not visible:
        timer = 0
        visible = True
    elif timer > 250 and visible:
        timer = 0
        visible = False


    # --- If time is up, reader may be startled --- #




    # --- Draw scene --- #
    bg.draw()
    pygame.draw.rect(w, (0, 255, 0), r)
    pson.draw()
    if visible:
        pygame.draw.circle(w, (255, 255, 255), (x, y), 25)




    # --- Finish --- #

    pygame.display.flip()
    c.tick(30)
ghost.center = (x,y)
if pygame.sprite.collide_rect(ghost, pson):
    pson.image = "PersonStartled.png"
bg.draw()
pygame.draw.rect(w, (0, 255, 0), r)
pson.draw()
ghost.draw()
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False


# Turn in your Coding Exercise.
