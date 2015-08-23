from utility_functions import *
from lattice import *

class smellMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.Map_old = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.dissipation = 0.8
        self.cutoff = 0.0

    def colorMap(self,screen):
        
        for tik1 in range(self.height):
            for tik2 in range(self.width): 
                cValue = round((1-self.Map[tik1][tik2])*255)
                cValue = keepInBoundaries(0,cValue,255)
                xpos = self.points[tik1][tik2].location[0]
                ypos = self.points[tik1][tik2].location[1]
                if self.Map[tik1][tik2] > 1e-2 and cValue < 250:
                    pygame.draw.circle(screen,(cValue,255,cValue),(xpos,ypos),4)
