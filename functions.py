import math
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


def calc_slope(xs, ys):
    
    return ((np.mean(xs) * np.mean(ys) - np.mean(xs * ys)) / (np.mean(xs)**2 - np.mean(xs*xs)))

def best_fit(xs,ys):
    
    m = calc_slope(xs,ys)
    c = np.mean(ys) - (m * np.mean(xs))
    return m,c
            
def reg_line (m, c, xs):
        #pythonic way vs utilizing a list, same concept, potentially more efficient, maybe test?
    return [(m*x)+c for x in xs]
def plot(x,y,r_line):
    plt.scatter(x,y,color='#003F72', label="Data points")
    plt.plot(x, r_line, label= "Regression Line")
    plt.legend()
def predict(m,c,x):
    return m*x + c
                                                           