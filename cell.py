import pygame
import numpy as np
from utilityFunctions import *
from scipy import stats

class cell(object):

    def __init__(self,lattice,x,y):
        self.x = x
        self.y = y
        self.previous_x = 0
        self.previous_y = 0
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
                thisDanger = lattice.zombiePherMap[xpos][ypos]
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
        
        for tik in range(nCells):
            if adjCells[tik][0] == motiveDirection[1][0] and adjCells[tik][1] == motiveDirection[1][1]:
                weightsDesire.append(self.moveToDesire)
            else:
                weightsDesire.append(self.moveToOther)

            if adjCells[tik][0] == motiveDirection[0][0] and adjCells[tik][1] == motiveDirection[0][1]: 
                    weightsDanger.append(1.0/self.moveAwayDanger)
            else:
                weightsDanger.append(self.moveToOther)
         
        weightsDanger.append(self.moveNowhere * self.hunger)
        normDanger = sum(weightsDanger)
        weightsDesire.append(self.moveNowhere * self.hunger)
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
        elif self.species == 'hero':
            lattice.heroMap[self.x][self.y] = flag

    def moveCell(self,lattice):
        
        motiveDirection = self.whereMotives(lattice)
        weights = self.weightWalk(lattice,motiveDirection) 
        shift = self.generateNextPosition(lattice,weights)
 
        self.updateCellMap(lattice,False)
        self.previous_x = self.x
        self.previous_y = self.y
        self.x = self.x + shift[0]
        self.y = self.y + shift[1]
        self.updateCellMap(lattice,True)
        minLx = 0
        minLy = 0
        maxLy = lattice.width
        maxLx = lattice.height
        self.x = wrapBoundaries(minLx,self.x,maxLx)
        self.y = wrapBoundaries(minLy,self.y,maxLy)

    def generateAnimationVectors(self,lattice,printStep_max):
        
        xpos = lattice.points[self.x][self.y].location[0]
        ypos = lattice.points[self.x][self.y].location[1]
        xmin = lattice.points[self.previous_x][self.previous_y].location[0]
        xmax = lattice.points[self.x][self.y].location[0]
        ymin = lattice.points[self.previous_x][self.previous_y].location[1]
        ymax = lattice.points[self.x][self.y].location[1]
        xVec = np.linspace(xmin,xmax,printStep_max).tolist()
        yVec = np.linspace(ymin,ymax,printStep_max).tolist()
        xVec = [ int(round(x)) for x in xVec ]
        yVec = [ int(round(x)) for x in yVec ]

        return xVec,yVec
        
    
 
