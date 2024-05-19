import numpy as np
import matplotlib.pyplot as plt


#problem parameters

a = 110 #heat diffusivity
length = 50 #mm
time = 4 #sec
nodes = 20

# differential units 

dx = length / nodes
dt = 0.5 * dx**2 / a
t_nodes = int(time/dt)

#Initial condition
u = np.zeros(nodes) + 15

# Boundary Conditions 
u[0] = 100
u[-1] = 100


# Visualisation setup

fig, axis = plt.subplots()

pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2, 3])

# Simulation

counter = 0

while counter < time :

    w = u.copy()

    for i in range(1, nodes - 1):

        u[i] = dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx ** 2 + w[i]

    counter += dt

    print("t: {:.3f} [s], Average temperature: {:.2f} Celsius".format(counter, np.average(u)))

    # visualisation

    pcm.set_array([u])
    axis.set_title("Distribution at t: {:.3f} s.".format(counter))
    plt.pause(0.01)


plt.show()










