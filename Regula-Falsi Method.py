#!/usr/bin/env python
# coding: utf-8

# In[5]:


#4. Regula-Falsi Method

def f(x):
    return x**3-x-2

a = int(input("First Initial Guess:"))
b = int(input("Second Initial Guess:"))
n = int(input("Number of Interactions:"))

if f(a)>f(b):
    print("Regula-Falsi Method Fails")
else:
    k = 1
    while(k<=n):
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        if f(a)*f(c)<0:
            b = c
        else:
            a = c
        print("Root is",c,"at",k,"iteration")    
        k=k+1
        
    


# In[ ]:





# In[ ]:




