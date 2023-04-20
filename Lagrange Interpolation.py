#!/usr/bin/env python
# coding: utf-8

# In[4]:


# From the data in the following table, find the value of P(50) by using Lagrange Interpolation.

x = [0, 20, 40, 60, 80, 100]
y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

m = len(x)
n = m - 1  #degree of the polynomial

xp = float(input("Enter x: "))
yp = 0
for i in range(n + 1):
    p = 1
    for j in range(n + 1):
        if j != i:
            p *= (xp - x[j])/(x[i] - x[j])
    yp += y[i]*p
    
print("For x = %2f, y = %f" %(xp, yp))    
    


# In[ ]:




