import numpy as np

from body import Body

from Initial_conditions import G


def gravitational_force( object1, object2):
    
#force acting on 1 due to 2
    r_object1_object2  =  object1.position -  object2.position
    distance=np.linalg.norm( r_object1_object2 )
    
    if distance < 1e-6:
        print("WARNING: Distance almost zero!")
        print(object1.name, object2.name)
    
    force=-((G* ( object1.mass ) * ( object2.mass ) ) / (distance**3)) * r_object1_object2
        
    return(force)