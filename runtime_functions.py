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
from utility_functions import * 
from cell_hero import *

def initialiseGame(width,height,stepDuration):

    window = grid_window(width,height)
    lat = lattice(width,height)
    MOVEEVENT = pygame.USEREVENT+1
    pygame.time.set_timer(MOVEEVENT,stepDuration)
    myfont = pygame.font.SysFont('DroidSansMono',30,bold=True) 

    return window, lat, MOVEEVENT, myfont

def initialisePlayerLists():

    zombieList = allZombies()
    motherList = allMothers()
    cellList = allCells()
    foodList = allFood()

    return zombieList, motherList, cellList, foodList

def placeStartingCells(lat,zombieList, motherList, cellList, foodList):

    heroCell = hero(lat,20,40)
    zombieList.addZombie(lat,12,14) 
    motherList.addMother(lat,6,5)
    cellList.addCell(lat,4,6)
    cellList.addCell(lat,6,8)
    cellList.addCell(lat,8,10)
    cellList.addCell(lat,10,20)
    cellList.addCell(lat,10,20)
    cellList.addCell(lat,10,20) 

    return heroCell

def initialUpdate(window,lat,cellList,zombieList,motherList,foodList):
    
    running_flag = True
    printStep = 0
    print_flag = 0
    shift = [0,0]
    space = False
    
    window.draw_background()
    lat.updateMaps(cellList,zombieList,motherList)
    cellList.updateCells(window.display,lat,foodList,cellList)
    zombieList.updateZombies(window.display,lat,cellList) 
    motherList.updateMothers(window.display,lat,foodList)
    foodList.updateFoods(window.display,lat)
    
    return running_flag, printStep, print_flag, shift, space

def eventHandler(running_flag, lat, window, cellList, zombieList, motherList, heroCell, foodList, space, event, shift, MOVEEVENT, print_flag):

    if event.type == pygame.QUIT:
        running_flag = 0
    elif event.type == MOVEEVENT: 
        killDying(lat,cellList)
        createChildren(lat,cellList) 
        zombieList.updateZombies(window.display,lat,cellList)
        cellList.updateCells(window.display,lat,foodList,cellList) 
        motherList.updateMothers(window.display,lat,foodList)
        heroCell.updateCell(lat,shift)
        lat.updateMaps(cellList,zombieList,motherList)
        shift = [0,0]
        if space:
            heroCell.dropFood(lat,foodList)
            space = False
        if cellList.numberOfCells() == 0 and motherList.numberOfCells() == 0 and zombieList.numberOfCells() == 0:
            running_flag = 0 
        print_flag = 1
    elif event.type == pygame.MOUSEBUTTONUP:
        placeFood(lat,foodList) 

    return running_flag, shift, space, print_flag

def printHandler(window, lat, cellList, zombieList, motherList, heroCell, foodList, printStep, print_flag, myfont, printStep_max):
    
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

    return printStep, print_flag
