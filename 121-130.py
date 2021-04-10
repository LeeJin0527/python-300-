# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:08:27 2021

@author: jin
"""

## 121-130
#%%
user = input(">> ")
if user.islower():
    print(user.upper())
    
else:
    print(user.lower())
#%%
user = int(input("score: "))

if ( 81 <= user <= 100):
    grade = "A"
    
elif (  61 <= user <= 80):
    grade = "B"
    
elif ( 41 <= user <= 60):
    grade = "C"
elif( 21 <= user <= 40):
    grade = "D"
else:
    grade = "E"
print("grade is ",grade)

#%%
환율 = { "달러" : 1167,
      "엔" : 1096,
      "유로" : 1268,
      "위안" : 171}

user = input(">>입력: ")
num, currency = user.split()
print(float(num) * 환율[currency] ,"원")

#%%

user1 = int(input("input number1: "))
user2 = int(input("input number2: "))
user3 = int(input("input number3: "))

print(max(user1, user2,user3))
#%%
user = input(">> 휴대전화 번호 입력:: ")
if (user[0:3] =="011"):
    tong = "SKT"
elif(user[0:3] =="016"):
    tong = "KT"
elif(user[0:3] =="019"):
    tong = "LGU"   
else:
    tong = "알수없음"
    
print("당신은", tong ,"사용자 입니다 ")

#%%

user = input(">> 우편번호:")

if (user[2] == "0") | (user[2] == "1")|( user[2] == "2"):
    gu = "강북구"
    

elif (user[2] == "3") | (user[2] == "4")|( user[2] == "5"):
    gu = "도봉구"

elif (user[2] == "6") | (user[2] == "7")|( user[2] == "8") |( user[2] == "9"):
    gu = "노원구"
    
print(gu)

#%%

user = input(">> 주민등록번호:")  
# print(user.split("-")[1][0])

if((user.split("-")[1][0]  =="1") | (user.split("-")[1][0]  =="3")):
    print("남자")
elif((user.split("-")[1][0]  =="2") | (user.split("-")[1][0]  =="4")):
    print("여자")
    
#%%

user = input(">> 주민등록번호:")  

if((0 < int(user.split("-")[1][1:3])  ) <=8):
    print("서울입니다")
else:
    print("서울이 아닙니다 ")
    
#%%
num = input(">> 주민등록번호:")  

계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
#%%
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
print(btc)

변동폭 =float(btc['max_price']) - float(btc['min_price'])
if (float(btc['opening_price']) + 변동폭 > float(btc['max_price'])):
    print("상승장")
else:
    print("하락장")





    
 


