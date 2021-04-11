# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 20:45:53 2021

@author: jin
"""

## 161-170
#%%
for i in range(100):
    print(i)

#%%
for i in range(2002, 2051, 4):
    print(i)
    
#%%
for i in range(1, 31):
    if i % 3 ==0:
        print(i)
        
#%%
for i in range(99,-1,-1):
    print(i)
    
#%%
for i in range(10):
    print(i / 10)

#%%
for i in range(1, 10):
    print( " 3x" ,i,"=", 3*i)

#%%
for i in range(1, 10):
    if i % 2 !=0:
        print( " 3x" ,i,"=", 3*i)
        
#%%
sum =0
for i in range(1,11):
    sum += i
print(sum)

#%%
sum =0
for i in range(1,11):
    if i %2 !=0:
        sum += i
        
    
print(sum)

#%%
mul =1;
for i in range(1,11):
    mul *= i
print(mul)
    
        
    