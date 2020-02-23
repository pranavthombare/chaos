import numpy as np
import matplotlib.pyplot as plt

iter = 200
list1 = []
points_to_be_looked_at = 500

def logisticFunc(r,x):
    return r * x * (1 - x)


def iterateLogistic(n,r,x):
    y = np.arange(n)
    for i in range(n):
        list1.append(logisticFunc(r,x))
        x = logisticFunc(r,x)
    plt.plot(y,list1)
    plt.show()

def bifurcationMap(x):
    #Let's store the values of r and x
    R = []
    X = []

    #We will split r and use to loop 
    r_range = np.linspace(1 ,4 ,10000)

    for r in r_range:
        for i in range(1,800 + 200):
            if i >= 800:
                R.append(r)
                X.append(x)
            x = logisticFunc(r,x)

    plt.scatter(R,X, s = 0.5) 
    plt.ylim(0, 1)
    plt.xlim(0, 4)
    plt.xlabel('r')
    plt.ylabel('X')
    plt.show()

iterateLogistic(200,2,0.7)