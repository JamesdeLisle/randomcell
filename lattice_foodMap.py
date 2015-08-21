from utility_functions import *
from lattice import *

class foodMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.foodMap = [ [ False for x in range(self.width)] for y in range(self.height)]
