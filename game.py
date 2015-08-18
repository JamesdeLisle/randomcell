#! /usr/bin/env python

import pygame
from lattice import *
from cell import *
from food import *
from numpy import abs
from players import *
from zombie import *
from drone import *
from mother import *
from grid_window import *
from lookcells import *    
    
pygame.init()

def main():
    
    width = 70
    height = 30
    stepDuration = 500
    window = grid_window(width,height)
    lat = lattice(width,height)
    MOVEEVENT = pygame.USEREVENT+1
    PRINTEVENT = pygame.USEREVENT+2
    pygame.time.set_timer(PRINTEVENT,1)
    pygame.time.set_timer(MOVEEVENT,stepDuration)
    myfont = pygame.font.SysFont('DroidSansMono',30,bold=True)   

    #############################################
    zombieList = allZombies()
    zombieList.addZombie(lat,12,14)
    motherList = allMothers()
    motherList.addMother(lat,6,5)
    cellList = allCells()
    cellList.addCell(lat,4,6)
    cellList.addCell(lat,6,8)
    #cellList.addCell(lat,8,10)
    #cellList.addCell(lat,10,20)
    #cellList.addCell(lat,10,20)
    #cellList.addCell(lat,10,20) 
    foodList = allFood()
    #foodList.addFood(lat,10,9)
    #############################################
    
    window.draw_background()
    running = 1
    lat.updateMaps(cellList,zombieList,motherList)
    cellList.updateCells(window.display,lat,foodList,cellList)
    zombieList.updateZombies(window.display,lat,cellList) 
    motherList.updateMothers(window.display,lat,foodList)
    foodList.updateFoods(window.display,lat)

    while running:
        
        event = pygame.event.poll()         

        if event.type == pygame.QUIT:
            running = 0
        elif event.type == MOVEEVENT:
            killDying(lat,cellList)
            createChildren(lat,cellList) 
            cellList.updateCells(window.display,lat,foodList,cellList)
            zombieList.updateZombies(window.display,lat,cellList) 
            motherList.updateMothers(window.display,lat,foodList)
            lat.updateMaps(cellList,zombieList,motherList) 
            if cellList.numberOfCells() == 0 and motherList.numberOfCells() == 0 and zombieList.numberOfCells() == 0:
                running = 0  
        elif event.type == PRINTEVENT:
            window.draw_background()
            drawQuantities(window.display,cellList,myfont)
            lat.colorWallMap(window.display) 
            lat.colorHeatMap(window.display)
            lat.colorSmellMap(window.display)
            cellList.printCells(window.display,lat)          
            zombieList.printZombies(window.display,lat)
            motherList.printMothers(window.display,lat)
            foodList.updateFoods(window.display,lat)

        elif event.type == pygame.MOUSEBUTTONUP:
            placeFood(lat,foodList) 
            
        pygame.display.update() 
    
main()
