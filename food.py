import pygame

class food:
    
    def __init__(self,actorLattices,x,y):
        self.x = x
        self.y = y
        actorLattices.food.Map[x][y] = True
        self.output = 10.0

    def printCell(self,screen,actorLattices):
        pygame.draw.circle(screen,(0,0,255),(actorLattices.drone.points[self.x][self.y].location[0],actorLattices.drone.points[self.x][self.y].location[1]),6)

