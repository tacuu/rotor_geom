import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from scipy import interpolate

def var_interpolate(RPROP,orig_RPROP,orig_var):
    f = interpolate.interp1d(orig_RPROP, orig_var)
    var = f(RPROP)
    return var

# Data
panel_RPROP = [0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.9,0.95,1.0]
axis_RPROP = [0.0,1.0]
axis  = [0.0,0.0] #y
chord_RPROP = [0.15,0.9,1.0]
chord = [0.1,0.1,0.05] #y
flap_RPROP = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
flap = [i ** 2 / 5 for i in flap_RPROP] #z

#Interpolate to panel
panel_axis_y = var_interpolate(panel_RPROP,axis_RPROP,axis)
panel_chord_y = var_interpolate(panel_RPROP,chord_RPROP,chord)
panel_flap_z = var_interpolate(panel_RPROP,flap_RPROP,flap)

zeroarray = np.zeros(len(panel_RPROP))
#calc axis coordinate


#calc panel coordinate
LE_y = panel_axis_y + panel_chord_y / 4
TE_y = panel_axis_y - panel_chord_y / 4 * 3
LE_z = panel_flap_z
TE_z = panel_flap_z
LE_coord = np.array([panel_RPROP,LE_y,LE_z])
TE_coord = np.array([panel_RPROP,TE_y,TE_z])

#plot
fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111,projection='3d')

#panels
num_panels = len(panel_RPROP) - 1
panel_coord = np.zeros([5,3])
for i in range(num_panels):
    panel_coord[0] = [LE_coord[0,i],LE_coord[1,i],LE_coord[2,i]]
    panel_coord[1] = [TE_coord[0,i],TE_coord[1,i],TE_coord[2,i]]
    panel_coord[2] = [TE_coord[0,i+1],TE_coord[1,i+1],TE_coord[2,i+1]]
    panel_coord[3] = [LE_coord[0,i+1],LE_coord[1,i+1],LE_coord[2,i+1]]
    panel_coord[4] = panel_coord[0]
    ax.plot(panel_coord[:,0],panel_coord[:,1],panel_coord[:,2], lw=1, c='gray')

ax.plot(axis_RPROP, axis, np.zeros(len(axis)), lw=1)
#ax.plot(LE_coord[0],LE_coord[1],LE_coord[2], color = "red")
#ax.plot(TE_coord[0],TE_coord[1],TE_coord[2], color = "red")



#show
#ax.set_xlim(-1, 1)
#ax.set_ylim(-1, 1)
#ax.set_zlim(-1, 1)
ax.set_aspect('equal')
plt.show()

print("hello")