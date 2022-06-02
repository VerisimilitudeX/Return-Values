#### ---- LIBRARIES ---- ####
import tsk
import random
import pygame
pygame.init()

#### --------------------- ####
#### ---- PLAYER WINS ---- ####
#### --------------------- ####
def player_wins(sprite1, sprite2):
    if p == "FireMonster.png" and e == "GrassMonster.png":
        win = True
    elif p == "GrassMonster.png" and e == "StoneMonster.png":
        win = True
    elif p == "StoneMonster.png" and e == "ElectricMonster.png":
        win = True
    elif p == "ElectricMonster.png" and e == "WaterMonster.png":
        win = True
    elif p == "WaterMonster.png" and e == "FireMonster.png":
        win = True

#### --------------------------- ####
#### ---- GET_MONSTER_IMAGE ---- ####
#### --------------------------- ####
def get_monster_image(key):
    if key == -1:
        player.image = monsters[random.randint(0, len(monsters) - 1)]
    elif key == pygame.K_a:
        player.image = monsters[0]
    elif key == pygame.K_s:
        player.image = monsters[1]
    elif key == pygame.K_d:
        player.image = monsters[2]
    elif key == pygame.K_f:
        player.image = monsters[3]
    elif key == pygame.K_v:
        player.image = monsters[4]
    else:
        player.image = "Blank.png"

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# --- Setup --- #
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# --- Sprites --- #                                     
monsters = ["FireMonster.png", "GrassMonster.png", "StoneMonster.png", "ElectricMonster.png", "WaterMonster.png"]
background = tsk.Sprite("Arena.jpg", 0, 0)
player = tsk.Sprite("Blank.png", 150, 200)
enemy = tsk.Sprite("Blank.png", 700, 200)

#### ---- RE-STRUCTURE 2 ---- ####

# Assign the enemy's image using the get_monster_image
# function
enemy.image = get_monster_image(tsk.is_key_pressed)

#### ---- END RESTRUCTURE 2 ---- ####

enemy.flip_x = True

# --- Variables --- #
countdown = 3000
misses = 0
hits = 0
timer_bar = pygame.Rect(0, 550, 1018, 50)
move_increment = 1018 / countdown

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:
#########################
    #### ---- EVENT LOOP ---- ####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # --- Put up monster when user presses key --- #
        if event.type == pygame.KEYDOWN:

            #### ---- RE-STRUCTURE 1 ---- ####
######################
            # Use the code below to write the function
            # get_monster_image that takes a key value
            # and returns the matching image from the
            # monsters list. Use it here to assign the
            # player's monster image.
######################
            key = event.key
            get_monster_image(key)
#
            #### ---- END RESTRUCTURE 1 ---- ####
#
    # --- Timer bar moves left --- #
    speed = move_increment * c.get_time()
    timer_bar.x -= int(speed)
#
    # --- When timer runs down, compare monsters --- #
    if countdown <= 0:
#
        #### ---- RE-STRUCTURE 4 ---- ####
#
        # Use the code below to create a function
        # called player_wins that takes two sprites and
        # returns a boolean. Call the function here.
        p = player.image
        e = enemy.image
        win = False
        player_wins(p, e)
#
        #### ---- END RESTRUCTURE 4 ---- ####
#
        if win:
            hits += 1
        else:
            misses += 1
#
        #### ---- RE-STRUCTURE 3 ---- ####
#
        # Use the get_monster_image function to assign
        # the enemy's image
        enemy.image = get_monster_image()
#
    #    #### ---- END RESTRUCTURE 3 ---- ####
#
        countdown = 2000
        timer_bar.x = 0
#
#
    #### ---- DRAW ---- ####
#
    # --- Scene --- #
    background.draw()
    player.draw()
    enemy.draw()
#
    # --- Interface --- #
    for i in range(hits):
        pygame.draw.circle(w, (0, 0, 255), (100 + i * 50, 50), 20)
#
    for i in range(misses):
        pygame.draw.circle(w, (255, 0, 0), (600 + i * 50, 50), 20)
#
    pygame.draw.rect(w, (0, 255, 0), timer_bar)
#
    # --- Finish --- #
    countdown -= c.get_time()
    pygame.display.flip()
    c.tick(30)
#
    # --- Scores --- #
    if hits >= 5 or misses >= 5:
        drawing = False
        print("FINAL SCORE")
        print("---------------")
        print("Wins: " + str(hits))
        print("Losses: " + str(misses))
#
#
# Turn in your Coding Exercise.
#