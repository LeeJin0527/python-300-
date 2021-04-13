#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 01:23:41 2021

@author: ijin
"""

##
##261-270

#%%
class Stock:
    pass

#%%
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code =code
        
삼성 = Stock ("삼성전자", "005930")
print(삼성.name)
print(삼성.code)

#%%
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code =code
    
    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)


#%%
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def set_code(self, code):
            self.code = code
        
        
            
a= Stock(None, None)
a.set_code("005292")
print(a.code)
#%%
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        
    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code
        
삼성 = Stock("삼성전자", "005361")
print(삼성.get_name())
print(삼성.get_code())

#%%
class Stock:
    def __init__(self, name, code, PER , PBR, 배수):
        self.name = name
        self.code = code
        self.PER =PER
        self.PBR =PBR
        self.배수 = 배수
        
        
        
    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code
    
#%%
class Stock:
    def __init__(self, name, code, PER , PBR, 배수):
        self.name = name
        self.code = code
        self.PER =PER
        self.PBR =PBR
        self.배수 = 배수
        
        
        
    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code
삼성 = Stock("삼성전자", "005361",15.79, 1.33, 2.83)      

#%%
class Stock:
    def __init__(self, name, code, PER , PBR, 배수):
        self.name = name
        self.code = code
        self.PER =PER
        self.PBR =PBR
        self.배수 = 배수
        
        
        
    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code  
    def set_per(self, PER):
        self.PER = PER
        
    def set_PBR(self, PBR):
        self.PBR = PBR
        
    def set_배수 (self,배수):
        self.배수 =배수

#%%
class Stock:
    def __init__(self, name, code, PER , PBR, 배수):
        self.name = name
        self.code = code
        self.PER =PER
        self.PBR =PBR
        self.배수 = 배수
        
        
        
    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code  
    def set_per(self, PER):
        self.PER = PER
        
    def set_PBR(self, PBR):
        self.PBR = PBR
        
    def set_배수 (self,배수):
        self.배수 =배수
        
삼성 = Stock("삼성전자", "005361",15.79, 1.33, 2.83)      
삼성.set_per(12.75)
print(삼성.PER)

#%%
class Stock:
    def __init__(self, name, code, PER , PBR, 배수):
        self.name = name
        self.code = code
        self.PER =PER
        self.PBR =PBR
        self.배수 = 배수
        
        
        
    def get_name(self):
        return self.name
        
    def get_code(self):
        return self.code  
    def set_per(self, PER):
        self.PER = PER
        
    def set_PBR(self, PBR):
        self.PBR = PBR
        
    def set_배수 (self,배수):
        self.배수 =배수
종목 = []      
삼성 = Stock("삼성전자", "005361",15.79, 1.33, 2.83)  
현대 = Stock("현대", "005375",8.70, 0.35, 4.27)  
LG = Stock("LG", "005378",317.34, 0.68, 1.37)

종목.append(삼성)
종목.append(현대)
종목.append(LG)
for i in 종목:
    print(i.code, i.PER)
    
    