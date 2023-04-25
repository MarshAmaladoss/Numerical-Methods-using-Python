#!/usr/bin/env python
# coding: utf-8

# In[4]:


#9. Gauss Siedal Method of solving simultaneous equations
# 2x+y+z=5
# 3x+5y+2z=15
# 2x+y+4z=8

x=0
y=0
z=0
for i in range(7):
    print("Iteration",i+1)
    x=(5-y-z)/2
    y=(15-3*x-2*z)/15
    z=(8-2*x-y)/4
    
    print(x,y,z)
    print()




# In[ ]:




