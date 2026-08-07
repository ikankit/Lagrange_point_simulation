import numpy as np
class Body:   #It storese all the attributes of body
    def __init__(self, name, mass, position, velocity):
        self.name=name
        self.mass=mass
        self.position=position
        self.velocity=velocity
        self.acc_old=np.zeros(3)
        self.acc_new=np.zeros(3)
