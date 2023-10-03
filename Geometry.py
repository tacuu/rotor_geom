import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib.animation import FuncAnimation
from scipy import interpolate

def var_interpolate(RPROP,orig_RPROP,orig_var):
    f = interpolate.interp1d(orig_RPROP, orig_var)
    var = f(RPROP)
    return var

def panel_plot(ax,panel_RPROP,LE_coord,TE_coord):
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
    return

# Data
panel_RPROP = [0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.9,0.95,1.0]
axis_RPROP = [0.0,1.0]
axis  = [0.0,0.0] #y
chord_RPROP = [0.15,0.9,1.0]
chord = [0.1,0.1,0.05] #y
flap_RPROP = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

PSI = np.linspace(0, 2*np.pi, 24)

fig = plt.figure(figsize=plt.figaspect(1))

""" for j in PSI:
    flap = [i ** 2 / 5 * np.sin(j) for i in flap_RPROP] #z
    lag = flap
    pitch = flap

    #Interpolate to panel
    panel_axis_y = var_interpolate(panel_RPROP,axis_RPROP,axis)
    panel_chord_y = var_interpolate(panel_RPROP,chord_RPROP,chord)
    panel_flap_z = var_interpolate(panel_RPROP,flap_RPROP,flap)
    panel_lag_y = var_interpolate(panel_RPROP,flap_RPROP,lag)
    panel_pitch = var_interpolate(panel_RPROP,flap_RPROP,pitch)

    zeroarray = np.zeros(len(panel_RPROP))

    #calc axis coordinate
    axis_coord = np.array([panel_RPROP, panel_axis_y + panel_lag_y, panel_flap_z])

    #calc panel coordinate
    LE_y = axis_coord[1] + panel_chord_y / 4
    TE_y = axis_coord[1] - panel_chord_y / 4 * 3
    LE_z = panel_flap_z - panel_chord_y / 4 * np.sin(panel_pitch)
    TE_z = panel_flap_z + panel_chord_y / 4 * 3 * np.sin(panel_pitch)
    LE_coord = np.array([panel_RPROP,LE_y,LE_z])
    TE_coord = np.array([panel_RPROP,TE_y,TE_z])

    #axis
    axis_coord = np.insert(axis_coord, 0, [axis_RPROP[0],axis[0],0], axis=1)

    #plot
    ax = fig.add_subplot(111,projection='3d')

    #panels
    num_panels = len(panel_RPROP) - 1
    #panel_coord = np.zeros([3,5])
    panel_coord = np.zeros([5,3])
    for i in range(num_panels):
        # panel_coord[:,0] = [LE_coord[0,i],LE_coord[1,i],LE_coord[2,i]]
        # panel_coord[:,1] = [TE_coord[0,i],TE_coord[1,i],TE_coord[2,i]]
        # panel_coord[:,2] = [TE_coord[0,i+1],TE_coord[1,i+1],TE_coord[2,i+1]]
        # panel_coord[:,3] = [LE_coord[0,i+1],LE_coord[1,i+1],LE_coord[2,i+1]]
        # panel_coord[:,4] = panel_coord[:,0]
        # ax.plot(panel_coord[0],panel_coord[1],panel_coord[2], lw=1, c='gray')
        panel_coord[0] = [LE_coord[0,i],LE_coord[1,i],LE_coord[2,i]]
        panel_coord[1] = [TE_coord[0,i],TE_coord[1,i],TE_coord[2,i]]
        panel_coord[2] = [TE_coord[0,i+1],TE_coord[1,i+1],TE_coord[2,i+1]]
        panel_coord[3] = [LE_coord[0,i+1],LE_coord[1,i+1],LE_coord[2,i+1]]
        panel_coord[4] = panel_coord[0]
        ax.plot(panel_coord[:,0],panel_coord[:,1],panel_coord[:,2], lw=1, c='gray')

    #show
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.5, 0.5)
    ax.set_zlim(-0.5, 0.5)
    ax.set_aspect('equal')
    #img = ax

    #ims.append([im])
 """
#animation function
def update_plot(k):
    flap = [i ** 2 / 5 * np.sin(k) for i in flap_RPROP] #z
    lag = flap
    pitch = flap

    #Interpolate to panel
    panel_axis_y = var_interpolate(panel_RPROP,axis_RPROP,axis)
    panel_chord_y = var_interpolate(panel_RPROP,chord_RPROP,chord)
    panel_flap_z = var_interpolate(panel_RPROP,flap_RPROP,flap)
    panel_lag_y = var_interpolate(panel_RPROP,flap_RPROP,lag)
    panel_pitch = var_interpolate(panel_RPROP,flap_RPROP,pitch)

    zeroarray = np.zeros(len(panel_RPROP))

    #calc axis coordinate
    axis_coord = np.array([panel_RPROP, panel_axis_y + panel_lag_y, panel_flap_z])

    #calc panel coordinate
    LE_y = axis_coord[1] + panel_chord_y / 4
    TE_y = axis_coord[1] - panel_chord_y / 4 * 3
    LE_z = panel_flap_z - panel_chord_y / 4 * np.sin(panel_pitch)
    TE_z = panel_flap_z + panel_chord_y / 4 * 3 * np.sin(panel_pitch)
    LE_coord = np.array([panel_RPROP,LE_y,LE_z])
    TE_coord = np.array([panel_RPROP,TE_y,TE_z])

    #axis
    axis_coord = np.insert(axis_coord, 0, [axis_RPROP[0],axis[0],0], axis=1)

    #plot 
    ax = fig.add_subplot(111,projection='3d')

    #panels
    panel_plot(ax,panel_RPROP,LE_coord,TE_coord)

    ax.plot(axis_coord[0],axis_coord[1],axis_coord[2],lw=1,c='gray')

    #set
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.5, 0.5)
    ax.set_zlim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.view_init(elev=10, azim=-10)

    #message = "PSI=" + int(k * 180 / np.pi)
    print(int(k * 180 / np.pi))

#ani = animation.ArtistAnimation(fig, ims, interval=100)
ani = FuncAnimation(fig, update_plot, PSI, interval=1)
ani.save("test.gif", writer="pillow")
#ani.save('wf_anim_art.mp4',writer='ffmpeg',dpi=100)
#plt.show()

print("Finished")