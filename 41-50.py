#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:31:39 2021

@author: ijin
"""

##41-50
#%%
ticker ="btc_krw"
ticker_up = ticker.upper()
print(ticker_up)

#%%
ticker ="BTC_KRW"
ticker_down = ticker.lower()
print(ticker_down)

#%%
lower= 'hello'
upper = lower.capitalize()
print(upper)

#%%
file_name = "보고서.xlsx"
print(file_name.endswith(".xlsx"))

#%%
file_name = "보고서.xlsx"
print(file_name.endswith(".xlsx"))
print(file_name.endswith(".xls"))

#%%
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

#%%

a = "hello world"
a.split( )
print(a)

#%%
ticker = "btc_krw" 
new_ticker = ticker.split("_")
print(new_ticker)

#%%
date = "2020-05-01"
new_date = date.split("-")
print(new_date)

#%%

data = "039490     "
print(data.rstrip())