from math import sqrt

# Physics Constants & Center of Mass 
G = 1  #Gravitational coonstant
R = 14  #Distance b/w earth and sun
m_of_object1=0.97

m_of_object2=0.03

mu =(m_of_object2)/(m_of_object1+m_of_object2) # Mass ratio

m_earth = mu #Earth mass
m_sun = 1.0 - mu #Sun mass

omega = sqrt(G * 1.0 / R**3) #Angular velocity

nudge = 0.15  #Small Displacement
craft_m = 0.000001  #Mass of spacecraft

dt = 0.1    #No.of timesteps

steps= 20000 #Total steps
