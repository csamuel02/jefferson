from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)

y = (x * x) - 4

plot(x, y)
grid()
show()