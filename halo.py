import numpy as np
from scipy.integrate import solve_ivp
import plotly.graph_objects as go
thrust = 1e-3 # Change can be done based on condition give this shit a slider
#Writing as func for Ankit to paste easily

def cr3bp_equations(t,state,mu):
  x,y,z,vx,vy,vz = state
  r1 = np.sqrt((x + mu)**2 + y**2 + z**2)
  r2 = np.sqrt((x-1 + mu)**2 + y**2 + z**2)
  #accelaration
  ax = x + 2*vy - (1-mu)*(x+mu)/(r1**3) - mu*(x-1+mu)/(r2**3)
  ay = y - 2*vx - (1-mu)*y/(r1**3) - mu*y/(r2**3)
  az = - (1-mu)*z/(r1**3) - mu*z/(r2**3)
  return[vx,vy,vz,ax,ay,az]

def run_halo_orbi(mu,state0)
  # Constant engine burns
  v_mag = np.sqrt(vx**2 + vy**2 + vz**2)
  if v_mag > 10:
    tx = thrust * (vx/v_mag)
    ty = thrust * (vy/v_mag)
    tz = thrust * (vz/v_mag)
  else:
    tx = 0
    ty = 0
    tz = 0
  ax+=tx
  ay+=ty
  az+=tz
  return[vx,vy,vz,ax,ay,az]
# Initializations insert values
x0 = 1.10
y0 = 0.0
z0 = 0.14
vx0= 0.0
vy0 = -0.22
vz0 = 0.0
flag0 = [x0,y0,z0,vx0,vy0,vz0]
time = np.linspace(0,3.2,1000)
sol = solve_ivp(equations_halo, [0,3.2], flag0, t_eval=time,method = 'RK45',rtol = 1e-9,atol = 1e-9)

#Plot

fig = go.Figure(data=[go.Scatter3d(x=sol.y[0], y=sol.y[1], z=sol.y[2],mode = "lines",line = dict(color = "blue",width = 4),name = "Halo orbit"),go.Scatter3d(x=sol.y[0], y=sol.y[1], z=sol.y[2],mode = "markers",marker = dict(color = "gray",size = 8),name = "Test")])
fig.update_layout(title = "Earth-Sun L2 Halo orbit (C3RBP)",scene =dict(xaxis_title = "x",yaxis_title = "y",zaxis_title = "z"))
fig.show()
# For lyapunov point just make z axis 0 that means vz and z = 0