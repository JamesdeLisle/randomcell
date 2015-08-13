import pygame

class food:
    
    def __init__(self,lattice,x,y):
        self.x = x
        self.y = y
        lattice.foodMap[x][y] = True

    def printFood(self,screen,lattice):
        pygame.draw.circle(screen,(0,0,255),(lattice.points[self.x][self.y].location[0],lattice.points[self.x][self.y].location[1]),6)

