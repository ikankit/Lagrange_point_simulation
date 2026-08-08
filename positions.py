import scipy as sc
import numpy as np
from Initial_conditions import mu

m1=-mu
m2=1-mu
def f(x):
    r1 = abs(x + mu)
    r2 = abs(x - 1 + mu)

    return x - (1-mu)*(x+mu)/r1**3 - mu*(x-1+mu)/r2**3
L1 =sc.optimize.root_scalar(f, bracket=[m1+1e-5,m2-1e-5]).root
L2 =sc.optimize.root_scalar(f, bracket=[m2+1e-5,5]).root
L3 =sc.optimize.root_scalar(f, bracket=[-5,m1-1e-5]).root
L4 = (0.5 - mu,np.sqrt(3) / 2)

L5 = (0.5 - mu,-np.sqrt(3) / 2)
if __name__=='__main__':
    print("L1=",L1)
    print("L2=",L2)
    print("L3=",L3)
    print("L4=",L4)
    print("L5=",L5)
    