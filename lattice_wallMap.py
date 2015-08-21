from utility_functions import *
from lattice import *

class wallMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = createWallMap(width,height)


