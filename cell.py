import pygame
import numpy as np
from lookcells import *
from scipy import stats

class cell(object):

    def __init__(self,lattice,x,y):
        self.x = x
        self.y = y
        self.hunger = 0.0
    
    def whereMotives(self,lattice):
        
        thatDanger = 0.0
        thatDesire = 0.0
        dangerDirection = [0,0]
        desireDirection = [0,0]
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        
        for tik in range(len(adjCells[:])):
            xpos = adjCells[tik][0]
            ypos = adjCells[tik][1]
        
            if self.species == 'drone':
                thisDanger = lattice.emptyMap[xpos][ypos]
                thisDesire = lattice.smellMap[xpos][ypos]
            elif self.species == 'zombie':
                thisDanger = lattice.motherPherMap[xpos][ypos]
                thisDesire = lattice.heatMap[xpos][ypos]
            elif self.species == 'mother':
                thisDanger = lattice.emptyMap[xpos][ypos]
                thisDesire = lattice.heatMap[xpos][ypos] 

            if thisDanger > thatDanger:
                thatDanger = thisDanger
                dangerDirection[0] = adjCells[tik][0]
                dangerDirection[1] = adjCells[tik][1]
            
            if thisDesire > thatDesire:
                thatDesire = thisDesire
                desireDirection[0] = adjCells[tik][0]
                desireDirection[1] = adjCells[tik][1]

        return (dangerDirection,desireDirection)
 
    def weightWalk(self,lattice,motiveDirection):

        weightsDesire = []
        weightsDanger = []
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        nCells = len(adjCells[:])
        
        if self.species == 'drone':
            moveToDesire = 8.0
            moveAwayDanger = 1.0
            moveToOther = 1.0
            moveNowhere = 5.0
        elif self.species == 'zombie':
            moveToDesire = 10.0
            moveAwayDanger = 25.0
            moveToOther = 1.0
            moveNowhere = 5.0
        elif self.species == 'mother':
            moveToDesire = 12.0
            moveAwayDanger = 1.0
            moveToOther = 1.0
            moveNowhere = 5.0

        for tik in range(nCells):
            if adjCells[tik][0] == motiveDirection[1][0] and adjCells[tik][1] == motiveDirection[1][1]:
                weightsDesire.append(moveToDesire)
            else:
                weightsDesire.append(moveToOther)

            if adjCells[tik][0] == motiveDirection[0][0] and adjCells[tik][1] == motiveDirection[0][1]: 
                    weightsDanger.append(1.0/moveAwayDanger)
            else:
                weightsDanger.append(moveToOther)
         
        weightsDanger.append(moveNowhere * self.hunger)
        normDanger = sum(weightsDanger)
        weightsDesire.append(moveNowhere * self.hunger)
        normDesire = sum(weightsDesire) 
        weightsDanger = [ a/normDanger for a in weightsDanger ]
        weightsDesire = [ a/normDesire for a in weightsDesire ]
        weightsDanger = [ round(a,2) for a in weightsDanger ]
        weightsDesire = [ round(a,2) for a in weightsDesire ]
        weights = [ a*b for a,b in zip(weightsDanger,weightsDesire)]
        norm = sum(weights)
        weights = [ a/norm for a in weights]
        
        return weights  
    
    def generateNextPosition(self,lattice,weights):

        draw = [np.random.uniform(), np.random.uniform()]
        shift = [0,0]
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        cellNum = np.array([ x for x in range(len(adjCells[:])+1)])
        probs = np.array(weights)
        choice = discreteDraw(cellNum,probs)

        if choice == len(cellNum)-1:
            shift = [0,0]
        else:
            shift = [adjCells[int(choice)][2],adjCells[int(choice)][3]]

        return shift
   
    def updateCellMap(self,lattice,flag):
        if self.species == 'drone':
            lattice.cellMap[self.x][self.y] = flag
        elif self.species == 'zombie':
            lattice.zombieCellMap[self.x][self.y] = flag
        elif self.species == 'mother':
            lattice.motherMap[self.x][self.y] = flag

    def moveCell(self,lattice):
        
        motiveDirection = self.whereMotives(lattice)
        weights = self.weightWalk(lattice,motiveDirection) 
        shift = self.generateNextPosition(lattice,weights)
         
        self.updateCellMap(lattice,False)
        self.x = self.x + shift[0]
        self.y = self.y + shift[1]
        self.updateCellMap(lattice,True)
        minLx = 0
        minLy = 0
        maxLy = lattice.width
        maxLx = lattice.height
        self.x = wrapBoundaries(minLx,self.x,maxLx)
        self.y = wrapBoundaries(minLy,self.y,maxLy)
        
    
 
