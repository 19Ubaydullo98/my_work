# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:35:12 2023

@author: Ubaydullo-PC
"""
"""
# if else shartlari va tarmoqlanish 
TARMOQLANISH
Shu vaqtgacha yozgan dasturlarimizga e'tibor bersangiz, dasturimiz yuqoridan pastga 
qarab qatorma-qator bajarilib keldi. Bu chiziqli dastur deyiladi. Voqelikda esa 
aksar dasturlar ma'lum bir shart bajarilishi (yoki bajarilmaganiga) ko'ra kodning 
bir qismidan boshqa qismiga "sakrab" o'tishi tabiiy hol. Dasturlashda bu tarmoqlanish deb ataladi. 

if OPERATORI
if so'zi ingliz tilidan "agar" deb tarjima qilinadi va deyarli barcha dasturlash tillarida shartlarni yozish uchun foydalaniladi. 
Keling quyidagi misolni ko'ramiz. Bizda avtolar ro'yxati bor:
"""
cars = ['mers', 'limuzin', 'bmw', 'rols roys', 'toyota']
for moshin in cars:
    print(moshin.title())
""" Mers
 Limuzin
 Bmw      # bu yerda Bmw moshinasi BMW ko'rinishida chiqisi kerak edi 
 Rols Roys
 Toyota    """# mana endi bizga if operatori kerak quyidagicha 
 ###  == bu belgi tengmi deb so'raydi 
for car in cars: # carsning ichidagi har bir moshina uchun 
     if car == 'bmw': # agar car  'bmw ga teng bo'lsa 
         print(car.upper()) # car nomini hammasini katta harfda chiqar degani bo'ladi 
     else:  # aks holda.....
         print(car.title()) # carning faqat birinchi harflarini kattada chiqaradi 
#Diqqat! Shart "badani" shartdan biroz o'ngga surib yoziladi (huddi for tsikli kabi).
#if/else dan keyin kelgan va o'ngga surib yozilgan har bir qator if/else shartining
#badani hisoblanadi.

""" agar biz carni ko'radigan bo'lsak 
print(car)
toyota 

car == 'bmw'
Out[16]: False   # yuqorida carni nimaga tengligini ko'rdik shunga false = yo'g'on , yo'q degan javob qaytaryapti 

car == 'toyota ' # car toyotaga teng bo'lgani uchun true = rost , ha deb javob qaytaryapti
Out[17]: True

a = 10  # a ni 10 ga teng deb oldikda uni tekshirib ko'ramiz 

a == 10 # a yimiz 10 tengmi deyapmiz bizga true = rost , ha deb javob qaytaryapti 
Out[19]: True

a == 5 # a yimiz  5 ga tengmi deyapmiz bizga false = yolg'on , yo'q deb qaytaryapti 
Out[20]: False

####################
a = 'Ali' a= bosh harfi katta bilan boshlangan 'Aliga tenglab oldik'

a == "Ali"
Out[22]: True   ## bu yerda to'g'ri deb chiqaryapti 

a == "ali"  ## bosh harfi kichkina bilan boshlangan aliga tenglab oldik 
Out[23]: False  ## dastur esa bizga hato javob chiqardi chunki
                ##  ali  tengmas Aliga teng emas ikkalasi ham boshqa boshqa 

"""
###############################################################################
"""
MATNLARNI SOLISHTIRISH
Aksar tizimlar foydalanuvchi kiritgan matnni ma'lum bir ko'rinishga keltirib oladi.
 Buning sababi, kompyuter uchun 'Ali', 'ALI', va 'ali' bu uchta turli hil ism. Ularni
 solishtirish uchun esa bir ko'rinishga keltirib olish kerak.
 
 
Tasavvur qiling siz yangi email manzil ochmoqchisiz, va o'zingizga yangi foydalanuvchi
ismini tanlashingiz kerak. Kompyuter siz kiritgan foydalanuvchi ismini tizimdagi
 mavjud foydalanuvchilar bilan solishtiradi va agar ism band bo'lsa sizga boshqa
 ism tanlashni aytadi. Solishtirish jarayonida esa, siz tanlagan ismni kichik harflarga
 o'tkazib, boshqa ismlar bilan solishtiradi.
 
 #########
 siz biror saytdan registratsiyadan o'rtayotganingizda sizga shunaqa narsalar so'raladi
 
 ism :
     Ubaydullo
 familya :
     Obidjanov 
     
     
yangi login yarating "Ubaydullo" logini band etilgan deb javob qaytariladi 


buni sababi shuki ko'p tizimlarda 
'Ubaydullo', 'ubaydullo', 'UBaydullo', 'UBAYDULLO' tulli ko'rinishdagi loginlarni 
.lower() metodi orqali bir hil ko'rinishga olib kelib keyin tekshiradi va rad qiladi 
misol uchun ko'ramiz 

name = 'Vali'

name.lower() == 'vali'   # deb so'rasak bo'ladi 

name = "Vali"

name.lower() == "vali"
Out[27]: True   # true = rost deb chiqarib beradi  



 """
""" QIYMATLARNING TENG EMASLIGINI TEKSHIRISH
Agar ikki qiymatning teng emasligini tekshirish talab qilinsa, != operatoridan foydalanilamiz. 

son = 7

son == 7
Out[33]: True

son ==6
Out[34]: False

son !=6   # bunda yuqorida haqiqatdanda son 6 tengmas , sonning qiymati 7 deganmizz
Out[35]: True

son !=7
Out[36]: False
"""


ism = input("Ismingizni kiritin>> ") # foydalanuvchidan ism kritishni so'rayapmiz 
if ism.lower() != 'islom':
    print(f"Kechirasiz {ism.title()}, biz Islomni kutayapmiz!") 
else:
    print(f"Salom {ism.title()}")
    
#shartlarda else qismi bo'lishi majburiy emas. Bunga keyingi bo'limlarda
#tushunarliroq misollar ko'ramiz.
"""
SONLARNI SOLISHTIRISH
Sonlarni solishtirishda yuqoridagi teng (==) va teng emas (!=) shartlariga
 qo'shimcha ravishda quyidagi mantiqiy shartlar ham qo'shiladi:
     
     
Kichik: a<b
Kichik yoki teng: a<=b
Katta: a>b
Katta yoki teng: a>=b
"""
random_son = float(input("32x2 nechiga teng: "))
if random_son != 64:
    print("JAVOB HATO ")
    
    
age = float(input("Yoshingiz nechida>>> "))
if age >= 18:
    print("siz bu saytga kirishingiz mumkin")
else:
    print("Kirish mumkin emas")

"""
age
Out[47]: 22.0

age>18
Out[48]: True

age <=18
Out[49]: False
"""

login = input("login yarating: ")
if len(login) <= 5 :
    print('Login 5 belgidan uzun bo\'lishi kerak')

#Sonlarni solishtirishda arifmetik ifodalar ham yozishimiz mumkin:                    
yil = float(input(" ILtimoz tug'ilgan sanangizni kriting>>> "))
if 2023-yil <= 18:
    print(f"Yoshingiz {2023-yil} da ekan \nKirishingiz mumkin emas!")
else:
    print("Hush kelibsiz")
    
    
yosh = float(input("Yoshingiz nechida: ")) 
if yosh < 60:   print('Siz pensionaerlar guruhida ekansiz') 
x, y = 25, 50 # x=25 va y=50
print("x>y") if x>y else print("x<y")
"""
x, y = 15, 12
print('x>y') if x>y else print('x<y')
"""



#########################################################
# Amaliyot 

car  = ['toyota', 'hundayi', 'gm', 'tesla']
for c in car:
    if c == 'gm':
        print(f"{c.upper()}")
    else:
        print(c.title())
##################################################        
car  = ['toyota', 'hundayi', 'gm', 'tesla']
for c in car:
    if c != 'gm':
        print(f"{c.upper()}")
    else:
        print(c.title())
######################################################
login = input('Yangi login yarating: ')

if login.lower() != 'admin':
    print(f"Hush kelibsiz {login.title()}!")
else:
    print("Hush kelibsiz, Admin. Foydalanuvchilar ro'yhatini ko'rasizmi?")
#######################################################

one_n = float(input("Birinchi sonni kiriting: "))
two_n = float(input("Ikkinchi sonni kiriting: "))
if one_n == two_n:
    print("Sonlar teng ")
    
###########################################################
ran_son = float(input(f"Ixtiyoriy son kiriting "))
if ran_son < 0:
    print("Siz kiritgan son manfiy son")
else:
    print("Siz kiritgan son musbat")
    
###################################################################
one_n = float(input("Birinchi sonni kiriting: "))

if one_n < 0:
    print("Musbat son kiriting")
else:
    print("Siz kiritgan sonning ildizi: ",one_n**0.5)
    