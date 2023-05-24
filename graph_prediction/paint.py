import matplotlib.pyplot as plt
import numpy as np



def function(t, w):
    to_return = 0
    for i in range(len(w)):
        to_return += w[i]*t**i
    return to_return


def getValues(t):
    noise = np.random.normal(0,0.5,t)
    return np.array([5*np.cos(i) + noise[i] for i in range(t)])


def error(y, w):
    error = 0
    for i in range(len(y)):
        error += (y[i] - function(i, w))**2 
    return error + 0.1*np.linalg.norm(w)**2

def random_guess(y, w_amount, times):
    w = [0 for i in range(w_amount)]
    for i in range(times):
        curr = w.copy()
        curr[int(np.random.uniform(0,len(curr)))] += np.random.uniform(-1,1)
        if error(y, curr) < error(y, w) or np.random.uniform(0,1) > i/times:
            w = curr.copy()
    return w
