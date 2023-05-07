import matplotlib.pyplot as plt
import numpy as np



def function(t, times, w):
    to_return = 0
    for i in range(times):
        to_return += w[i]*t**i
    return to_return


def getValues(t):
    noise = np.random.normal(0,0.5,t)
    return np.array([5*np.cos(i) + noise[i] for i in range(t)])