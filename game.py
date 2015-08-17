#! /usr/bin/env python

import pygame
from lattice import *
from cell import *
from food import *
from numpy import abs
from players import *
<<<<<<< HEAD
from cell_zombie import *
from grid_window import *
    
def main():
    width = 30
    height = 30
    # TODO only even numbers will work with levelgen
    window = grid_window(width, height)
    #window.create_window()
    lat = lattice(width, height)
=======
from zombie import *
from drone import *
from mother import *
from grid_window import *
    
def main():
    
    width = 70
    height = 30
    window = grid_window(width,height)
    lat = lattice(width,height)
>>>>>>> newfeatures
    MOVEEVENT = pygame.USEREVENT+1
    DOUBLEMOVEEVENT = pygame.USEREVENT+1
    pygame.time.set_timer(DOUBLEMOVEEVENT,125)
    pygame.time.set_timer(MOVEEVENT,250)
<<<<<<< HEAD
    zombieList = allZombies()
    zombieList.addZombie(lat,12,14)
    cellList = allCells()
    cellList.addCell(lat,4,5)
    cellList.addCell(lat,15,20)
    cellList.addCell(lat,25,6)
    foodList = allFood()
    #foodList.addFood(lat,10,9)
=======
    #############################################
    zombieList = allZombies()
    zombieList.addZombie(lat,12,14)
    motherList = allMothers()
    motherList.addMother(lat,6,5)
    cellList = allCells()
    #cellList.addCell(lat,4,50)
    #cellList.addCell(lat,6,57)
    cellList.addCell(lat,8,62)
    foodList = allFood()
    #foodList.addFood(lat,10,9)
    #############################################
>>>>>>> newfeatures
    window.draw_background()
    running = 1

    while running:
        event = pygame.event.poll()
        
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == MOVEEVENT:
            window.draw_background()
<<<<<<< HEAD
            killDying(lat, cellList)
            createChildren(lat, cellList)
=======
            killDying(lat,cellList)
            createChildren(lat,cellList) 
>>>>>>> newfeatures
            lat.updateHeatMap(cellList)
            lat.colorHeatMap(window.display)
            lat.updateSmellMap()
            lat.colorSmellMap(window.display)
<<<<<<< HEAD
            zombieList.updateZombies(window.display, lat, cellList)
            cellList.updateCells(window.display, lat, foodList, cellList)
            foodList.updateFoods(window.display, lat)
            lat.colorWallMap(window.display)

            if cellList.numberOfCells() == 0:
                running = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            placeFood(lat,foodList)
        
        pygame.display.update()

    pygame.quit()
=======
            lat.updateMotherPherMap(motherList)
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
>>>>>>> newfeatures

main()
