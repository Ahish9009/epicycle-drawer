import math

def pos_at(time, abs_fft, phase_fft):

    N = len(abs_fft)
    circlePos = [(0,0)]
    loc_x = 0
    loc_y = 0
    w = 2*math.pi/N

    for i in range(N):

        loc_x += abs_fft[i]*math.cos((i)*w*time + phase_fft[i])
        loc_y += abs_fft[i]*math.sin((i)*w*time + phase_fft[i])

        circlePos += [(loc_x, loc_y)]

    return circlePos
