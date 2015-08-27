#! /usr/bin/env python

import pygame
from utility_functions import * 
from runtime_functions import *

pygame.init()

def main():
    
    width = 70
    height = 30
    stepDuration = 1000
    printStep_max = 30

    window, actorLattices, fluidLattices, MOVEEVENT, myfont = initialiseGame(width, height, stepDuration)
    
    zombieList, motherList, droneList, foodList = initialisePlayerLists()
    
    heroCell = placeStartingCells(actorLattices,zombieList, motherList, droneList, foodList) 
    
    running_flag, printStep, print_flag, shift, space, wall, wallOrientation = initialUpdate(window,\
            fluidLattices,actorLattices,droneList,zombieList,motherList,foodList)

    while running_flag:
        
        event = pygame.event.poll()  
        key = pygame.key.get_pressed()

        shift,space,wall,wallOrientation = detectInput(key,shift,space,wall,wallOrientation)
         
        running_flag, shift, space, print_flag,wall = eventHandler(running_flag,\
                fluidLattices, actorLattices, window, droneList, zombieList,\
                motherList, heroCell, foodList, space, event, shift, MOVEEVENT,\
                print_flag,wall, wallOrientation)

        printStep, print_flag = printHandler(window, fluidLattices, actorLattices,\
                droneList, zombieList, motherList, heroCell, foodList, printStep,\
                print_flag, myfont, printStep_max)

        pygame.display.update() 
    
main()
