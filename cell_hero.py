from cell import *
from utility_functions import *

class hero(cell):
    
    def __init__(self,actorLattices,x,y):
        cell.__init__(self,x,y)
        self.species = 'hero'
        actorLattices.hero.Map[x][y] = True

    def printCell(self, screen, actorLattices, printStep, printStep_max):
        
        xVec,yVec = self.generateAnimationVectors(actorLattices,printStep_max) 
        aura1 = pygame.Surface((140,100))
        aura1.set_alpha(100)
        aura1.fill((200,255,0))
       
        aura2 = pygame.Surface((100,20))
        aura2.set_alpha(100)
        aura2.fill((200,255,0))

        aura3 = pygame.Surface((100,20))
        aura3.set_alpha(100)
        aura3.fill((200,255,0))

        screen.blit(aura1,(xVec[printStep]-70,yVec[printStep]-50))
        screen.blit(aura2,(xVec[printStep]-50,yVec[printStep]-70))
        screen.blit(aura3,(xVec[printStep]-50,yVec[printStep]+50))
        
        xPos = xVec[printStep]
        yPos = yVec[printStep]

        p1 = (xPos-70,yPos-50)
        p2 = (xPos-50,yPos-50)
        p3 = (xPos-50,yPos-70)
        p4 = (xPos+50,yPos-70)
        p5 = (xPos+50,yPos-50)
        p6 = (xPos+70,yPos-50)
        p7 = (xPos+70,yPos+50)
        p8 = (xPos+50,yPos+50)
        p9 = (xPos+50,yPos+70)
        p10 = (xPos-50,yPos+70)
        p11 = (xPos-50,yPos+50)
        p12 = (xPos-70,yPos+50)

        pygame.draw.polygon(screen,(201,25,0),(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12),3)

        pygame.draw.polygon(screen,(0,0,0),((xVec[printStep]-10,yVec[printStep]),(xVec[printStep],yVec[printStep]-10),(xVec[printStep]+10,yVec[printStep]),(xVec[printStep],yVec[printStep]+10)))
        pygame.draw.polygon(screen,(0,128,255),((xVec[printStep]-9,yVec[printStep]),(xVec[printStep],yVec[printStep]-9),(xVec[printStep]+9,yVec[printStep]),(xVec[printStep],yVec[printStep]+9)))
    
    def moveCell(self,fluidLattices,actorLattices,shift):
        
        adjCells = getAdjacent(fluidLattices.wall.Map,self.x,self.y)
        nCells = len(adjCells[:])
        move_flag = False

        for tik in range(nCells):
            if self.x + shift[0] == adjCells[tik][0] and self.y + shift[1] == adjCells[tik][1]:
                move_flag = True
        
        if not move_flag:
            shift = [0,0]

        self.updateCellMap(actorLattices,False)
        self.previous_x = self.x
        self.previous_y = self.y
        self.x = self.x + shift[0]
        self.y = self.y + shift[1]
        self.updateCellMap(actorLattices,True)
        minLx = 0
        minLy = 0
        maxLy = actorLattices.drone.width
        maxLx = actorLattices.drone.height
        self.x = wrapBoundaries(minLx,self.x,maxLx)
        self.y = wrapBoundaries(minLy,self.y,maxLy)

    def dropFood(self,actorLattices, foodList):
         
        foodList.addCell(actorLattices,self.x,self.y) 

    def updateCell(self, fluidLattices, actorLattices, shift):

        self.moveCell(fluidLattices,actorLattices,shift)

    def createWall(self, fluidLattices, wallOrientation):
        
        wallLength = 5
        wallVec = [-2,-1,0,1,2]
        if wallOrientation == 'vertical': 
            for tik in range(wallLength):
                fluidLattices.wall.Map[self.x + wallVec[tik]][self.y] = True
        elif wallOrientation == 'horizontal':
            for tik in range(wallLength):
                fluidLattices.wall.Map[self.x][self.y+wallVec[tik]] = True
