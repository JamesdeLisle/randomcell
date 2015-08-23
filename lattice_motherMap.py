from utility_functions import *
from lattice import *

class motherMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = [ [ False for x in range(self.width)] for y in range(self.height)]
