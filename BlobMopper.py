"""
LESSON: Unit 6 Quiz
EXERCISE: Blob Mopper
"""

#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()


#### ----------------------------- ####
#### ---- MAKE SPLAT FUNCTION ---- ####
#### ----------------------------- ####

# Create a function to make splats that takes a
# location to place the splat as a parameter
def make_splat(locationx, locationy):

    # Create a list of filenames that the splat can use
    # and randomly choose one. Use the following images:
    # SplatDarkYellow.png, SplatGreen.png,
    # SplatPurple.png, and SplatYellow.png
    filenames = ["SplatDarkYellow.png", "SplatGreen.png", "SplatPurple.png", "SplatYellow.png"]
    randomfilename = filenames[random.randint(0, len(filenames) - 1)]

    # Create a splat with the randomly-chosen image,
    # place its center at the given location, and set
    # its scale to 30%
    splat = tsk.Sprite(randomfilename, locationx, locationy)
    splat.scale = 0.3

    # Return the new splat
    # ---> TEST AFTER THIS LINE <--- #
    return splat

#### ------------------------------- ####
#### ---- CLEAN SPLATS FUNCTION ---- ####
#### ------------------------------- ####

# Create a function that takes a list of sprites and
# decides which ones should be removed
def clean_splats(spritelist):

    # Make an empty list to store the marked sprites
    marked_sprites = []

    # Get the mouse position, and check each splat in
    # the parameter list
    x, y = pygame.mouse.get_pos()
    for splat in spritelist:

        # If the mouse and splat collide, add it to
        # the list of marked sprites
        if splat.rect.collidepoint(x, y):
            marked_sprites.append(splat)

    # Return the list of marked sprites
    # ---> TEST AFTER THIS LINE <--- #
    return marked_sprites

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

#### ---- SETUP ---- ####
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Create an empty list for splats and a timer for how
# long before each new one appears
splats = []
timer = 3

# Create sprites for the background (ScienceLab.jpg)
# and the blob (Blob.jpg), where the blob starts at a
# random height on the floor
background = tsk.Sprite("ScienceLab.jpg", 0, 0)
blob = tsk.Sprite("Blob.jpg", 0, random.randint(1, 573))

# Create speed variables for the blob's horizontal and
# vertical movement
hspeed = 3
vspeed = 3

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    #### ---- UPDATE SPRITES ---- ####

    # --- Update blob position --- #

    # Move the blob based on its two speeds and
    # c.get_time()
    blob.center_x += hspeed * c.get_time()
    blob.center_y += vspeed * c.get_time()

    # If the blob has hit the sides of the screen, face
    # it the other way and reverse its horizontal speed
    if blob.center_x == 1018 or blob.center_x == 0:
        blob.flip_x = True
        hspeed = -hspeed

    # If the blob has hit the bottom of the screen or
    # the top of the floor, reverse its vertical speed
    # ---> TEST AFTER THIS LINE <--- #
    if blob.center_y == 0 or blob.center_y == 573:
        blob.flip_y = True
        vspeed = -vspeed

    # --- Make new splats --- #

    # If the timer ran out, call the function to make
    # a new splat at the blob's center position
    if timer == 0:
        make_splat(blob.center_x, blob.center_y)

        # Put the new splat in the list of splats and
        # re-set the timer
        # ---> TEST AFTER THIS LINE <--- #
        splats.append(splat)
        timer = 3

    # --- Get rid of colliding splats --- #

    # Call the function to mark splats to remove using
    # the list of all splats
    clean_splats(splats)

    # Go through the returned list and remove each of
    # those splats from the list of all splats
    # ---> TEST AFTER THIS LINE <--- #
    for splat in marked_sprites:
        splats.remove(splat)

    #### ---- DRAW FRAME ---- ####

    # --- Sprites --- #

    # Draw the background, all the splats in the
    # current list, and the blob
    background.draw()
    for splat in splats:
        splat.draw()
    blob.draw()
    
    # --- Finish --- #
    pygame.display.flip()
    c.tick(30)

    # Track time with the timer
    # ---> TEST AFTER THIS LINE <--- #
    timer -= c.get_time()

# Turn in your Coding Exercise.
