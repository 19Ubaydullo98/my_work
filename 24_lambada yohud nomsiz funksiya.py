# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 20:17:41 2024

@author: Ubaydullo
"""
###############        LAMBADA YOHUD NOMSIZ FUNKSIYA        ###################
"""Pythonning o'ziga xos xususiyatlaridan biri, nomsiz vaqtinchalik funksiyalar 
yaratish imkoniyati. Bunday funksiyalarni yaratishda def operatori o'rniga 
lambda operatori ishlatilgani uchun ham lambda funskiyalar deb ataladi.     """

# Nomsiz funksiyalar quyidagicha yaratiladi:

#    Nomsiz funksiyalar quyidagicha yaratiladi:
    
#Lambda funksiyalari istalgan miqdordagi argumentlarga ega bo'lishi mumkin, ammo
#funksiya badanida faqat bitta ifoda mavjud bo'ladi. Ifoda bajariladi va qaytariladi
#(return operatori shart emas).
#Nomsiz funksiyalar biror ifodani tezda hisoblab olishda qulay. Misol uchun 
#quyidgai lambda funksiya ikkita argument qabul qiladi.  (pi,r), va aylana uzunligini qaytaradi:
import math 
# def nom(argument):
#     return ifoda
#  lambda argument : ifoda  bu yerda defning o'rniga lambada qo'yiladi yoniga argument yoziladi
                       # ^ bu yerda return shart emas ifodani o'zi tashqariga qaytaradi 
                       # argumentlar soni cheklangmagan quyidagicha: !
# lambada argument1, argument2 : ifoda = argument1 + argument2 
# misollar ko'raylik 
uzunlik = lambda pi, r : 2*r*pi
print(uzunlik(math.pi,10))

kvadrat = lambda x, y : x**y 
print(kvadrat(20,2))
# savol tu'g'ilishi aniq hozir biz lambda nomsiz funksiya deb aytdingiz lekin siz unga nom beryapmiz
# biz uni aslida qayerda ishlatamiz misol uchun :
################################ funksiyadan yana funksiyayasash 
def daraja(n):
    return lambda x: x**n  #biz daraja funksiyasidan yana 2 ta funksiya yasadik 

kvadrat  = daraja(2)
print(kvadrat(9))

kub = daraja(3)
print(kub(6))
print(f"2 ning kvadrati {kvadrat(2)} ga teng.")

print(f"3 ning kubi {kub(3)} ga teng.")
############################# ##########  MAP() FUNKSIYASI 
'''BU FUNKSIYA ARGUMENT SIFATIDA RO'YHAT (YOKI LUG'AT) VA BOSHQA BUR FUNKSIYA
QABUL QILIB, RO'YHAT ELEMENTLARIGA QABUL QILINGAN FUNKSIYA YORDAMIDA ISHLOV BERADI.
QUYIDAGI MISOLNNI KO'RAMIZ '''
from math import sqrt 
numbers = list(range(11)) # o dan 100 gacha sonlar ro'yxati 
ildiz = list(map(sqrt,numbers))## bunda map ikkita argument qabul qilyapti sqrt funksiyasi 
# va numbers degan ro'yhat --> map funksiyasi numbersdan sonlarni qaabul qiladida 
# ildizini chiqarib list orqali ro'yhat yasaydi 
print(ildiz) 
""" Agar biz map dan foydalanmagan holatda buni yozmoqchi bo'lsak quyidagicha 
uzunroq yo'ldan ketgan bo'lardik  """
ildiz = []
for son in numbers:
    ildiz.append(sqrt(son)) ## shu kabi funksiyadan foydalangan bo'lar edik 
#################################### keling endi numbersning darajalirini yasaylik 
def daraja2(x):
    """daraja qaytaradigan funksiya """
    return x*x
print(daraja2(6)) # funksiyamiz ishladi 
daraja = list(map(daraja2,numbers))   # huddi shu tarzda ishlasak soddaroq 
print(daraja)
#####  Aslida lambda orqali bundanda soddaroq ko'rinishga keltirsak bo'ladi 
 ### bu yerda  kodimiz nomi yo'q bo'ldi nomsiz bo'ldi 
kvadrat = list(map(lambda x: x*x , numbers))  ### eng sodda ko'rinishlaridan bir turi 
print(kvadrat)     ##### ^ bu yerda lambda funksiyasini beryapmiiz 
####################### yana buni dexqonchasiga ishlamoqchi bo'lsak quyidagicha bo'ladi 

kvadrat = []
for son in numbers:
    kvadrat.append(son*son)  ### shunaqangi uzun kod yozishimiz kerak bo'lar ekan 
print(kvadrat)
######################################  Ikki ro'yhatni elementlarini bir biriga qo'shish 
a =[3,5,10]
b= [4,6,46]
summa = list(map(lambda x,y : x+y, a,b))
print(summa)  
# natija:  [7, 11, 56]    lambda x,y qiymatni  a va b variabledan qabul qiladi va ularni bir biriga qo'shadi. 
############################### filter funksiyasi 
import random as r 
numbers = r.sample(range(100), 10) # 0 dan 99 gacha sonlar ichidan ixtiyoriy 10 ta son tanlab oladi
def juft(son):
    """sonlar qabul qilib juft yoki toqligini aniqlab beruvchi funksiya """
    return son%2==0

juft_son = list(filter(juft, numbers))
print(numbers)# ixtiyoriy 10 ta son 
print(juft_son) # bu faqat juft sonlarni qabul qilib oladi 
########## shunday holatlarda lambda funksiyasidan foydalanganimiz avzal 
juft_son = list(filter(lambda x: x%2==0, numbers))   # bu ko'rinishi qulayroq 
print(juft_son)
########################################### filter funksiyasidan matnlar bilan 
# ishlash uchun ham ishlatamiz 
fruit = ['apple','apricot','peach','pineapple','poegranate','grape','watermelon','melon','banana']
meva = 'a'
other_fruit = list(filter(lambda x: x.startswith(meva),fruit))
print(other_fruit) # bu metod orqali biz qaysidir so'zning bosh harfi ma'lum bir harfdan boshlangan so'zlarni saralab beradi

## quyidagi funksiyamizda so'zdagi harflar soni 5 tagacha bo'lgan so'zlarni chiqaradi 
fruit_2 = list(filter(lambda meva: len(meva)<=5, fruit))
print(fruit_2)
    
#### quyidagi funksiyamiz so'zning bosh va oxirgi harfi ma'lum harflar bilan tugagan so'z chiqaradi 
meva = list(filter(lambda meva:meva.startswith('p') and meva.endswith('e'),fruit))
print(meva)

    




