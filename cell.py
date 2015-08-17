import pygame
import numpy as np
from lookcells import *
from scipy import stats

<<<<<<< HEAD
class cell:
=======
class cell(object):
>>>>>>> newfeatures

    def __init__(self,lattice,x,y):
        self.x = x
        self.y = y
<<<<<<< HEAD
        lattice.cellMap[x][y] = True
        self.hunger = 0.0
        self.birthometer = 0
        self.deathsdoor = 0.0
        
    def eatFood(self,lattice,foodList):
        
        if lattice.foodMap[self.x][self.y]:
            self.hunger = 0.0
            lattice.foodMap[self.x][self.y] = False
            for tik in range(len(foodList.foodList)):
                if foodList.foodList[tik].x == self.x and foodList.foodList[tik].y == self.y:
                    foodList.foodList.pop(tik)
                    break
    
    def whereSmell(self,lattice):
        
        thatSmell = 0.0
        smellDirection = [0,0]
=======
        self.hunger = 0.0
    
    def whereMotives(self,lattice):
        
        thatDanger = 0.0
        thatDesire = 0.0
        dangerDirection = [0,0]
        desireDirection = [0,0]
>>>>>>> newfeatures
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        
        for tik in range(len(adjCells[:])):
            xpos = adjCells[tik][0]
            ypos = adjCells[tik][1]
<<<<<<< HEAD
            if lattice.smellMap[xpos][ypos] > thatSmell:
                thatSmell = lattice.smellMap[xpos][ypos]
                smellDirection[0] = adjCells[tik][0]
                smellDirection[1] = adjCells[tik][1]

        return smellDirection

    def weightWalk(self,lattice,smellDirection):

        weights = []
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        nCells = len(adjCells[:])
        for tik in range(nCells):
            if adjCells[tik][0] == smellDirection[0] and adjCells[tik][1] == smellDirection[1]:
                weights.append(8.0)
            else:
                weights.append(1.0)

        weights.append(20.0 * self.hunger)
        norm = sum(weights)
        for tik in range(len(weights)):
            weights[tik] = weights[tik]/norm

        return weights

=======
        
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
    
>>>>>>> newfeatures
    def generateNextPosition(self,lattice,weights):

        draw = [np.random.uniform(), np.random.uniform()]
        shift = [0,0]
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        cellNum = np.array([ x for x in range(len(adjCells[:])+1)])
        probs = np.array(weights)
        choice = discreteDraw(cellNum,probs)
<<<<<<< HEAD
=======

>>>>>>> newfeatures
        if choice == len(cellNum)-1:
            shift = [0,0]
        else:
            shift = [adjCells[int(choice)][2],adjCells[int(choice)][3]]

        return shift
<<<<<<< HEAD
 
    def moveCell(self,lattice):
        
        smellDirection = self.whereSmell(lattice)
        weights = self.weightWalk(lattice,smellDirection) 
        shift = self.generateNextPosition(lattice,weights)

        lattice.cellMap[self.x][self.y] = False
        self.x = self.x + shift[0]
        self.y = self.y + shift[1]
        
        minL = 0
        maxL = len(lattice.points[0])-1
        if self.x > maxL:
            self.x = minL
        elif self.x < minL:
            self.x = maxL
        if self.y > maxL:
            self.y = minL
        elif self.y < minL:
            self.y = maxL
    
    def updateCellMap(self,lattice):
        lattice.cellMap[self.x][self.y] = True
            
    def updateCell(self,lattice,foodList,cellList):
       
        self.eatFood(lattice,foodList)
        self.moveCell(lattice)
        self.updateCellMap(lattice) 
        self.hunger = self.hunger + 0.01
        self.birthometer = self.birthometer - 1
        if self.birthometer < 1:
            self.birthometer = 0
        if self.hunger > 1.0:
            self.deathsdoor = self.deathsdoor + 0.1

    def printCell(self,screen,lattice):
        green = round((1-self.hunger)*255) 
        blue = round(self.hunger*255)
        if green < 0:
            green = 0
        elif green > 255:
            green = 255
        if blue < 0:
            blue = 0
        elif blue> 255:
            blue = 255
        pygame.draw.circle(screen,(0,green,blue),(lattice.points[self.x][self.y].location[0],lattice.points[self.x][self.y].location[1]),10)


=======
   
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
        
    
 
>>>>>>> newfeatures
