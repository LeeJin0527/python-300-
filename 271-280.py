#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:45:00 2021

@author: ijin
"""
import random
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        self.account = str(num1) +"-" +str(num2) +"-" +str(num3)
account = Account("이진",100)
print(account.name)
print(account.bank)        

#%%

import random
class Account:
    ac =0
    def __init__(self, name, balance):
        
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        self.account = str(num1) +"-" +str(num2) +"-" +str(num3)
        Account.ac +=1
        #print(ac)
        
account = Account("이진",100)
print(Account.ac)
account = Account("이진",100)
print(Account.ac)

#%%
#클래스가 몇번 불리었는지 확인
import random 

class Account:
    account_count = 0 
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 +"-" +num2 +"-" +num3
        Account.account_count +=1
    @classmethod    
    def get_count_num(cls):
        print(cls.account_count)

kim = Account("김민수", 100)
lee = Account("이진", 100)
kim.get_count_num()
lee.get_count_num()

#%%
import random 

class Account:
    account_count = 0 
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 +"-" +num2 +"-" +num3
        Account.account_count +=1
        
    def deposit(self, amount):
        if amount >=1:
            self.balance += amount
            
            
    @classmethod    
    def get_count_num(cls):
        print(cls.account_count)
#%%
import random 
class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance 
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 +"-" +num2 +"-" +num3
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
    
    def display_info(self):
        print("은행이름: {}".format(self.bank))
        print("예금주: {}".format(self.name))
        print("계좌번호: {}".format(self.account))
        print("잔고: {}".format(self.balance))
        
        
                
            
account = Account("이진", 1000)
account.display_info()

#%%
import random
class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance 
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
    
    
#%%
import random 
class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance 
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 +"-" +num2 +"-" +num3
        
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
    
    def display_info(self):
        print("은행이름: {}".format(self.bank))
        print("예금주: {}".format(self.name))
        print("계좌번호: {}".format(self.account))
        print("잔고: {}".format(self.balance))
        
    def deposit(self, amount):
        if amount >=1:
            self.balance += amount
            Account.account_count += 1
        if (Account.account_count ==5):
            self.balance = self.balance * 1.01
        
                
            
account = Account("이진", 1000)
account.deposit(100)
account.deposit(100)
account.deposit(100)
account.deposit(100)
account.deposit(100)
print(account.balance)

#%%

import random 
class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance 
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 +"-" +num2 +"-" +num3
        
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
    
    def display_info(self):
        print("은행이름: {}".format(self.bank))
        print("예금주: {}".format(self.name))
        print("계좌번호: {}".format(self.account))
        print("잔고: {}".format(self.balance))
        
    def deposit(self, amount):
        if amount >=1:
            self.balance += amount
            Account.account_count += 1
        if (Account.account_count ==5):
            self.balance = self.balance * 1.01
data =[] 
k = Account("Kim", 10000)
l = Account("Lee", 100000)
p = Account("Park", 10)

data.append(k)
data.append(l)
data.append(p)

print(data)

#%%
for i in data:
    if(i.balance >=100):
        print(i.balance)
        
#%%
import random 
class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log =[]
        
        self.name = name
        self.balance = balance 
        self.bank = "SC은행"
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 +"-" +num2 +"-" +num3
        
    def withdraw(self,amount):
        if self.balance >= amount:
            self.withdraw_log.append(amount)
            self.balance -= amount
    
    def display_info(self):
        print("은행이름: {}".format(self.bank))
        print("예금주: {}".format(self.name))
        print("계좌번호: {}".format(self.account))
        print("잔고: {}".format(self.balance))
        
    def deposit(self, amount):
        if amount >=1:
            self.deposit_log.append(amount)
            self.balance += amount
            if self.deposit_count %5 ==0:
                    self.balance = self.balance * 1.01
                
          

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)
        
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)
            
            
account = Account("이진", 1000)
account.deposit(100)
account.deposit(200)
account.deposit(300)
#account.deposit(100)
#account.deposit(100)

account.deposit_history()

account.withdraw(100)
account.withdraw(20)
account.withdraw_history() 

#%%     
        

