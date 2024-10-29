0# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 20:09:07 2023

@author: Ubaydullo-PC
"""

#  for BILAN TANISHAMIZ
#Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab 
#etilishi mumkin. Misol uchun, ro'yxat ichidagi har bir elementni alohida qatordan
#konsolga chiqarish, yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo. 

mehmonlar = [ "vali", "Umid", "homid", "karim","jasur"]
#hammasiga salom berib chiqishimiz mumkin 
print("Salom", mehmonlar[0].title())
print("salom", mehmonlar[1].title())
print("salom", mehmonlar[2].title())
print("salom", mehmonlar[3].title())

#Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu 
#tsikl (loop) deb ataladi. 
#Keling quyidagi misolni ko'ramiz. Bizda mehmonlar ro'yxati bor, biz har bir 
#mehmonning ismini yangi qatordan chiqarmoqchimiz. Buning uchun quyidagi kodni 
#yozamiz:
    
for mehmon in mehmonlar:
    print("Salom", mehmon)  #bu for tsiklning bodysi deyiladi 
    print("hayr", mehmon)
"""   
#Keling, kodni tahlil qilaylik. 
1-qatorda biz mehmonlar degan ro'yxat yaratdik va uni mehmonlarning ismi bilan
 to'ldirdik.
2-qatorda for tsiklini bohladik. Bu qator Pythonga mehmonlar degan ro'yxatdan
har bir elementini olib uni yangi, mehmon degan o'zgaruvchiga yuklashni buyuryapti
(o'zgaruvchiga istalgan nom berishingiz mumkin. Biz tushunarli bo'lishi uchun
 mehmon deb atadik)
3-qatorda biz mehmon degan o'zgaruvchining qiymatini konsolga chiqardik. Bu 
tsikl to mehmonlar ro'yxatida elementlar tugagunga qadar takrorlanadi.
"""
    
#For" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.
'''
for QANDAY ISHLAYDI
Keling yana bir misol ko'raylik. 
'''
classmate =['anvar','dilmurod', 'shavkatjon','temur', 'qobiljon', 'hayotbek']
for dost in classmate:
    print(f"Hurmatli {dost.title()} sizni 18-noyabr kuni to'yga taklif qilamiz")
    print("Hurmat bilan Mamatovlar oilasi")
    
    
"""Yuqoridagi kodda 2-qator bu tsikl boshi deyiladi. Aynan shu qator kodimiz nech 
marta takrorlanishini aniqlaydi. Bizning holatimizda tsikl mehmonlar ro'yxati
ichidagi elementlar tugagunga qadar takrorlanadi. Tsikl boshlanishi ikki nuqta
 (:) bilan tugaydi. Undan keyingi 3 va 4-qatorlar bu tsiklning badani deyiladi.  
 ###################
 Tsikl badani surilish (indentation) bilan ajratiladi, ya'ni tsiklning takrorlanuvchi
 qismi asosiy koddan bir muncha o'ngroqqa surilgan bo'ladi. Agar biz mana shu surilishni
 tark qilsak kodimiz xato beradi:
"""
classmate =['anvar','dilmurod', 'shavkatjon','temur', 'qobiljon', 'hayotbek']
for dost in classmate:
#print(f"Hurmatli {dost.title()} sizni 18-noyabr kuni to'yga taklif qilamiz")
    print("Hurmat bilan Mamatovlar oilasi")
"""
Natija: IndentationError: expected an indented block"""

#Shunigdek, ko'pchilik yo'l qo'yadigan yana bir xato, qo'shimcha qatorlarni surish esdan chiqishi:
classmate =['anvar','dilmurod', 'shavkatjon','temur', 'qobiljon', 'hayotbek']
for dost in classmate:
    print(f"Hurmatli {dost.title()} sizni 18-noyabr kuni to'yga taklif qilamiz")
print("Hurmat bilan Mamatovlar oilasi")   
# Natijada qo'shimcha qator for tsikldan tashqarida bo'lib qoladi natijani ko'raylik

# Yoki aksincha quyidagicha bo'lsa tsikl beshinchi qatorni o'ziniki deb qabul qiladi 
classmate =['anvar','dilmurod', 'shavkatjon','temur', 'qobiljon', 'hayotbek']
for dost in classmate:
    print(dost)
    
 
    print(classmate)# bu kod tsikldan tashqarida edi 

# aslida to'g'ri kod quyidagicha 
classmate =['anvar','dilmurod', 'shavkatjon','temur', 'qobiljon', 'hayotbek']
for dost in classmate:
    print(dost)
print(classmate)# bu kod tsikldan tashqarida edi 


#for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
#Keling quyidagi misolni ko'ramiz

number = list(range(1,12))# bu yerda 1 dan 11 gacha son paydo bo'ladi 
print(number)

for son in number:
    print(f"{son}ning kvadrati {son**2}ga teng")

#for yordamida yangi ro'yxat ham shakllantirish mumkin:

raqam = list(range(1,11))
kvadrat =[]  # BO'SH RO'YHAT YARATAMIZ 
for son in raqam:
    kvadrat.append(son**2)
print(kvadrat)

"""   
for va input()0
for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan 
qiymatlar bilan to'ldirish mumkin: 
"""
friend = []
num = list(range(5))
for n in num:
    friend.append(input(f" {n+1}-do'stingizni kiriting:" ))

print(friend)

friends = []
print('Beshta eng yaqin do\'stingizni kriting') 
for n in range(5):  #bu yerda range orqali 5 ta son yaratib oldik 
    friends.append(input(f" {n+1}  - do'stingizni kriting>>>\n")) # {n+1} range 0dan boshlagani uchun 1 ni qo''shib chiqaryapmiz 
    
# KODNI TAHLIL QILISH 


######################################
# AMALIYOT

qarindosh = ['anvar', 'sanjar', 'halima', 'zilola', 'farhod']
for n in qarindosh:
    print(f"Hurmatli {n} birodar sizni 2-oktyabr tug'ilgan kunga kelishizni so'raymiz")
print(f"Kod {len(qarindosh)} marta takrorlanadi")
    
sonlar = list(range(11,100,2))
print(sonlar)
for i in sonlar:
    print(f"{i} sonining kubi {i**3} ga teng")
    
    
cinema = []
for k in range(5):
    cinema.append(input(f"{k+1} - sevimli kinoyingizni kiriting:  "))

#print(f"siz eng sevimli kinolaringiz quyidagilar: ",cinema)

dialog =input( f"siz kecha necha kishi bilan suhbat qurdiz: ")
suhbat = []
for soni in range(int(dialog)):
    suhbat.append(input(f"{soni + 1} - suhbat qurgan insoningiz kim edi: "))

    
print(suhbat)



