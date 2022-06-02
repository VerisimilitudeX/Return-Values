"""
LESSON: 6.2 - Return Values
WARMUP 4
"""

import pygame
pygame.init()

#### ----------------------------- ####
#### ---- GET POINTS FUNCTION ---- ####
#### ----------------------------- ####
def get_points(center):
    x, y = center

    # Return a list of coordinate tuples for points 30
    # pixels above, below, left, and right of this point
    return [(x, y + 30), (x, y - 30), (x + 30, y), (x - 30, y)]

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([500, 500])
w.fill((100, 230, 100))

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            centers = get_points((x, y))

            if centers != None:
                for circle in centers:
                    pygame.draw.circle(w, (255, 100, 255), circle, 25)
            pygame.draw.circle(w, (255, 255, 100), (x, y), 20)

    pygame.display.flip()