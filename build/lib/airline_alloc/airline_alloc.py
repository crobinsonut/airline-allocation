__all__ = ['Airline_alloc']
import numpy as np
from openmdao.main.api import Assembly, Component
from openmdao.lib.datatypes.api import Array, Float, Int

# Make sure that your class has some kind of docstring. Otherwise
# the descriptions for your variables won't show up in the
# source ducumentation.
class Airline_alloc(Component):
    """
    """
    # declare inputs and outputs here, for example:
    #x = Float(0.0, iotype='in', desc='description for x')
    #y = Float(0.0, iotype='out', desc='description for y')

    def execute(self):
        """ do your calculations here """
        pass
        