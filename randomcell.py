#! /usr/bin/env python

import pygame
from utilityFunctions import * 
from runtime_functions import *

pygame.init()

def main():
    
    width = 70
    height = 30
    stepDuration = 300
    printStep_max = 10

    window, lat, MOVEEVENT, myfont = initialiseGame(width, height, stepDuration)
    zombieList, motherList, cellList, foodList = initialisePlayerLists()
    heroCell = placeStartingCells(lat, zombieList, motherList, cellList, foodList) 
    running_flag, printStep, print_flag, shift, space = initialUpdate(window, lat, cellList, zombieList, motherList, foodList)

    while running_flag:
        
        event = pygame.event.poll()  
        key = pygame.key.get_pressed()

        shift,space = detectInput(key,shift,space)
         
        running_flag, shift, space, print_flag = eventHandler(running_flag, lat, \
                window, cellList, zombieList, motherList, heroCell, foodList, \
                space, event, shift, MOVEEVENT, print_flag)

        printStep, print_flag = printHandler(window, lat, cellList, zombieList, motherList, heroCell, foodList, printStep, print_flag, myfont, printStep_max)

        pygame.display.update() 
    
main()
