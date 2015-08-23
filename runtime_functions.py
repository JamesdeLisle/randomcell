import pygame
from lattice import *
from cell import *
from food import *
from numpy import abs
from players import *
from cell_zombie import *
from cell_drone import *
from cell_mother import *
from window import *
from utility_functions import * 
from cell_hero import *
from lattice_containers import *

def initialiseGame(width,height,stepDuration):

    window = grid_window(width,height)
    actorLattices = actorLattice(width,height)
    fluidLattices = fluidLattice(width,height)

    MOVEEVENT = pygame.USEREVENT+1
    pygame.time.set_timer(MOVEEVENT,stepDuration)
    myfont = pygame.font.SysFont('DroidSansMono',30,bold=True) 

    return window, actorLattices, fluidLattices, MOVEEVENT, myfont

def initialisePlayerLists():

    zombieList = allZombies()
    motherList = allMothers()
    droneList = allDrones()
    foodList = allFood()

    return zombieList, motherList, droneList, foodList

def placeStartingCells(actorLattices,zombieList, motherList, droneList, foodList):

    heroCell = hero(actorLattices,20,40)
    zombieList.addCell(actorLattices,12,14) 
    motherList.addCell(actorLattices,6,5)
    droneList.addCell(actorLattices,4,6)
    droneList.addCell(actorLattices,6,8)
    droneList.addCell(actorLattices,8,10)
    droneList.addCell(actorLattices,10,20)
    droneList.addCell(actorLattices,10,20)
    droneList.addCell(actorLattices,10,20) 

    return heroCell

def initialUpdate(window,fluidLattices,actorLattices,droneList,zombieList,motherList,foodList):
    
    running_flag = True
    printStep = 0
    print_flag = 0
    shift = [0,0]
    space = False
    
    window.draw_background()

    fluidLattices.heat.updateMap(fluidLattices.wall,[droneList])
    fluidLattices.smell.updateMap(fluidLattices.wall,[foodList])
    fluidLattices.zombiePheremone.updateMap(fluidLattices.wall,[zombieList])
    fluidLattices.motherPheremone.updateMap(fluidLattices.wall,[motherList])
    
    droneList.updateCells(fluidLattices,actorLattices,foodList)
    zombieList.updateCells(fluidLattices, actorLattices, droneList) 
    motherList.updateCells(fluidLattices,actorLattices,foodList)
    
    return running_flag, printStep, print_flag, shift, space

def eventHandler(running_flag, fluidLattices, actorLattices, window, droneList, zombieList, motherList, heroCell, foodList, space, event, shift, MOVEEVENT, print_flag):

    if event.type == pygame.QUIT:
        running_flag = 0
    elif event.type == MOVEEVENT: 
        createChildren(actorLattices,droneList)
        killDying(actorLattices,droneList) 
        droneList.updateCells(fluidLattices,actorLattices,foodList)
        zombieList.updateCells(fluidLattices, actorLattices, droneList) 
        motherList.updateCells(fluidLattices,actorLattices,foodList)
        heroCell.updateCell(fluidLattices, actorLattices, shift)
        fluidLattices.heat.updateMap(fluidLattices.wall,[droneList])
        fluidLattices.smell.updateMap(fluidLattices.wall,[foodList])
        fluidLattices.zombiePheremone.updateMap(fluidLattices.wall,[zombieList])
        fluidLattices.motherPheremone.updateMap(fluidLattices.wall,[motherList]) 
        shift = [0,0]
        if space:
            heroCell.dropFood(actorLattices,foodList)
            space = False
        if droneList.numberOfCells() == 0:
            running_flag = 0 
        print_flag = 1
    elif event.type == pygame.MOUSEBUTTONUP:
        placeFood(fluidLattices,actorLattices,foodList)

    return running_flag, shift, space, print_flag

def printHandler(window, fluidLattices, actorLattices, droneList, zombieList, motherList, heroCell, foodList, printStep, print_flag, myfont, printStep_max):
    
    if print_flag:
        window.draw_background()
        drawQuantities(window.display,droneList,myfont)
        fluidLattices.wall.colorMap(window.display) 
        fluidLattices.heat.colorMap(window.display,printStep,printStep_max)
        fluidLattices.smell.colorMap(window.display)
        droneList.printCells(window.display,actorLattices,printStep,printStep_max)          
        zombieList.printCells(window.display,actorLattices,printStep,printStep_max)
        motherList.printCells(window.display,actorLattices,printStep,printStep_max)
        heroCell.printCell(window.display,actorLattices,printStep,printStep_max)
        foodList.printCells(window.display,actorLattices)
        printStep += 1
   
        if printStep == printStep_max:
            print_flag = 0
            printStep = 0

    return printStep, print_flag



