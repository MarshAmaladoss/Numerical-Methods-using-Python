#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math

def rk4(f, y0, t0, tf, h):
    # Runge-Kutta 4th Order Method 
    t = t0
    y = y0
    while t <= tf:
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        t = t + h
    return y


def f(t, y):
    return math.sin(t) - y

y0 = 0
t0 = 0
tf = 10
h = 0.1

y_sol = rk4(f, y0, t0, tf, h)

print("Solution at t = ", tf, " is: ", y_sol)


# In[9]:


import math

def rk4(f, x0, y0, xf, h):
    # Runge-Kutta 4th Order Method 
    x = x0
    y = y0
    while x <= xf:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
    return y


def f(x, y):
    return x**2+y**2

x0 = 1
y0 = 1.2
xf = 1.05
h = 0.05

y_sol = rk4(f, x0, y0, xf, h)

print("Solution at x = ", xf, " is: ", y_sol)


# In[11]:


def f(x,y):
    return x**2+y**2
x,y,h= 0.0,.65,0.5
for i in range(1000):
    k1= h*f(x,y)
    k2= h* f(x+0.5*h, y+0.5*k1)
    k3= h* f(x+0.5*h, y+0.5*k2)
    k4= h* f(x+h, y+k3)
    y=y+ (k1+2*k2+2*k3+k4)/6.0
    x=x+h
    
    print(x,y)


# In[17]:


#10. Runge-Kutta fourth order method of solving differential eqautions

def f(x,y):
    return (x+y)**2

x = 0
y = 1

xmax = 0.2 # y(xmax) will be calculated
stepsize = 0.05 # Size by which x values should differ
while x<xmax:
    k1 = stepsize * f(x,y)
    k2 = stepsize * f(x+stepsize/2, y + k1/2)
    k3 = stepsize * f(x+stepsize/2, y + k2/2)
    k4 = stepsize * f(x + stepsize, y+k3)
    deltay = (k1+2*k2+2*k3+k4)/6
    y = y + deltay
    x = x + stepsize
    print(x,y)


# In[ ]:




