import numpy as np
import matplotlib.pyplot as plt
trajectory_path = './trajectory.txt'
lines = [line.rstrip('\n') for line in open(trajectory_path)]
trajectory = []
for line in lines:
    splitted = line.split(' ')
    t_world_cam = [float(i) for i in splitted[1:4]]
    q = [float(i) for i in splitted[4:]]
    trajectory.append(t_world_cam)

trajectory = np.array(trajectory)
x,y,z = trajectory.T
plt.scatter(x,y)
plt.scatter(x[0],y[0])
plt.show()
