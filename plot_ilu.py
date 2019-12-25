from matplotlib import pyplot as plt
import numpy
import math
i=float(1.0)
while i<7.1:
    plt.scatter(i,11)
    i=i+0.2
i=float(1.0)
while i<7.1:
    plt.scatter(i,4)
    i=i+0.2
i=float(4)
while i<11.1:
    plt.scatter(4,i)
    i=i+0.2
i=float(11)
while i<14.7:
    plt.scatter(i,((5*i)-37)/3.6)
    i=i+0.2
i=float(7.4)
while i<11.1:
    plt.scatter(i,((-5*i)+73)/3.6)
    i=i+0.2
i=float(215)
while i<326:
    radian=float((math.pi/180)*i)
    x=float(3.60555*math.cos(radian))
    y=float(3.60555*math.sin(radian))
    plt.scatter(18.5+x,8+y)
    i=i+1
i=float(6.00)
while i<11.1:
    plt.scatter(21.5,i)
    i=i+0.2
i=float(6.00)
while i<11.1:
    plt.scatter(15.5,i)
    i=i+0.2
i=float(0)
while i<181:
    radian=float((math.pi/180)*i)
    x=float(1.8*math.cos(radian))
    y=float(1.8*math.sin(radian))
    plt.scatter(9.2+x,10+y)
    i=i+1
i=float(0)
while i<181:
    radian=float((math.pi/180)*i)
    x=float(1.8*math.cos(radian))
    y=float(1.8*math.sin(radian))
    plt.scatter(12.8+x,10+y)
    i=i+1
plt.show()
