import numpy as np
import matplotlib.pyplot as plt

# Load in vertices with mass for hull half
plan_vertices = np.loadtxt('vertices.tsv', delimiter='\t', skiprows=1)

# Create polygon with mirror
vertices = np.zeros((plan_vertices.shape[0]*2-2,3), dtype=np.float64)
vertices[:plan_vertices.shape[0],:] = plan_vertices
for i in range(plan_vertices.shape[0]-2):
    index = i+plan_vertices.shape[0]
    vertices[index,:] = plan_vertices[-i-2]
    vertices[index,1] *= -1

# Plot result
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(vertices[:,1],vertices[:,2])
ax.set_aspect('equal', 'box')
plt.show()

# Calculate total mass, center of mass, moment of inertia
mass = 0.
center_of_mass = np.zeros(2)
moment_of_intertia = 0.

for i in range(vertices.shape[0]):
    mass += vertices[i,0]
    center_of_mass += vertices[i,1:]*vertices[i,0]
center_of_mass /= mass

for i in range(vertices.shape[0]):
    moment_of_intertia += vertices[i,0]*np.linalg.norm(vertices[i,1:]-center_of_mass)

print('mass: ', mass)
print('center_of_mass: ', center_of_mass)
print('moment of inertia: ', moment_of_intertia)

# Calculate draft, and displacement change per draft change, center of buoyancy
center_of_buoyancy = np.zeros(2)

# Calculate righting moment (includes calculating shift of center of buoyancy) and location of metacenter

# Make a plot of righting force and heaving force as functions of roll and heave

# Make plot of resonant frequencies