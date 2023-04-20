#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Bisection Method
def f(x):
    y = x**2 - 4
    return y

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
 
c = (a+b)/2

while abs(f(c)) > 0.01:
    if f(a)*f(c) > 0:
        a = c
    else:
        b = c
        
    c = (a+b)/2
    
    print(c, " ", f(c))
    
print("The Root of x**2 - 4 is", c)          


# In[17]:


#Bisection Method
def f(x):
    y = x**3 - 4*x - 9
    return y

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
 
c = (a+b)/2

while abs(f(c)) > 0.01:
    if f(a)*f(c) > 0:
        a = c
    else:
        b = c
        
    c = (a+b)/2
    
    print(c, " ", f(c))
    
print("The Root of x**3 -4*x - 9 is", c)


# In[ ]:





# In[ ]:




