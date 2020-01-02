import matplotlib.pyplot as plt
import numpy as np

def pos_at(time, abs_fft, phase_fft):

    N = len(abs_fft)
    circle_pos = [(0,0)]
    loc_x = 0
    loc_y = 0
    w = 2*np.pi/N
    
    for i in range(N):

        loc_x += abs_fft[i]*np.cos((i)*w*time + phase_fft[i])
        loc_y += abs_fft[i]*np.sin((i)*w*time + phase_fft[i])

        circle_pos += [(loc_x, loc_y)]

    return circle_pos

def get_init_vals(n_circles, abs_fft, phase_fft):
    
    circles = []
    initCirclesPos = pos_at(0, abs_fft, phase_fft)
    for i in range(n_circles):
        circles += [plt.Circle(initCirclesPos[i], abs_fft[i], fill=False)]

    return circles

def get_circle(r, centerPos):
    n_points = int(r)+200
    theta = np.linspace(0, 2*np.pi, n_points)
    y = r*np.cos(theta) + centerPos[0]
    z = r*np.sin(theta) + centerPos[1]

    return y, z
