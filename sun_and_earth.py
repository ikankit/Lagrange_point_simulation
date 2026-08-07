import numpy as np

from Initial_conditions import G,R,mu,omega
from body import Body

def create_bodies():
    m_earth=mu
    m_sun=1-mu
    
    sun_pos= np.array([-mu*R,0.0,0.0])          #sun initial position
    
    earth_pos= np.array([(1-mu)*R,0.0,0.0])     #earth initial position
    
    sun_vel= np.array([0.0,-omega*mu*R,0.0])    #sun initial velocity
    
    earth_vel=np.array([0.0,omega*(1-mu)*R,0.0])  #earth initial velocity
    
    sun=Body(
        name= "Sun",
        mass= m_sun,
        position= sun_pos,
        velocity= sun_vel
        )                                #sun body
    
    earth=Body(
        name="Earth", 
        mass=m_earth, 
        position=earth_pos, 
        velocity=earth_vel
        )                             #earth body
    
    return sun,earth