# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:24:12 2021

@author: jin
"""

##191-200
#%%
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print( int(j) + int(j)*0.00014)
        
#%%
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print( int(j) + int(j)*0.00014)
    print("--------")
    
#%%
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for i in data:
    for j in i:
        result.append( int(j) + int(j)*0.00014)
print(result)

#%%
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

sub =[]
for i in data:
    result = []
    for j in i:
        result.append( int(j) + int(j)*0.00014)
    sub.append(result)
    
print(sub)
#%%
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    for j  in i[3:]:
        print(j)
        
#%%
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    for j in i[3:]:
        if j>=150:
            print(j)
            
#%%
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    for j in i[3:]:
        if j>=i[0]:
            print(j)
            
#%%
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

volatility =[]
for i in ohlc[1:]:
    volatility.append(i[1] -i[2])
    
    
        
print(volatility)

#%%
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    if i[0] < i[-1]:
        print(i[1] - i[0])
        
#%%
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
sum = 0
for i in ohlc[1:]:
    sum +=(i[0] -i[-1])
print(sum) 
        
        