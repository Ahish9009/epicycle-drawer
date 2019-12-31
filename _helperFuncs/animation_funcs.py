import math
import matplotlib.pyplot as plt

def pos_at(time, abs_fft, phase_fft):

    N = len(abs_fft)
    circle_pos = [(0,0)]
    loc_x = 0
    loc_y = 0
    w = 2*math.pi/N
    
    for i in range(N):

        loc_x += abs_fft[i]*math.cos((i)*w*time + phase_fft[i])
        loc_y += abs_fft[i]*math.sin((i)*w*time + phase_fft[i])

        circle_pos += [(loc_x, loc_y)]

    return circle_pos

def get_init_vals(n_circles, abs_fft, phase_fft):
    
    circles = []
    initCirclesPos = pos_at(0, abs_fft, phase_fft)
    for i in range(n_circles):
        circles += [plt.Circle(initCirclesPos[i], abs_fft[i], fill=False)]

    return circles
