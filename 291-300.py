# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
##
#%%291 -300
f = open("C:/Users/01/Desktop/새 폴더/a/매수종목1.txt", mode = "wt", encoding = "utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420\n")

f.close()

#%%

f = open("C:/Users/01/Desktop/새 폴더/a/매수종목2.txt", mode = "wt", encoding = "utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")

f.close()
#%%
import csv 

f = open("C:/Users/01/Desktop/새 폴더/a/매수종목.csv" ,mode ="wt", encoding="cp949",newline='' )
writer = csv.writer(f)

writer.writerow(["종목명", "종목코드","PER"])
writer.writerow(["삼성", "005930",15.59])
writer.writerow(["네이버", "035420",10])
f.close()

#%%
f = open("C:/Users/01/Desktop/새 폴더/a/매수종목1.txt", encoding ="utf-8")
lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()
    codes.append(code)
    
print(codes)
f.close()

#%%
f = open("C:/Users/01/Desktop/새 폴더/a/매수종목2.txt", encoding ="utf-8")
lines = f.readlines()

data ={}
for line in lines:
    line = line.strip()
    k, v = line.split()
    data[k] =v
    
print(data)
f.close()
#%%
per =["10.31","","8.00"]

for i in per:
    try:
        print(float(i))
        
    except:
        print(0)
        
#%%
per = ["10.31", "", "8.00"]
answer =[]
for i in per:
    try:
        answer.append(float(i))
    except:
        print(0)
print(answer)

#%%
try:
    b = 3/0
except ZeroDivisionError:
    print("0으로 나누면 안돼요")
    
#%%

data = [1, 2, 3]
for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)
        
#%%
per = ["10.31"," ","8.00"]
for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환완료")
       