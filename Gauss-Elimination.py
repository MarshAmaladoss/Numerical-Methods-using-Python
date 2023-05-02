#!/usr/bin/env python
# coding: utf-8

# In[2]:


#8. Gauss Elimination method of solving simultaneous equations

import numpy as np
def gausselim(a,b):
    n=len(b)
    for k in range(0,n-1):
        for i in range (k+1,n):
            if a[i,k] != 0.0:
                l = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n]-l*a[k,k+1:n]
                b[i] = b[i]-l*b[k]
    for k in range (n-1,-1,-1):
        b[k] = (b[k]-np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

a = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]])  
b = np.array([11,-16,17])
print("The Solution is",gausselim(a,b))
            
        
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




