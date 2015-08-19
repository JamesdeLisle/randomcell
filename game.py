#! /usr/bin/env python

import pygame
from lattice import *
from cell import *
from food import *
from numpy import abs
from players import *
from cell_zombie import *
from cell_drone import *
from cell_mother import *
from grid_window import *
from utilityFunctions import *    
from cell_hero import *

pygame.init()

def main():
    
    width = 70
    height = 30
    stepDuration = 400
    window = grid_window(width,height)
    lat = lattice(width,height)
    MOVEEVENT = pygame.USEREVENT+1
    pygame.time.set_timer(MOVEEVENT,stepDuration)
    myfont = pygame.font.SysFont('DroidSansMono',30,bold=True)   

    #############################################
    heroCell = hero(lat,20,40)
    zombieList = allZombies()
    zombieList.addZombie(lat,12,14)
    motherList = allMothers()
    motherList.addMother(lat,6,5)
    cellList = allCells()
    cellList.addCell(lat,4,6)
    cellList.addCell(lat,6,8)
    cellList.addCell(lat,8,10)
    cellList.addCell(lat,10,20)
    cellList.addCell(lat,10,20)
    cellList.addCell(lat,10,20) 
    foodList = allFood()
    #############################################
    
    window.draw_background()
    running = 1
    lat.updateMaps(cellList,zombieList,motherList)
    cellList.updateCells(window.display,lat,foodList,cellList)
    zombieList.updateZombies(window.display,lat,cellList) 
    motherList.updateMothers(window.display,lat,foodList)
    foodList.updateFoods(window.display,lat)
    printStep = 0
    print_flag = 0
    printStep_max = 10
    shift = [0,0]
    
    while running:
        
        event = pygame.event.poll() 
        
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == MOVEEVENT:
            killDying(lat,cellList)
            createChildren(lat,cellList) 
            zombieList.updateZombies(window.display,lat,cellList)
            cellList.updateCells(window.display,lat,foodList,cellList) 
            motherList.updateMothers(window.display,lat,foodList)
            heroCell.updateCell(lat,shift)
            lat.updateMaps(cellList,zombieList,motherList)
            if cellList.numberOfCells() == 0 and motherList.numberOfCells() == 0 and zombieList.numberOfCells() == 0:
                running = 0 
            print_flag = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            placeFood(lat,foodList) 

        if print_flag:
            window.draw_background()
            drawQuantities(window.display,cellList,myfont)
            ############################################
            # Color Maps
            lat.colorWallMap(window.display) 
            lat.colorHeatMap(window.display,printStep,printStep_max)
            lat.colorSmellMap(window.display)
            ############################################
            # Color cell movement
            cellList.printCells(window.display,lat,printStep,printStep_max)          
            zombieList.printZombies(window.display,lat,printStep,printStep_max)
            motherList.printMothers(window.display,lat,printStep,printStep_max)
            heroCell.printCell(window.display,lat,printStep,printStep_max)
            ############################################
            foodList.updateFoods(window.display,lat)
            printStep += 1
       
            if printStep == printStep_max:
                print_flag = 0
                printStep = 0
         
        pygame.display.update() 
    
main()
