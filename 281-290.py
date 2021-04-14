#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:55:07 2021

@author: ijin
"""

##
#281- 290
#%%
class Car:
    def __init__(self, tire, price):
        self.tire = tire
        self.price = price
        
car = Car(2, 1000)
print(car.tire)
print(car.price)

#%% 차 클래스 상속받은 자전차 클래스 생성
# class Car:
#     def __init__(self, tire, price):
#         self.tire = tire
#         self.price = price
        
# class ByCar(Car):
#     pass

#%%
class Car:
    def __init__(self, tire, price):
        self.tire = tire
        self.price = price
        
class ByCar(Car):
    def __init__(self, tire, price):
        self.tire = tire
        self.price = price

bicycle = ByCar(2, 100)
print(bicycle.price)

#%%

class Car:
    def __init__(self, tire, price):
        self.tire = tire
        self.price = price
        
class ByCar(Car):
    def __init__(self, tire, price , 구동계):
        super().__init__(tire, price)
        self.구동계 = 구동계
        
bicycle = ByCar(2, 100, "시마노")
print(bicycle.구동계)

#%%
class Car:
    def __init__(self , tire, price):
        self.tire  = tire
        self.price = price
        
class 자동차(Car):
    def __init__(self, tire , price):
        super().__init__(tire, price)
    def 정보(self):
        print("바퀴수 : {} 가격 :{}".format(self.tire, self.price))
        
car = 자동차(4, 1000)
car.정보()

#%%
class Car:
    def __init__(self, tire, price):
        self.tire = tire
        self.price = price
        
class 자전차(Car):
    def __init__(self, tire, price,name):
        super().__init__(tire, price)
        self.name =  name
    def 정보(self):
        print("바퀴수 : {} ".format(self.tire))
        print("가격 :{}".format(self.price))
        print("구동계: {}".format(self.name))
bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

#%%
class 부모:
    def 호출(self):
        print("부모호출")
class 자식(부모):
    def __init__(self):
            print("자식생성")
        
            
나 = 자식()

#%%
class 부모:
    def __init__(self):
        print("부모생성")
        
class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()
        
나 = 자식()
        
        