from math import pi
import matplotlib.pyplot as plt


def create_time_span(t_start, t_end, step_size):
    """
    Create a timespan from t_start to t_end with step_size increments.
    :param t_start: start time
    :param t_end: end time
    :param step_size: step size (delta time)
    :return: A list of the timespan
    """
    time_span = []
    time_c = t_start
    while time_c <= t_end:
        time_span.append(time_c)
        time_c += step_size
    time_span.append(time_c)
    return time_span

# x_ddot + 2bw_0x_dot + w_0^2x = 0
# x_ddot = - 2bw_0x_dot - w_0^2x


w_0 = 2*pi
b = 0.5

x = 2
x_dot = 0
dt = 0.1
T = 10

time = create_time_span(0, T, dt)

x_data = [x]
x_dot_data = [x_dot]
x_ddot_data = [- 2*b*w_0*x_dot - w_0**2*x]

for t in time:
    if t == time[-1]:
        break
    x_ddot = - 2*b*w_0*x_dot - w_0**2*x
    x_dot += x_ddot * dt
    x += x_dot * dt

    x_ddot_data.append(x_ddot)
    x_dot_data.append(x_dot)
    x_data.append(x)

print(len(x_data))
print(len(time))
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(time, x_data, color='b')
height = 2  # 900
ax.set_xlim([0, T])
ax.set_ylim([-height, height])
ax.set_title('plot')
plt.grid()
plt.show()
