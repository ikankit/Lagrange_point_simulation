import matplotlib.pyplot as plt
import numpy as np
import scipy as sc 
import positions as Pp
from Initial_conditions import mu


def create_effective_potential(mu):

    m_earth=mu
    m_sun=1-mu

    L1=Pp.L1
    L2=Pp.L2
    L3=Pp.L3   
    L4=(0.5-mu,np.sqrt(3)/2)
    L5=(0.5-mu,-np.sqrt(3)/2)
    
    sun=(-mu,0)
    earth=(1-mu,0)
    
    x=np.linspace(-1.5,1.5,800)
    y=np.linspace(-1.5,1.5,800)
    
    X,Y=np.meshgrid(x,y)
    r1=np.sqrt((X+mu)**2+Y**2)
    r2=np.sqrt((X-1+mu)**2+Y**2)
    
    omega=-((1-mu)/r1)-(mu/r2)-0.5*(X**2+Y**2)
    
    omega[r1<0.0001]=np.nan
    omega[r2<0.0001]=np.nan

    v_max=-0.5*(mu**2-mu+3) 
    upper=v_max+6
    lower=v_max-1.5
#print(v_max)
    omega_clipped=np.clip(omega,lower,upper)
    
    fig,ax=plt.subplots(figsize=(6,6),dpi=150)
    contour=ax.contour(X,Y,omega_clipped,levels=25,cmap='plasma')
    ax.clabel(contour, inline=True, fontsize=3, fmt='%1.2f')

#Positions of 2 bodies
    ax.plot(sun[0],sun[1],'ro', markersize=10)
    ax.plot(earth[0],earth[1],'ro', markersize=5)
    
    ax.plot(L4[0],L4[1],'bo', markersize=2)
    ax.text(L4[0]+0.025,L4[1]+0.025,"L4",color="red",fontsize=8)

    ax.plot(L5[0],L5[1],'bo', markersize=2)
    ax.text(L5[0]+0.025,L5[1]+0.025,"L5",color="red",fontsize=8)

    ax.plot(L1,0,'bo', markersize=3)
    ax.text(L1-0.1,0,"L1",color="red",fontsize=8)

    ax.plot(L2,0,'bo', markersize=2)
    ax.text(L2+0.045,0,"L2",color="red",fontsize=8)

    ax.plot(L3,0,'bo', markersize=2)
    ax.text(L3+0.025,0,"L5",color="red",fontsize=8)


    ax.set_aspect('equal')
    ax.set_xlabel("x",fontsize=10)
    ax.set_ylabel("y",fontsize=10)
    ax.set_title("Effective Potential in the CR3BP",fontsize=10)
    

    fig.tight_layout()
    return fig