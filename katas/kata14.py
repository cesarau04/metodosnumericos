import numpy as np
import math
import matplotlib.pyplot as plt

n=5
a=0
b=1.5
h=0.1
x=np.linspace(a,b,n)
y0=1

def fprima(x,y):
    return 2*x*y

def euler(h,x,y0):
    y=[]
    y.append(y0)
    for i in range(1,len(x)):
        y.append(y[i-1]+h*fprima(x[i-1],y[i-1]))
    return y

y=euler(h,x,y0)
print(y)
