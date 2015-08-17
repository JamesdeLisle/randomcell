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
    
def main():
    
    width = 70
    height = 30
    window = grid_window(width,height)
    lat = lattice(width,height)
    MOVEEVENT = pygame.USEREVENT+1
    DOUBLEMOVEEVENT = pygame.USEREVENT+1
    pygame.time.set_timer(DOUBLEMOVEEVENT,125)
    pygame.time.set_timer(MOVEEVENT,250)
    #############################################
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
    #foodList.addFood(lat,10,9)
    #############################################
    window.draw_background()
    running = 1

    while running:
        event = pygame.event.poll()
        
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == MOVEEVENT:
            window.draw_background()
            killDying(lat,cellList)
            createChildren(lat,cellList) 
            lat.updateHeatMap(cellList)
            lat.colorHeatMap(window.display)
            lat.updateSmellMap()
            lat.colorSmellMap(window.display)
            lat.updateMotherPherMap(motherList)
            lat.updateZombiePherMap(zombieList)
            zombieList.updateZombies(window.display,lat,cellList)
            cellList.updateCells(window.display,lat,foodList,cellList)
            motherList.updateMothers(window.display,lat,foodList)
            foodList.updateFoods(window.display,lat)

            lat.colorWallMap(window.display)

            if cellList.numberOfCells() == 0 and motherList.numberOfCells() == 0 and zombieList.numberOfCells() == 0:
                running = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            placeFood(lat,foodList) 

        pygame.display.update()

main()
