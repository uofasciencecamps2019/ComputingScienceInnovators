

# -*- coding: utf-8 -*-




#import modules

import pygame

import random

import time



#def collision_with_boundaries(snake_head):

    # if snake is outside of boundaries return 1

#def generate_snake(snake_head, snake_position, button_direction):

    #uses button_direction to decide where snake head will go


#def display_snake(snake_position):

    #uses list of snake's positions to display snake

#def play_game(snake_head, snake_position, button_direction):

    #crashed = False
    
    #while crashed is not True:

        #for event in pygame.event.get():

            #ends game if you click on X

            #sets variable used to move snake using arrow keys


        #moves snake position

        

        #display background and snake

        

        #ends game loop if snake leaves the boundary


        #clock.tick(20)



if __name__ == "__main__":

    # set variables

    display_width = 500

    display_height = 500

    player_color = (255,0,0)

    window_color = (200,200,200)

    clock=pygame.time.Clock()

    

    #create the snake

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250]]



    #initialize pygame modules    

    pygame.init()

    

    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game")

    pygame.display.update()

    

    #start the game loop

    #play_game(snake_head, snake_position, 1)



    pygame.quit()