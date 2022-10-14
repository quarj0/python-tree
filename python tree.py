from numpy import *
from matplotlib import pyplot as plt
t = linspace(0,39*pi/2,1000)
x = t*cos(t)**3
y = 9*t*sqrt(abs(cos(t)))+t*sin(0.2*t)*cos(4*t)
plt.plot(x,y,c='green')
plt.grid(True)
plt.title("From Python")
plt.show()
