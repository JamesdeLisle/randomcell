from utility_functions import *
from lattice import *
import numpy as np

class heatMap(lattice):
    
    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.Map_old = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.dissipation  = 0.95
        self.cutoff = 1e-2 

    def colorMap(self,screen,printStep,printStep_max):
        
        for tik1 in range(self.height):
            for tik2 in range(self.width): 
                cValue_max = round((1-self.Map[tik1][tik2])*255)
                cValue_min = round((1-self.Map_old[tik1][tik2])*255)
                cValueVec = np.linspace(cValue_min,cValue_max,printStep_max)
                cValue = keepInBoundaries(0,cValueVec[printStep],255) 
                xpos = self.points[tik1][tik2].location[0]-9
                ypos = self.points[tik1][tik2].location[1]-9
                width = 19
                height = 19
                if self.Map[tik1][tik2] != 0:
                    pygame.draw.rect(screen,(255,cValue,cValue),(xpos,ypos,width,height))

