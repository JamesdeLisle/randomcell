from utility_functions import createWallMap
from lattice import *

class wallMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = createWallMap(width,height)

    def colorMap(self,screen):

        for tik1 in range(self.height):
            for tik2 in range(self.width):
                xpos = self.points[tik1][tik2].location[0]-9
                ypos = self.points[tik1][tik2].location[1]-9
                width = 19
                height = 19
                if self.Map[tik1][tik2]:
                    pygame.draw.rect(screen,(0,0,0),(xpos,ypos,width,height))
    

