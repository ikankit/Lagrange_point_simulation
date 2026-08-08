import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from Initial_conditions import mu

# Defining a function to find 2*U
def U2_func(x, y, mu):
  r1 = np.sqrt((x + mu)**2 + y**2) + 1e-10
  r2 = np.sqrt((x - (1 - mu))**2 + y**2) + 1e-10
  return (x**2 + y**2) + 2*(1 - mu)/r1 + 2*mu/r2

# Finding the derivative of 2*U along a axis
def dU_dx(x, mu):
  t1 = x
  t2 = (1 - mu) * (x + mu) / np.abs(x + mu)**3
  t3 = mu * (x - (1 - mu)) / np.abs(x - (1 - mu))**3
  return t1 - t2 - t3
def create_zvc_plot(mu):

    # Calculating the lagrange points and C

    x1 = 1 - mu - (mu / 3) ** (1 / 3)
    x2 = 1 - mu + (mu / 3) ** (1 / 3)
    x3 = -(1 + 5 * mu / 12)

    x_L1 = fsolve(dU_dx, x1, args=(mu,))[0]
    x_L2 = fsolve(dU_dx, x2, args=(mu,))[0]
    x_L3 = fsolve(dU_dx, x3, args=(mu,))[0]

    x_L4 = 0.5 - mu
    y_L4 = np.sqrt(3) / 2

    C1 = U2_func(x_L1, 0, mu)
    C2 = U2_func(x_L2, 0, mu)
    C3 = U2_func(x_L3, 0, mu)
    C4 = U2_func(x_L4, y_L4, mu)

    C_conditions = [C1 + 0.5,(C1 + C2) / 2,(C2 + C3) / 2,(C3 + C4) / 2,C4 - 0.5]
    titles = ["$C > C_1$","$C_1 > C > C_2$","$C_2 > C > C_3$","$C_3 > C > C_4$","$C < C_4$"]

    grid_pts = np.linspace(-2.2, 2.2, 800)

    X, Y = np.meshgrid(grid_pts, grid_pts)

    U2 = U2_func(X, Y, mu)

    fig, axes = plt.subplots(2, 3,figsize=(15, 10))

    axes = axes.flatten()

    for i, C_target in enumerate(C_conditions):

        ax = axes[i]
        if C_target >= np.min(U2):
            ax.contourf(X, Y,U2,levels=[np.min(U2),C_target],colors=["black"])
        # Bodies
        ax.scatter([-mu, 1 - mu], [0, 0], color="gray",zorder=5,s=[80, 40])
        # Lagrange points
        lag_x = [ x_L1, x_L2,x_L3, 0.5 - mu, 0.5 - mu]

        lag_y = [ 0, 0, 0,np.sqrt(3) / 2, -np.sqrt(3) / 2]
    
        lag_names = ["L1","L2","L3","L4", "L5"]
        ax.scatter(lag_x,lag_y,color="red",s=20,zorder=10)
        for lx, ly, name in zip(lag_x,lag_y,lag_names):
            ax.text(lx + 0.04,ly + 0.04, name, color="red",fontsize=8)
        ax.axhline(0,color="k",linewidth=0.5)
        ax.axvline(0, color="k",linewidth=0.5)
        ax.set_xlim(-2.2, 2.2)
        ax.set_ylim(-2.2, 2.2)
        ax.set_aspect("equal")
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([-2, -1, 0, 1, 2])
        ax.set_title(titles[i], y=-0.15,fontsize=14)
    axes[5].axis("off")

    fig.suptitle(
        "Zero-Velocity Curves (CR3BP)\n"
        "Black regions represent forbidden regions "
        "White regions represents permisseble regions"
        "($v^2 < 0$).",fontsize=14, y=0.95
    )

    plt.subplots_adjust(hspace=0.3,wspace=0.3)

    return fig