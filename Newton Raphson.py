#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Newton-Raphson Method
#f(x)=x**3-x*x-2 and the root lies between 1 and 2
def f(x):
    return x**3-x*x-2
def df(x):
    return 3*x*x-2*x

a=float(input("Initial Value: "))
n=int(input("Number of Iterations: "))
k=1
while(k<=n):
    r=a-(f(a)/df(a))
    print("Root is",r,"at",k,"iteration")
    k=k+1
    a=r


# In[2]:


#Newton-Raphson Method
#f(x)=2*x**3-2*x-5 and the root lies between 1 and 2
def f(x):
    return 2*x**3-2*x-5
def df(x):
    return 6*x**2-2

a=float(input("Initial Value: "))
n=int(input("Number of Iterations: "))
k=1
while(k<=n):
    r=a-(f(a)/df(a))
    print("Root is",r,"at",k,"iteration")
    k=k+1
    a=r


# In[ ]:




