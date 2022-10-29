import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from assist_functions.assist_functions import create_time_span, compress
import time as real_time

# Simulation #
dt = 0.01
time = create_time_span(0, 5, dt)

# F = m * x_ddot
# F = -m*g
# x_ddot = -g
# if x <= ballradius
# F = -mg + N
# N = mg
# m * x_ddot = -mg + mg
# x_ddot = -g + g = 0
x_ddot_sim = []
x_dot_sim = []
x_sim = []

ball_radius = 1
g = 9.81
x_dot_0 = 0
x_0 = 10

x_ddot = -g
x_dot = x_dot_0
x = x_0
e = 0.55  # e E[0,1]
for t in time:
    if t == 0:
        x_ddot = -g
        x_dot = x_dot_0
        x = x_0
        x_ddot_sim.append(x_ddot)
        x_dot_sim.append(x_dot)
        x_sim.append(x)
    else:
        x_ddot = -g
        x_dot += x_ddot * dt
        x += x_dot * dt
        if x <= ball_radius:
            x_ddot = -g + g
            x_dot += - (1+e)*x_dot*1
            x = ball_radius
        x_ddot_sim.append(x_ddot)
        x_dot_sim.append(x_dot)
        x_sim.append(x)

# ANIMATION #

# "Compress" animation
fps = 30
x_sim, time = compress(fps, x_sim, time)

fig, ax = plt.subplots(figsize=(6.41, 8.8))

time_template = 'time = %.1fs'
real_time_template = 'real time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
real_time_text = ax.text(0.05, 0.85, '', transform=ax.transAxes)

x_limit = 4
y_limit_max = x_0 + ball_radius
y_limit_min = -1
floor_start = 0

ax.set_xlim(-x_limit, x_limit)
ax.set_ylim(y_limit_min, y_limit_max)

floor, = ax.plot([-x_limit, x_limit], [floor_start, floor_start], 'k-', lw=1)
circle = plt.Circle((0, 0), 1, fc='b')

ax.set_aspect(1)
start_time = 0


def init():
    time_text.set_text('')
    real_time_text.set_text('')
    circle.center = (0, 0)
    ax.add_artist(circle)
    return circle, time_text, real_time_text


def update(frame):
    global start_time
    if frame == 0:
        start_time = real_time.time()
    circle.center = (0, x_sim[frame])
    time_text.set_text(time_template % time[frame])
    elapsed_time = real_time.time() - start_time
    real_time_text.set_text(real_time_template % elapsed_time)
    return circle, time_text, real_time_text


# blit=True ensures that only the portions of the image which have changed are updated.
ani = FuncAnimation(fig, update, frames=len(time), interval=1/fps*1000, init_func=init, blit=True)

ani.save('../gifs/ball_bouncing.gif', writer='imagemagick', fps=15)  # Uncomment to update gif

plt.show()
