# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:09:51 2021

@author: jin
"""

#%% 131-140
#%%
과일 = ["사과" , "귤", "수박"]
for 변수 in 과일 : 
    print(변수)
    
#%%
과일 = ["사과" , "귤", "수박"]
for 변수 in 과일 : 
    print("#####")
    
#%%
for 변수 in ["A", "B", "C"]:
    print(변수)
#%%
i = 0
while( i < 3):
    print(chr(65 + i))
    i = i+1
    
#%%
print("출력:" ,"A")
    
print("출력:", "B")
print("출력:", "C")

#%%
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)
  
#%%
변수 = "A"
b = 변수.lower()

print("변환:" ,b)
변수 = "B"
b = 변수.lower()  
print("변환:", b)
변수 = "C"
b = 변수.lower()
print("변환:", b)
#%%
for i in range(3):
    print( 10 * (i+1))
    
#%%
for i in [10,20,30]:
    print(i)
    
#%%
for i in range(3):
    print( "print(" + str(10 * (i+1)) +")")
    
#%%
for i in range(3):
    print( 10 * (i+1))
    print("==========")
    
#%%
print("-------")
for i in range(3):
    print( 10 * (i+1))
    
#%%
for i in range(4):
    print("--------")
    






