# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 20:50:12 2023

@author: Ufbaydullo-PC
"""
'''                   NESTING
Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yoki boshqa lug'atni, 
yoki aksincha ro'yxat ichida lug'atni saqlash ham qo'l kelishi mumkin. Bu ingliz 
tilida Nesting deyiladi, bir narsani ichida bir narsa saqlash, misol uchun 
Kitob ichida bo'limlar bor, bo'limlar ichida ham boblar boblar ichida betlar bor 
va  hokazo...... Nesting Pythondagi foydali xususiyatlardan biri.
Keling, bunga bir nechta misollar ko'ramiz.                      '''
###############################################
'''                      LUG'ATLAR RO'YXATI
Biz avvalgi darsimizda talabalarning ma'lumotlarini lug'at shaklida saqlashni 
ko'rgan edik. Shunday talabalardan yuzlab bo'lganda, ularning har biriga alohida
lug'at qilishimiz tabiiy, lekin bu lug'atlar bilan ishlash qiyinchilik tug'dirishi 
mumkin. Shunday xolatda barcha lug'atlarni (talabalarni) bitta ro'yxatga joylab, 
ular ustida turli amallar bajarish mumkin.

Kelin quyidagi misolni ko'ramiz, bazamizda bir nechta mashinalar bor. Har bir 
mashina alohida lug'at shaklida. '''

car_1 ={
       'model':"nexia",
       'colour': "white",
       'year': 2013,
       "cost": 6800,
       "km": 50000,
       'karobka': "mehanika"
       }

car_2 ={
       'model':"matiz",
       'colour': "grey",
       'year': 2015,
       "cost": 6000,
       "km": 70000,
       'karobka': "mehanika"
       }

car_3 ={
       'model':"spark",
       'colour': "moykriy",
       'year': 2017,
       "cost": 7000,
       "km": 50000,
       'karobka': "avtomat"
       }

#Agar biz har bir lug'atga alohida murojat qiladigan bo'lsak, lug'atlarning 
#nomlarini yodlab qolishimiz talab qilinar edi:
car = car_1 
print(f"{car['model'].title()}, "          # bu qator tashlab yozishning yana 
      f"{car['colour'].title()}, "         # bir usuli 
      f"{car['year']}, {car['cost']}$")

car = car_2 
print(f"{car['model'].title()}, "
      f"{car['colour'].title()}, "
      f"{car['year']}, {car['cost']}$")

car = car_3 
print(f"{car['model'].title()}, "
      f"{car['colour'].title()}, "
      f"{car['year']}, {car['cost']}$")
# har bir moshinani chiqarishimiz uchun yuqridagiga o'xshab kodimiz kattalashib ketadi.

#Keling barcha avtolarni bitta ro'yxatga joylaymiz, va for tsikli yordamida
#birma-bir konsolga chiqaramiz:
cars = [car_1, car_2, car_3]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['colour'].title()}, "
          f"{car['year']} - yiln, {car['cost']}$")
    
print(cars) # bizda 3 ta lug'at bor edi biz ularni bitta ro'yhatga joyladik.
# biz har bir lug'atga murojat qilmoqchi bo'lsak ro'yhatnni indexni berish usulidan foydalanamiz:
print(cars[0])

#Biror lug'atdagi elementga murojat qilish uchun esa quyidagi usuldan foydalanishimiz mumkin:
print(cars[0]['colour'])
print(cars[2]['model'])

print(f"{cars[0]['colour'].title()} "
      f"{cars[0]['model'].title()}")

print(
      
      
      
      
      
      
      
      )
print('salom')




    