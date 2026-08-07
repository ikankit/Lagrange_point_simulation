import numpy as np

from sun_and_earth import create_bodies
from spacecraft import create_spacecraft
from lagrange_point import calc_lagp
from lagrange_velocity import lagrange_velocity
from velocity_verlet import velocity_verlet

from Initial_conditions import G, R, mu, dt,steps


def run_simulation(selected_point,steps=steps):

    sun, earth = create_bodies()

    lag_points = calc_lagp(mu, R)

    selected_point = np.array(lag_points[selected_point], dtype=float)

    omega = np.sqrt(G * (sun.mass + earth.mass) / R**3)

    craft_velocity = lagrange_velocity(selected_point, omega)

    spacecraft = create_spacecraft(

        position=selected_point,

        velocity=craft_velocity

    )

    bodies = [sun, earth, spacecraft]

    sun_traj = np.zeros((steps,3))
    earth_traj = np.zeros((steps,3))
    craft_traj = np.zeros((steps,3))

    for i in range(steps):

        velocity_verlet(bodies, dt)

        sun_traj[i] = sun.position
        earth_traj[i] = earth.position
        craft_traj[i] = spacecraft.position

    return sun_traj, earth_traj, craft_traj, lag_points