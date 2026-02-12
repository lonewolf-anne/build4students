import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Example data (you should replace this with your own)
time_vals = np.linspace(0, 10, 100)  # 100 points from 0 to 10 seco
#numpy.linspace --it generates an equal interval of numbers over a range
velocity_vals = 20 * time_vals - 9.81 * time_vals**2  # just a sample trajectory

fig, ax = plt.subplots()
line, = ax.plot([], [], color='r')
ax.set_xlim(0, max(time_vals))
ax.set_ylim(0, max(velocity_vals)*1.1)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Velocity (m/s)')
ax.set_title('Rocket Velocity Over Time')

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(time_vals[:i], velocity_vals[:i]) 
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init,
                             frames=len(time_vals), interval=100, blit=True)

plt.show()