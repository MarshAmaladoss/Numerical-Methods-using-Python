#!/usr/bin/env python
# coding: utf-8

# In[2]:


#7. Simpson's 3/8 rule of Integration
import math
def f(x):
   return 1/math.sqrt(1+x)

a=float(input("Lower Limit:"))
b=float(input("Upper Limit:"))
n=int(input("Enter the value of n:"))   # n should be a multiple of 3
h=(b-a)/n

k=1
sum=0
while(k<n):
    x=a+k*h
    if(k%3==0):
        sum=sum+2*f(x)
    else:
        sum=sum+3*f(x)
    k=k+1  
Ia=((3*h)/8*(f(a)+f(b)+sum))    
print("Approx value of Integration:",Ia)
    


# In[ ]:




