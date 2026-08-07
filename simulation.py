import numpy as np

from sun_and_earth import create_bodies
from spacecraft import create_spacecraft
from lagrange_point import calc_lagp
from lagrange_velocity import lagrange_velocity
from velocity_verlet import velocity_verlet

from Initial_conditions import G, R, mu, dt,steps


def run_simulation(selected_point,steps=steps):

    object1, object2 = create_bodies()

    lag_points = calc_lagp(mu, R)

    selected_point = np.array(lag_points[selected_point], dtype=float)

    omega = np.sqrt(G * (object1.mass + object2.mass) / R**3)

    craft_velocity = lagrange_velocity(selected_point, omega)

    spacecraft = create_spacecraft(

        position=selected_point,

        velocity=craft_velocity

    )

    bodies = [sun, earth, spacecraft]

    object1_traj = np.zeros((steps,3))
    object2_traj = np.zeros((steps,3))
    craft_traj = np.zeros((steps,3))

    for i in range(steps):

        velocity_verlet(bodies, dt)

        object1_traj[i] = object1.position
        object2_traj[i] = object2.position
        craft_traj[i] = spacecraft.position

    return object1_traj, object2_traj, craft_traj, lag_points
