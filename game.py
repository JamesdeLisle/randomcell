#! /usr/bin/env python

import pygame
from lattice import *
from cell import *
from food import *
from numpy import abs
from players import *
from cell_zombie import *
from grid_window import *
    
def main():
    width = 30
    height = 30
    # TODO only even numbers will work with levelgen
    window = grid_window(width, height)
    #window.create_window()
    lat = lattice(width, height)
    MOVEEVENT = pygame.USEREVENT+1
    DOUBLEMOVEEVENT = pygame.USEREVENT+1
    pygame.time.set_timer(DOUBLEMOVEEVENT,125)
    pygame.time.set_timer(MOVEEVENT,250)
    zombieList = allZombies()
    zombieList.addZombie(lat,12,14)
    cellList = allCells()
    cellList.addCell(lat,4,5)
    cellList.addCell(lat,15,20)
    cellList.addCell(lat,25,6)
    foodList = allFood()
    #foodList.addFood(lat,10,9)
    window.draw_background()
    running = 1

    while running:
        event = pygame.event.poll()
        
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == MOVEEVENT:
            window.draw_background()
            killDying(lat, cellList)
            createChildren(lat, cellList)
            lat.updateHeatMap(cellList)
            lat.colorHeatMap(window.display)
            lat.updateSmellMap()
            lat.colorSmellMap(window.display)
            zombieList.updateZombies(window.display, lat, cellList)
            cellList.updateCells(window.display, lat, foodList, cellList)
            foodList.updateFoods(window.display, lat)

            lat.colorWallMap(window.display)
        elif event.type == pygame.MOUSEBUTTONUP:
            placeFood(lat,foodList)
        
        pygame.display.update()

    pygame.quit()

main()
