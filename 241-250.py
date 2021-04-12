#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:53:45 2021

@author: ijin
"""

##241 -250
#%%

import datetime
now = datetime.datetime.now()
print(now)

#%%
import datetime
now = datetime.datetime.now()
print(type(now))

#%%
import datetime

now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days = day)
    date = now - delta
    print(date)
#%%
import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

#%%
import datetime

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret)

#%%
import time
import datetime


while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)
    
#%%
import os
ret = os.getcwd()
print(ret, type(ret))

#%%
import os
os.rename("/Users/ijin/Desktop/git/untitled5.py","/Users/ijin/Desktop/git.241-250.py")

#%%
import numpy 
for i in numpy.arange(0, 5, 0.1):
    print(i)
    
    
    
    