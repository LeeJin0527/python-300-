#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 00:45:14 2021

@author: ijin
"""

##
#%%251- 260
#%%
#클래스, 객체, 인스턴스에 대해 설명해봅시다.
#객체(Object):
    # 개념: 소프트웨어 세계에 구현할 대상
    # 클래스에 선언된 모양 그대로 생성된 실체 
    
    # 특징: 클래스의 인스턴스 라고 부른다
    # 객체는 모든 인스턴스를 대표하는 포괄적인 의미를 갖는다 
    # oop의 관점에서 클래스의 타입으로 선언 되었을 때 객체 라고 부른다 
 
# 인스턴스(Instance):
#     개념: 설계도를 바탕으로 소프트웨어 세계에 구현된 구체적인 실체 
#     즉 , 객체를 소프트웨어에 실체화 하면 그것을 인스턴스 라고 부른다 
#     실체화된 인스턴스는 메모리에 할당된다
    
#     특징: 인스턴스는 객체에 포함된다고 볼 수 있다
#     ####중요 :oop의 관점에서 객체가 메모리에 할당되어 실제 사용될 때 인스턴스 라고 부른다 
#     추상적인 개념과 구체적인 객체 사이의 관계에 초점을 맞출 경우에 사용한다 
#     객체는 클래스의 인스턴스다 
#     객체간의 링크는 클래스 간의 연관 관계의 인스턴스다 
#     실행 프로세스는 프로그램의 인스턴스다

##클래스 , 객체, 인스턴스의 차이 
# 클래스는 '설계도' 객체는 '설계도로 구현한 모든 대상'을 의미한다

# 클래스의 타입으로 선언 되었을 때 객체라고 부르고 그 객체가 메모리에 할당되어 실제 사용 될때 인스턴스라고 부른다 
# 객체는 현실세계에 가깝고 인스턴스는 소프트웨어 세계에 가깝다 
# 객체는 실체 인스턴스는 관계에 초점을 둔다 
# 객체를 클래스의 인스턴스라고도 부른다 

#%%
class Human:
    pass

#%%
class Human:
    pass

areum = Human()

#%%
class Human:
    def __init__(self):
        
        print("응애응애")
    
areum = Human()

#%%
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age =age
        self.sex = sex

areum = Human("아름", 25, "여
자")
print(areum.name)
    
#%%
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        
areum = Human("아름", 25, "female")
print(areum.age)

#%%
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
        
areum = Human("아름", 25, "여자")
areum.who()

#%%
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름:{} 나이:{} 성별:{} " .format(self.name, self.age, self.sex))
        

    
        
    def setInfo(self , name, age, sex):
        self.name =name
        self.age = age
        self.sex = sex
        
areum = Human("불명", 0, "모름")
areum.who()

areum.setInfo("아름", 25, "여자")
areum.who()

#%%
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        
    def __del__(self):
        print("나의 죽음을 알리지 마라")
        
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
        
        
areum = Human("아름", 25, "여자")
del(areum)

#%%
class OMG :
    def print1(self) :
        print("Oh my god")


mystock = OMG()
mystock.print1()
 