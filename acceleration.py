import numpy as np
from gravitational_force import gravitational_force

def body_acc(body,bodies):
    
    F_total= np.zeros(3)
    
    for other_body in bodies:
        if other_body is body:
            continue
        F_total=F_total+gravitational_force(body, other_body)
    acceleration = F_total/body.mass
    
    return acceleration