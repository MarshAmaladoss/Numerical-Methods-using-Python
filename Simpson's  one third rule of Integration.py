#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Simpson's 1/3 rule of Integration
def f(x):
        return 1/(1+x)
    
a=float(input("Enter the Lower Limit:"))    
b=float(input("Enter the Lower Limit:"))    
n=int(input("Enter the number of strips:"))

h=(b-a)/n
k=1
sum=0

while(k<n):
    x=a+k*h
    if(k%2==0):
        sum=sum+2*f(x)
    else:
        sum=sum+4*f(x)
    k=k+1    
Ia=(h/3)*(f(a)+f(b)+sum)    
print("Approx value of Integration:",Ia)
    


# In[ ]:




