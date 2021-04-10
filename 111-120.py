# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:46:44 2021

@author: jin
"""

#%%
#111-120
#%%
user = input(">> ")
print(user * 2)

#%%
user = int(input("숫자를 입력하세요: "))
print(user + 10)

#%%
user = int(input(">> "))
if (user % 2 ==0 ):
    print("짝수")
else:
    print("홀수")
    

#%%
user= int(input("입력값 : "))
output = user + 20 
if (output > 255 ):
    print("255")
else:
    print(output)
    
#%%
user= int(input("입력값 : "))
output = user - 20 
if (output > 255 ):
    print("255")
elif ( output < 0 ):
    print("0")
else:
    print(output)
#%%

user = input("현재시간 : ")
if ( user[-2:] == "00"):
    print("정각입니다")
else:
    print("정각이 아닙니다")
    
    
#%%
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은? ")
if(user in fruit):
    print("정답입니다")
    
#%%
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "Samsung", "LG"]

user = input(">> ")
if user in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")
    

#%%
fruit = {"봄" : "딸기" , "여름": "토마토", "가을" :"사과"}
user = input(">> 좋아하는 계절은 : ")
if user in fruit.keys():
    print("정답입니다")
    
#%%

fruit = {"봄" : "딸기" , "여름": "토마토", "가을" :"사과"}
user = input(">> 좋아하는 과일은 : ")
if user in fruit.values():
    print("정답입니다")
else:
    print("오답입니다")



