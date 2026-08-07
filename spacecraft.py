import numpy as np

from Initial_conditions import craft_m

from body import Body

def create_spacecraft(position,velocity):
    
    spacecraft = Body(
    name="spacecraft",
    mass=craft_m,
    position=np.array(position, dtype=float),
    velocity=np.array(velocity, dtype=float))
    
    return spacecraft
