# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:13:52 2021

@author: Lenovo-PC
"""

# import pygame module in this program
import pygame;
import animate;

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((600, 600))

# set the pygame window name
pygame.display.set_caption("Moving rectangle")

# object current co-ordinates
x = 200
y = 200
a=100
b=100
# dimensions of the object
width = 20
height = 20

# velocity / speed of movement
vel = 10
animate.resetStateToInitialConditions()
x = animate.state["positions"][0]["x"]
print(animate.state["positions"][0]["x"])
print(x)
y = animate.state["positions"][0]["y"]
a=animate.state["positions"][1]["x"]
b=animate.state["positions"][1]["y"]
# Indicates pygame is running
run = True

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)
    
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            
            # it will make exit the while loop
            run = False
    # stores keys pressed
    
        
            
    # completely fill the surface object
    # with black colour
    win.fill((0, 0, 0))
   
    # drawing object on screen which is rectangle here

  
    
    
   
   
  
    # it refreshes the window
    animate.updatePosition() 
    print(animate.state["positions"][0]["x"])
    pygame.draw.circle(win, (204, 255, 255), animate.coord(a,b), 15)
    pygame.draw.circle(win, (255,255,255), animate.coord(x,y), 15)
    pygame.display.update()
    print(animate.coord(a,b))
    print(animate.coord(x,y))
   

# closes the pygame window
pygame.quit()
