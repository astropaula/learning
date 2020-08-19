import pygame, sys, time, random
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Pastel Balls Animation')

# Set up direction variables.
DOWN = 'down'
UP = 'up'

MOVESPEED = 6

# Set up the colors.
YELLOW = (255, 255, 230)
WHITE = (255, 255, 255)
COLOR1 = (153, 102, 255)
COLOR2 = (255, 230, 255)
COLOR3 = (204, 230, 255)
COLOR4 = (255, 204, 255)
COLOR5 = (179, 198, 255)
COLOR6 = (179, 255, 230)
COLOR7 = (255, 204, 204)
COLOR8 = (194, 240, 194)

# Set up the box data structure.
b1 = {'cir':[400, 80],'rad':75, 'color':COLOR1, 'dir':UP}
b2 = {'cir':[200, 150], 'rad':25, 'color':COLOR2, 'dir':DOWN}
b3 = {'cir':[500, 200],'rad': 30, 'color':COLOR3, 'dir':UP}
b4 = {'cir':[50, 300],'rad': 45, 'color':COLOR4, 'dir':DOWN}
b5 = {'cir':[800, 45],'rad': 40, 'color':COLOR5, 'dir':UP}
b6 = {'cir':[250, 60],'rad': 30, 'color':COLOR6, 'dir':DOWN}
b7 = {'cir':[620, 0],'rad': 15, 'color':COLOR7, 'dir':UP}
b8 = {'cir':[900, 320],'rad': 50, 'color':COLOR8, 'dir':DOWN}
b9 = {'cir':[80, 20],'rad':55, 'color':COLOR5, 'dir':UP}
b9 = {'cir':[700, 80],'rad':60, 'color':COLOR3, 'dir':DOWN}
boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

# Run the game loop.
while True:
    # Check for the quit event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)
    #MOVESPEED = random.randint(0,10)
    for b in boxes:
        # Move the box data structure.
        if b['dir'] == UP:
            b['cir'][1] -= random.randint(4, 10)
        if b['dir'] == DOWN:
            b['cir'][1] += random.randint(4, 10)
        
        
        # Check whether the box has moved out of the window.
        if (b['cir'][1] - b['rad']) < 0:
            # The box moved past the top.
            b['dir'] = DOWN
            #print(b['dir'])
        
        if (b['cir'][1] + b['rad']) > WINDOWHEIGHT:
            # The box has moved past the bottom.
            b['dir'] = UP
        

        
        pygame.draw.circle(windowSurface, b['color'], b['cir'],b['rad'],0)
    
    pygame.display.update()
    time.sleep(0.02)

