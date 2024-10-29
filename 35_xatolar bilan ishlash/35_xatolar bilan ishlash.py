# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:43:44 2024

@author: Ubaydullo
Xatolikni ham o'zimizga bo'ysindirish"""  

age = input("Yoshingizni kiriting: ")
# age = int(age)
# print(f"Siz {2024-age} - yilda tug'ilgansiz.") # foydalanuvchi biron son kiritsa 
# yilni hisoblaydi biroq butunli son kiritsa 26.5 kabi 
#natija: ValueError: invalid literal for int() with base 10: '26.5'kabi hatolik beradi 
# odatda python bunday holatda python mahsus exception(istisno) obyekt yaratadi. 
# agar bu obyekt "tutib" olinmasa dastur bajarilishdan to'xtaydi 
# istisni obyektini tutib olish uchun pythonda maxsus try-exception operatoridan foydalanamiz.
# bu quyidagicha bajariladi!
try:
    age = int(age)  # bu hatolik beradigan kodimiz qatori
    # print(f"Siz {2024-age} - yilda tug'ilgansiz.")  # bu yerda yozishimiz aslida to'g'ri emas
except:
    print("Siz butun son kiritmagansiz!!!")
else:   # try to'g'ri bajarilsa pastdagi javob chiqadi
    print(f"Siz {2024-age} - yilda tug'ilgansiz.") 
    # bundan so'ng dasturimiz to'xtab qolmaydi keyingi kodga o'tib ketaveradi 
    # biz buna katta katta kodlar yozganimizda foydalanuvchi noto'g'ri ma'lumot kiritsa 
    # dasturimiz ishdan chiqmasdan ishlay boshlaydi.
print("dastur davom etayapti")
print("Dastur tugadi")

############################################################
try:
    age = int(age)
except ValueError: # endi qachonki ValueError bo'lganida kodimizdan javob qaytadi 
    print("Siz Butun son kiritmadingiz")  # aniq xatolikni beryapmiz
    
#masalan: Zerodivision
x,y = 5,4
# x/(y+1) # bu yerda hatolik zero divisionError bo'ladi
try:
    x/(y-4)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi. ")

# masalan: indexError
fruit = ["apple", "quince", "fig","apricot"]
try:
    print(fruit[5])
except IndexError:
    print(f"fruitda {len(fruit)} dona element bor holos")
# masalan: keyError
user = {
        "username": "ubaydullo",
        "status": 'admin',
        "email": "ubaydullo1940@gmail.com",
        "phone": "+998942750737"
        }
key = "pochta"
tel = "phone"
try:
    print(f"foydanaluvchi: {user[key]}")
except KeyError:
    print("Bunday kalit mavjud emas")
print(user[tel])

# # masalan: FileNotFindError
filename= "data.txt"
# with open(filename) as file:
#     file = file.read()  # FileNotFoundError:
try:
    with open(filename) as file:
        file = file.read()
except FileNotFoundError:
    print("Bunday file mavjud emas")  # shu holatda dasturimiz to'xtamay ishlab ketaveradi.

###############################################################
import json
# ro'yhat fayllar:
talaba1 = {"ism":"ubaydullo", "familya":"Obidjanov","yosh":"26"}
talaba1_json = json.dumps(talaba1)

filename = "talaba1.json"

with open(filename, 'w') as file:
    json.dump(talaba1_json, file)

talaba2 = {"ism":"Ali", "familya":"Valiyev","yosh":"45"}
talaba2 = json.dumps(talaba2)
with open("talaba2.json","w") as file:
    json.dump(talaba2, file)
    
talaba4 = {"ism":"Vali", "familya":"qodirov","yosh":"36"}
talaba4 = json.dumps(talaba4)
with open("talaba4.json", "w") as file:
    json.dump(talaba4, file)

files = ["talaba1.json", "talaba2.json","talaba3.json","talaba4.json"]

for filename in files:
    try:
        with open(filename) as file:
            talabalar = json.load(file)
            talaba = json.loads(talabalar)
    except FileNotFoundError :
        print("Bunday fayl mavjud emas") # bu yerada biz hech narsa chiqarmasdan pass ni ham bermasak bo'laveradi
    else:
        print(talaba["ism"])

#################################################################
son = input("Son kiriting: ")
try:
    son = int(son)
    x = 50/son
except ValueError:
    print("Siz butun son kiritmadingiz.")
except ZeroDivisionError :
    print("0 sonini kiritib bo'lmaydi!!!")
else:
    print(f"x = {x}")
##########33333
################## 
# Buni if metodi orqali ham bajarsak bo'ladi masalan.
while True:
    yil  = input("Tug'ilgan yilingizni kiriting: ")
    if yil.isdigit():
        yil = int(yil)
        break
    else:
        print("siz to'g'ri ma'lumot kiritmagansiz!!!")
print(f"Siz {2024-yil} yoshdasiz ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    


























