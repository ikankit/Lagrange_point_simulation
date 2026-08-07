import numpy as np

# Calculating Lagrange Points
def calc_lagp(mu,R):
    
  offset = mu*R
  r_l1 = R*(mu/3.0)**(1.0/3.0)
  l1_x = R-r_l1-offset
  r_l2 = R*(mu/3.0)**(1.0/3.0)
  l2_x = R+r_l2-offset
  r_l3 = R*(1.0-(7.0/12.0)*mu)
  l3_x = -offset-r_l3
  l4_x = R*(1.0/2.0)-offset
  l4_y = R*(np.sqrt(3.0)/2.0)
  l5_x = R*(1.0/2.0)-offset
  l5_y = -R*(np.sqrt(3.0)/2.0)
  return{"L1":(l1_x,0,0),
         "L2":(l2_x,0,0),
         "L3":(l3_x,0,0),
         "L4":(l4_x,l4_y,0),
         "L5":(l5_x,l5_y,0),
         }