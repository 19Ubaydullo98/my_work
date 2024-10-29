# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:42:24 2023

@author: Ubaydullo-PC
"""
""" pythonda lug'atlar katta bo'lishi mumkin kichkina bo'lishi mumkin, lug'at ichidagi
kalitlarni yoki qiymatlarni bilmasligimiz mumkin  mana shunday holatda 
bizga .ITEMS() METODI YORDAMGA KELADI QUYIDAGICHA ISHLATILADI                       """
talaba = {'ism':'Ubaydullo', 
          'familya':'obidjanov',
          'yosh':25,
          "fakultet":'komyuter injinering',
          'guruh':18104
          }
#print(talaba.items())
#####
#Bu metodni to'g'ridan-to'g'ri emas, for tsikli yordamida chaqirish orqali 
#lug'atdagi barcha elementlarni tushunarliroq shaklda ko'rishimiz mumkin.
for kalit,qiymat in talaba.items(): # for tsiklida biz bir emas ikki o'zgaruvchi yaratib oldik 
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}")

######### bu lug'atdagi ma'lumotni chiroylik qilib chiqaraylik
car = {   
       'dilmurod':'ferrari', 
       'Qobil':'nexia',
       'hayotbek':'tesla',
       'ahmadjon':'maskvich'
       }
for key, value in car.items():
    print(f"{key.upper()} {value} moshnasini minishni hoxlaydi!")
#########################33333333333333333333333333333333333333333333
"""                                      .keys() METODI
Agar lug'atdagi kalit so'zlarni ko'rish talab qilinsa, .keys() metodidan foydalanishimiz mumkin.
bizga kalit so'zinni o'zi kerak ;                        """
product ={
    "olma":"10000",
    'pomegranate': 25000,
    'quince': 12000,
    'banan': 18000,
    "apelsin":25000
    }
print(product.keys()) # bunda faqat kalit so'zlarni o'zi chiqadi holos 

for mahsulot in product.keys():# bunda keys orqali kalit so'zlarni mahsulotga yukladik
    print(mahsulot.title())
# lekin bun bizga KEY() metodisiz ham shundoq chiqaveradi 
for mahsulot in product:
    print(mahsulot.capitalize())
###############
bozorlik =['pomegranate', 'olma','quince','watermelon','melon','coconut']
for mahsulot in product:
    if mahsulot in bozorlik:
        print(f"{mahsulot} {product[mahsulot]} so'm.")
    else: 
        print("bizni bozorda bu mahsulot yo'q ")
#####
for buyum in bozorlik:
    if buyum not in product:
        print(f" Do'koningizga {buyum} ham olib keling!")
#############################################################################
'''                           LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
Pythonda lug'at elementlari siz (foydalanuvchi) kiritgan tartibda saqlanadi.
Agar lug'at elementlarini alifbo bo'yicha chiqarish talab qilinsa, sorted() funktsiyasidan foydalanamiz.'''
###
print(sorted(product.keys(  )))

print("there are many product in our market. They: ")
for mahsulot in sorted(product):
    print(mahsulot.title())
###########################################################################
'''                              .values() METODI
Agar lug'atdagi qiymatlarni chiqarish talab qilinsa .values() metodidan foydalanishimiz mumkin. '''

phone = {
    'ali': "redmi note 11 pro",
    'usmon': 'apple 15',
    'dili': "nony",
    'karim': 'galaxy s21',
    'olim': 'apple 15'
    }
print(phone.values())

print("our users applies  model of telephone following: ")
for user in phone.values():
    print(user.title())
##############
'''Yuqoridagi usul bilan qiymatlarni chiqrganimizda, lug'atdagi barcha qiymatlar
chiqib keladi. Agar, biror qiymat ko'p marta qaytarilsa, konsolga ham ko'p marta 
chiqib keladi.   Quyidagi misloni ko'raylik:               '''
phone = {
    'ali': "redmi note 11 pro",
    'usmon': 'apple 15',
    'dili': "nony",
    'karim': 'galaxy s21',
    'olim' : 'apple 15',
    'orif': 'galaxy s21',
    'jo\'ra': 'huawei',
    'hamid': 'galaxy s21'
    }

print("our users applies  model of telephone following: ")
for user in phone.values():
    print(user.title())
# natijada bir hil phone ishlatadigonlar ko'p chiqadi   
#Buning oldini olish uchun set() funktsiyasidan foydalanishimiz mumkin.

print("our users applies  model of telephone following: ")
for user in set(phone.values()):
    print(user.title(   ))

'''Pythonda set yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta 
elementlarni saqlashga mo'ljallangan. Lug'at va ro'yxatdan farqli ravishda,
 set ichidagi elementlar biror tartibda saqlanmaydi, va ularga indeks orqali 
 murojat qilib bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmaydi.     '''
# misol uchun:
car = {"ferrari","BMV","mers", 'Toyota', 'BMV', 'ferrari'}
print(type(car))
print(car) 
# natija:  {'ferrari', 'mers', 'Toyota', 'BMV'} bunda bir hillik yo'q 

#############################################################

py_tr = {
    'remave':"ro'yhatdan biror elementni  olib tashlash",
    'del': "indexini ko'rsatgan holatda olib tashlash",
    "pop": "ro'yhatdan sug'urib olish pop(index)",
    "sort()": " ro'yhatni tartiblash car.sort()",
    "sorted()": "ro'yhatga o'zgarish kritmasdan tartiblash ",
    "reverse=True": "teskari tartiblash uchun: sorted(o'zgaruvch,reverse =True)",
    "reverse()": "ro'yhatni teskari tartibblash.",
    "len" : "ro'yhat uzunligi",
    "list": "ro'yhat yaratish.",
    "range": "malum sonlar ketma-ketligini  yaratish"
    }
for key, value in py_tr.items():
    print(f"{key} - {value}")
    
capital = {
    "o'znbekiston":"toshkent",
    "qozog'iston" : "Ostana",
    "tojikiston" : "dushanbe",
    "turkmaniston": "Ashhabod",
    "Gruziya": "tbilisi",
    "Qirg'iziston": "Bishkek",
    "yaponiya": "tokio",
    "xitoy" : "pekin",
    "finlandiya" : "finland",
    "italiya": "rim"
    }
'''
print("Dunyo davlatlari:")
for country in sorted(capital.keys()):
    print(country.title())
print("dunyo davlari poytaxtlari:")
for cap in sorted(capital.values()):
    print(cap.title())'''
    
    
user = input("Qaysi davlatni poytaxtini bilishnni Hohlaysiz?: ")
for  poytaxt in capital:
    if user== poytaxt:
        print(f" {user.title()}ning poytaxti {capital[user].title()} shahri.")
poytaxt = capital.get(user)
if poytaxt == None:
    print("Bizni ro'yhatimizda bunday davlat yo'q ")
else:
    print(f" {user.title()}ning poytaxti {capital[user].title()} shahri.")
    ##########################################
meal = {
        'osh':25000,
        "sho'rva":20000,
        'qozonkabob': 22000,
        'shashlik': 12000,
        "manti": 4000,
        'somsa': 8000,
        "bishteks": 25000,
        "qotirma": 20000,
        "mastava": 15000,
        "shovla": 17000,
        }
taom = []        
print("3 ta taom buyurtma bering.")   
for son in range(1,4):
    t = input(f"{son} - taomni yozing ")
    taom.append(t)         
for taomlar in taom:
    if taomlar not in meal:
        print("bizda bunday taom yo'q")
    else:
            print(f"{taomlar} {meal[taomlar]} so'm ")








