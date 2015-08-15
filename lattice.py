import pygame
from lookcells import *
from levelgen import *


class latAttribute:

    def __init__(self,x,y):
        self.location = [110+(x*20),110+(y*20)]
         
def createWallMap(width,height):

    wallMap = [ [ False for x in range(width)] for y in range(height)]
   
    level = 0
    if level == 0:
        wallMap = maze(width, height)
    elif level == 1:
        for tik1 in range(width):
            for tik2 in range(height):
                if tik1 % 2 == 0 and tik2 % 2 == 0:
                    wallMap[tik1][tik2] = True
    elif level == 2:
        for tik1 in range(width):
            for tik2 in range(height):
                if 10 <= tik1 <= 20 and 10 <= tik2 <= 20:
                    wallMap[tik1][tik2] = True
    elif level == 3:
        for tik1 in range(width):
            for tik2 in range(height):
                if 0 < tik1 < 15 and tik2 == 10:
                    wallMap[tik1][tik2] = True

    return wallMap

class lattice:
#TODO move each individual grid to its own class
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.points = [ [ latAttribute(x,y) for x in range(self.width)] for y in range(self.height)]
        self.wallMap = createWallMap(self.width,self.height)
        self.heatMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.cellMap = [ [ False for x in range(self.width)] for y in range(self.height)]
        self.foodMap = [ [ False for x in range(self.width)] for y in range(self.height)]
        self.smellMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.zombieCellMap = [ [ False for x in range(self.width)] for y in range(self.height)]

    def getwidth(self):
        return self.width

    def getheight(self):
        return self.height

    def colorWallMap(self,screen):

        for tik1 in range(self.width):
            for tik2 in range(self.height):
                xpos = self.points[tik1][tik2].location[0]-9
                ypos = self.points[tik1][tik2].location[1]-9
                squarewidth = 18
                squareheight = 18
                if self.wallMap[tik1][tik2]:
                    # TODO stop the lattice drawing directly on the screen
                    pygame.draw.rect(screen,(0,0,0),(xpos,ypos,squarewidth,squareheight))

    def updateHeatMap(self,cellList):

        tempMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        for tik1 in range(len(self.heatMap[0])):
            for tik2 in range(len(self.heatMap[0])):
                self.heatMap[tik1][tik2] = self.heatMap[tik1][tik2] * 0.95 
                if self.cellMap[tik1][tik2]:
                    for tik5 in range(len(cellList.celist)):
                        if cellList.celist[tik5].x == tik1 and cellList.celist[tik5].y == tik2:
                            self.heatMap[tik1][tik2] = (1 - cellList.celist[tik5].hunger) * 2.0

                adjCells = getAdjacent(self.wallMap,tik1,tik2)

                if len(adjCells) == 0:
                    pass
                else:
                    scale = 1.0/len(adjCells[:])
                    for tik3 in range(len(adjCells[:])):
                        xpos = adjCells[tik3][0]
                        ypos = adjCells[tik3][1]
                        tempMap[xpos][ypos] = tempMap[xpos][ypos] + self.heatMap[tik1][tik2] * scale
                        
        for tik1 in range(len(self.heatMap[0])):
            for tik2 in range(len(self.heatMap[0])):
                if tempMap[tik1][tik2] < 1e-2:
                    tempMap[tik1][tik2] = 0
        self.heatMap = tempMap
    
    def updateSmellMap(self):
        
        tempMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        for tik1 in range(self.width):
            for tik2 in range(self.height):
                if self.foodMap[tik1][tik2]:
                    tempMap[tik1][tik2] = 1.0
                tempMap[tik1][tik2] = tempMap[tik1][tik2] * 0.8 

                adjCells = getAdjacent(self.wallMap,tik1,tik2)
                if len(adjCells) == 0:
                    pass
                else:
                    scale = 1.0/len(adjCells[:])
                    
                    for tik3 in range(len(adjCells[:])):
                        xpos = adjCells[tik3][0]
                        ypos = adjCells[tik3][1]
                        tempMap[xpos][ypos] = tempMap[xpos][ypos] + self.smellMap[tik1][tik2] * scale 
                        
        self.smellMap = tempMap

    def colorSmellMap(self,screen):
        
        for tik1 in range(len(self.smellMap[0])):
            for tik2 in range(len(self.smellMap[0])):
                len(self.heatMap[0]) 
                
                cValue = round((1-self.smellMap[tik1][tik2])*255/1.5)
                
                if cValue > 255:
                    cValue = 255
                elif cValue < 0:
                    cValue = 0
                 
                xpos = self.points[tik1][tik2].location[0]
                ypos = self.points[tik1][tik2].location[1]
                if self.smellMap[tik1][tik2] > 1e-2 and cValue < 250:
                    # TODO stop the lattice drawing directly on the screen
                    pygame.draw.circle(screen,(cValue,255,cValue),(xpos,ypos),4)
                
     
    def colorHeatMap(self,screen):
        
        for tik1 in range(len(self.heatMap[0])):
            for tik2 in range(len(self.heatMap[0])):
                len(self.heatMap[0]) 
                cValue = round((1-self.heatMap[tik1][tik2])*255)
                if cValue > 255:
                    cValue = 255
                elif cValue < 0:
                    cValue = 0
                xpos = self.points[tik1][tik2].location[0]-9
                ypos = self.points[tik1][tik2].location[1]-9
                squarewidth = 18
                squareheight = 18
                if self.heatMap[tik1][tik2] != 0:
                    # TODO stop the lattice drawing directly on the screen
                    pygame.draw.rect(screen,(255,cValue,cValue),(xpos,ypos,squarewidth,squareheight))
                

