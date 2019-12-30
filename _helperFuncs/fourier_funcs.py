import numpy as np
import math

def inv(points_fft, N):
    #inverse fourier array
    generated_function = np.asarray([0j for i in range(N)])

    for tau in range(N):
        for k in range(len(points_fft)):
            # inverse fourier transform
            generated_function[tau] += points_fft[k]*(math.e**(1j*2*math.pi*k*tau/N))

    return np.divide(generated_function, N)
