import numpy as np

def inv(points_fft, N):
    for tau in range(N):
        for k in range(len(points_fft)):
            # inverse fourier transform
            generated_function[tau] += points_fft[k]*(math.e**(1j*2*math.pi*k*tau/N))

    return [x/t for x in generated_function]
