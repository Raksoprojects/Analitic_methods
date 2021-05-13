import numpy as np
from matplotlib import pyplot as plt

n = 0.2

def euler(t):
    f = lambda ti, y: y*(1-y)*ti # ODE
    h = n
    s = np.zeros(len(t))
    s[0] = 1/2
    for i in range(0, len(t) - 1):
        s[i + 1] = s[i] + h*f(t[i], s[i])

    return s   

def Heun(t):

    t0 = t[0]
    f = lambda ti, y: y*(1-y)*ti # ODE
    x = 1/2
    s = np.array(x)
    h = n
    while t0 < t[-1]-h:
        k1 = h * f(t0,x)
        k2 = h * f(t0+h, x+k1) 
        x = x + 0.5 * (k1+k2)
        s = np.append(s,x)
        t0+=h  
    return s

def midpoint(t):

    t0 = t[0]
    f = lambda ti, y: y*(1-y)*ti
    yi = 1/2
    s = np.array(yi)
    h = n
    
    while t0 < t[-1]-h:
        yi2 = yi + f(t0, yi) * h/2
        yi = yi + f(t0+0.1, yi2) * h
        s = np.append(s, yi)
        t0 +=h


    return s


if __name__ == "__main__":
    #t = np.linspace(0,10,n)
    t = np.arange(0,10,n,dtype=float)

    y = np.exp((t*t/2)) / (np.exp((t*t/2)) + 1)

    y_euler = euler(t)

    y_heun = Heun(t)

    y_midpoint = midpoint(t)

    plt.plot(t,y, label="metoda analityczna")
    plt.plot(t,y_euler, label="metoda eulera")
    plt.plot(t,y_heun, label="metoda heuna, bez iteracji")
    plt.plot(t, y_midpoint, label="metoda punkty środkowego")
    plt.legend()
    plt.show()