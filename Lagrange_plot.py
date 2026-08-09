import matplotlib.pyplot as plt
import numpy as np
import positions as Pp



def Lagrange_point_plot(mu):
    
    m1=mu
    m2=1-mu

#positions
    m1_p=(-mu,0)
    m2_p=(1-mu,0)
    L4=(0.5-mu,np.sqrt(3)/2)
    L5=(0.5-mu,-np.sqrt(3)/2)
    L1=(Pp.L1, 0)
    L2=(Pp.L2, 0)
    L3=(Pp.L3, 0)

#plotting
    fig,ax=plt.subplots(figsize=(5,5))
    ax.set_aspect('equal')
    ax.set_xlim(-1.4,1.4)
    ax.set_ylim(-1.2,1.2)
    ax.axhline(0,color='black',linewidth=1)
    ax.axvline(0,color='black',linewidth=1)


    ax.text(1.42,-0.04,"x",fontsize=8)
    ax.text(-0.04,1.24,"y",fontsize=8)

#circle
    circle=plt.Circle((0,0),1,fill=False,linestyle='-',linewidth=1,color='dodgerblue')
    ax.add_patch(circle)

#barycenter
    ax.scatter(0,0,color='black',s=30,zorder=2)
    ax.text(-0.25,0.15,"Barycenter",ha='center',fontsize=7)

#m1
    ax.scatter(m1_p[0],0,s=700,color='gold',edgecolor='darkorange',linewidth=1,zorder=4)
    ax.text(m1_p[0]-0.15,-0.19,"Mass 1",ha='center',color='darkorange',fontsize=7)

#m2
    ax.scatter(m2_p[0],0,s=260,color='royalblue',edgecolor='white',linewidth=1,zorder=6)
    ax.text(m2_p[0]+0.1,-0.15,"Mass 2",ha='center',color='royalblue',fontsize=7)
    
#Lagrange Points
    lagrange_style = dict(s=50,edgecolor='black',linewidth=0.6,zorder=7)

# L1
    ax.scatter(L1[0],L1[1],color='crimson',**lagrange_style)
    ax.text(L1[0],0.05,"$L_1$",color='crimson',ha='center',fontsize=10)
# L2
    ax.scatter(L2[0],L2[1],color='crimson',**lagrange_style)
    ax.text(L2[0],0.05,"$L_2$",color='crimson',ha='center',fontsize=10)
# L3
    ax.scatter(L3[0],L3[1],color='crimson',**lagrange_style)
    ax.text(L3[0]-0.06,0.05,"$L_3$",color='crimson',ha='center',fontsize=10)
# L4
    ax.scatter(L4[0],L4[1],color='forestgreen',**lagrange_style)
    ax.text(L4[0]+0.02,L4[1]+0.03,"$L_4$",color='forestgreen',fontsize=10)
# L5
    ax.scatter(L5[0],L5[1],color='forestgreen',**lagrange_style)
    ax.text(L5[0]+0.03,L5[1]-0.06,"$L_5$",color='forestgreen',fontsize=10)

#triangle
    ax.plot([m1_p[0],m2_p[0],L4[0],m1_p[0]],[0,0,L4[1],0],linestyle='-',color='forestgreen',lw=1)
    ax.plot([m1_p[0],m2_p[0],L5[0],m1_p[0]],[0,0,L5[1],0],linestyle='-',color='forestgreen',lw=1)

#Title
#plt.suptitle("Positions of Lagrange Points (CR3BP)",fontsize=10,y=0.95)
#plt.title("Positions of Lagrange Points (CR3BP) in Normalized Rotating Frame",pad=20,fontsize=9.5)

#texts
#box=dict(boxstyle='round',facecolor='white')
#parameter=(r"$\mu=\frac{m_2}{m_1+m_2}$" "\n" r"$\mu = 3.003*10^{-6}$" "\n" "G=1 \n" "Distance=1")
#ax.text(1.5,1,parameter,bbox=box,fontsize=5)

    fig.tight_layout()
    
    return fig



