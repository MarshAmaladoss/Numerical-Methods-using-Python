#!/usr/bin/env python
# coding: utf-8

# In[1]:


def f(x):
    return 1/(1+x*x)
a = float(input("Lower Limit:"))
b = float(input("Upper Limit:"))
n = int(input("Number of Strips:"))
h = (b - a)/n
k = 1
sum = 0
while(k<n):
    t = a + k * h
    sum = sum + f(t)
    k = k + 1
int_a = (h/2)*(f(a) + f(b) + 2*sum)
print("Value of Integration:",int_a)

import sympy as sy
x = sy.Symbol("x")
int_e = sy.integrate(f(x), (x, 0, 1))
print("Exact Value:",int_e)


# In[ ]:




