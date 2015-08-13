#! /usr/bin/env python

import pygame
from lattice import *
from cell import *
from food import *
from numpy import abs
from players import *
from cell_zombie import *

screen = pygame.display.set_mode((800,800))

def drawGrid():
    for tik in range(0,31):
        pygame.draw.line(screen,(0,0,255),(100+(tik*20),100),(100+(tik*20),700))
        pygame.draw.line(screen,(0,0,255),(100,100+(tik*20)),(700,100+(tik*20)))

def drawBackground():
    screen.fill((255,255,255))
    drawGrid()
    
def main():

    lat = lattice()
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
    drawBackground()
    running = 1

    while running:
        event = pygame.event.poll()
        
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == MOVEEVENT:
            drawBackground()
            killDying(lat,cellList)
            createChildren(lat,cellList) 
            lat.updateHeatMap(cellList)
            lat.colorHeatMap(screen)
            lat.updateSmellMap()
            lat.colorSmellMap(screen)
            zombieList.updateZombies(screen,lat,cellList)
            cellList.updateCells(screen,lat,foodList,cellList)
            foodList.updateFoods(screen,lat)

            lat.colorWallMap(screen)
        elif event.type == pygame.MOUSEBUTTONUP:
            placeFood(lat,foodList)
        
        pygame.display.update()

main()
