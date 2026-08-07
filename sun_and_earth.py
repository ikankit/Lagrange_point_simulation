import numpy as np

from Initial_conditions import G,R,mu,omega
from body import Body

def create_bodies():
    m_object1 = mu
    m_object2 = 1-mu
    
    object1_pos= np.array([-mu*R,0.0,0.0])          #sun initial position
    
    object2_pos= np.array([(1-mu)*R,0.0,0.0])     #earth initial position
    
    object1_vel= np.array([0.0,-omega*mu*R,0.0])    #sun initial velocity
    
    object2_vel=np.array([0.0,omega*(1-mu)*R,0.0])  #earth initial velocity
    
    object1=Body(
        name= "object 1",
        mass= m_object1,
        position= object1_pos,
        velocity= object1_vel
        )                                #sun body
    
    object2=Body(
        name="object 2", 
        mass=m_object2, 
        position=object2_pos, 
        velocity=object2_vel
        )                             #earth body
    
    return object1,object2
