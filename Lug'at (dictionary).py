# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:25:18 2023

@author: Ubaydullo-PC
"""
"""
Ushbu darsda yangi ma'lumot turi, Lug'at (Dictionary) bilan tanishamiz. Dars
 davomida lug'at yaratish, unga ma'lumot qo'shish, lug'atning ichida ro'yxat 
 yoki aksincha ro'yxatning ichida lug'at saqlash ka'bi mavuzlar bilan tanishamiz.
 
Lug'at, ma'lumotlarni bizga tushunarliroq ko'rinishda saqlash imkonini beradi. 
Misol uchun biz biror avtomobilga oid lug'at yaratishimiz va lug'atda shu avtoga 
tegishli barcha ma'lumotlarni saqlashmiz mumkin (nomi, rangi, yili, motori, narhi va hokazo). 
##############################################

                          LUG'AT (DICTIONARY) NIMA?
Keling, nima uchun bu ma'lumot turi lug'at (dictionary) deyilishini tushunish uchun,
oddiy lu'gatga qaraymiz. Odatda, lug'atdagi ma'umotlar ikki qismdan iborat bo'ladi:
kalit so'z va izoh (yoki tarjima).
Apple (kalit) ---- Olma (tarjimasi = izohi )   
colour(kalit so'z) ----- Rang (izohi = tarjimasi)

Xuddi oddiy lug'atlardagi ka'bi Python lug'atidagi ma'lumotlar ham ikki qismdan
iborat bo'ladi: kalit so'z va qiymat (ingliz tilida key-value pair yoki kalit
o'z-qiymat juftligi deyiladi).


Dasturlashda ko'p ishlatiladigan atamalarni ingliz tilida yodlab qolish juda muhim!
Bu sizga kelajakda yangi ma'lumotlar izlashda, xatolar usitda ishlashda va umuman 
ish faoliyatingizda ko'p asqotadi. Shuing uchun variable, integer, float, string,
list, tuple, dictionary, function, loop, va boshqa so'zlarni yaxshilab o'zlashtirib oling."""
##################################
# keling oddiy lug'at yaratamiz 

fruit = {"apple":"olma", 'peanut':"yeryong'oq","pomegranate":"anor"}
print(fruit['apple']) # kalit so'z apple uni izohi esa 
print(f"Peanutning tarjimasi {fruit['peanut']} bo'ladi.")
#######
car_1 = {'model':'ferrari','rangi':'qizil'} #shu lug'at 
print(car_1)                                  
"""
Yuqorida car_0 degan lug'at yaratdik. Lu'gatda 2 ta ma'lumot bor: mashinaning modeli
(ferrari) va rangi (qizil). Bu yerda 'model' va 'rang' kalit so'zlar, 'ferrari' 
va 'qizil' esa mos keluvchi kalit so'zlarning qiymatlari. Kalit so'z va qiymat 
orasi ikki nuqta (:) bilan, lug'atdagi har bir juftlik esa vergul (,) bilan ajratilgan. """
################################################SRCTVUYBIUNOMP<LMNOUIYUTRESERTVYBIN
'''                 LUG'AT BILAN ISHLASH
Demak, Pytonda lug'at kalit so'z-qiymat juftliklarining yi'ginidisi ekan. 
Lug'atdagi biror qiymatni ko'rish uchun unga kalit so'z orqali murojat qilamiz: '''
###
car_1 = {'model':'ferrari','rangi':'qizil'} #shu lug'at 
print(car_1['model'].title())# biz ro'yhatga index orqali emas kalit so'z orqali murojat qilamiz
print(car_1['rangi'].title())

#Lug'atdagi qiymatlar son (int, float), matn (string), ro'yxat (list, tuple) va
# hatto boshqa lug'at ham bo'lishi mumkin.
####

student = {'ism':'isroiljanov islomjon','date':'2010','birth':13}
print(f"""Talaba: {student['ism'].title()}
{student['date']}-yilda tug'ilgan 
hozirda u {student['birth']} yoshda""")
##############################################################
'''                       YANGI JUFTLIK QO'SHISH
Lug'aga yangi kalit so'z va qiymatlar qo'shishimiz ham mumkin. Keling, yuqoridagi
talaba_0 nomli lu'gatga yana 2 ta yangi, kurs va fakultet nomli, kalit so'zlar
va qiymatlar qo'shamiz:                   '''
student['guruh'] = 18.104
student['fakultet']= 'Kompyuter injinering'
print(student)
###
student['ism']='ubaydullo' # bunda lug'atdagi qiymatni o'zinin o'zgartiridik
# ism o'zi Islomjon Isroiljanov edi va endi esa u Ubaydulloga o'zgardi 
################################################################
'''                        BO'SH LUG'AT
Ba'zida dastur boshida bo'sh lug'at yaratib, dastur davomida lug'atga yangi 
ma'lumotlar kiritib borish talab qilinishi mumkin. Bundah holatda bo'sh lug'at 
quyidagicha yaratiladi:                                     '''
student_1 = {}
student_1['ism']= 'hasanboy jo\'rahanov'
student_1['date']=2005
student_1['age']=18
print(student_1)
print(f"Talaba {student_1['ism'].title()} {student_1['date']} yilda tug'ilgan, Hozirda u {student_1['age']} yoshda")

#Lug'atga kalit so'zlar qanday ketma-ketlikda kiritilsa, shu ketma-ketlik saqlanib qoladi.
######################################################################
#                      QIYMATNI O'ZGARTIRISH
#Biror kalit so'zga tegishli qiymatni o'zgartirish esa quyidgachia amalga oshiriladi:
student_1['age']=19 # yoshini 1 yoshga o'zgartirdik
print(f" Talaba {student_1['ism'].title()} hozir {student_1['age']} yoshda ")
###############################################################
'''                 KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH
Lu'gatdagi biror juftlik kerak emas bo'lsa uni del operatori yordamida
 lug'atdan olib tashlashimiz mumkin:               '''
print(student_1)
del student_1['date']
print(student_1) # bu yerda talabani nechanchi yilda tug'ilganini chiqarib tashladik
####
print(fruit)
del fruit['pomegranate']  #bu yerda pomegranate ni o'chirib tashladik 
print(fruit)
###########################################################################
'''            LUG'ATNI QATORLARGA BO'LIB YOZISH
Uzung lug'atlarni bir necha qatorga bo'lib yozishimiz ham mumkin. Keling quyidagi
misolni ko'ramiz, siz do'stlaringizdan ular qanday modeldagi moshina minishini
hohlardiz deb so'radingiz va javoblarni bitta lug'atga joylamoqchisiz:             '''
car = {   # Birinchi siz  katta qavsni ochamiz va enterni bosamiz 
       'dilmurod':'ferrari',  # agar biz bu yerda vergul qo'ymasak code hatolik chiqaradi
       'Qobil':'nexia',
       'hayotbek':'tesla',
       'ahmadjon':'maskvich'
       }         # KATTA QAVSNI SHU TARZDA YOPAMIZ       
print(car)

'''Lug'atlarning ishlatilish doirasi juda keng va sizning yondoshuvingizga 
bog'liq xolos. Yuqoridagi lug'atga ham e'tibor qilsangiz, biz bir narsa (shaxs,
avto) haqida ko'p ma'lumotlarni emas,  ko'pchilik haqida bir hil ma'lumotlarni saqladik. '''
##########################################################################
'''                           get() METODI
Biz shu vaqtgacha lug'atdagi qiymatlarni ko'rish uchun to'g'ridan-to'g'ri kalit 
so'z orqali murojat qilayotgan edik. Bu usulning kamchiligi shundaki, agar 
lug'atda siz so'ragan kalit topilmasa, dastur KeyError xatoligi bilan to'xtab qoladI          '''
print(car)
moshin = car['ahmadjon']
print(f"Ahmadjon {moshin} moshinasini minmoqchi!")
####
#print(car['shavkatjon']) #bunda biz car lug'atida yo'q kalitni so'radik 
#natija:  KeyError: 'shavkatjon'   shunga o'xshagan hatolik chiqaradi   
'''KeyError ham Run time error qatoriga kiradi.'''
######## shunday vaziyatda bizga GET metodi bizga yordamga keladi
moshina = car.get("shavkatjon", 'bunday ism yo\'q.')
print(moshina) # bu yerda get metodi 
# birinchi get shavkatjonni oladida carnni ichidan bunday keynni qidiradi 
# topilmasa verguldann keyingi matnni chiqaradi 
#verguldan keyin hechn narsa yozmasak ham bo'ladi 
#######
'''Agar .get() metodida ikkinchi argumentni tashlab ketsangiz, va kalit mavjud 
bo'lmasa .get() metodi None degan qiymatni qaytaradi. None - qiymat mavjud emas
degan ma'noni beradi.                                                 '''
bus = car.get('shavkatjon')
print(bus)
#   Natija:   None -- mavjud emas = yo'q degani bu 
#####################################################################33

py_tr = {
    'lstrip': 'matn boshidagi bo\'shliqni o\'chiradi',
    'rstrip': "matn oxiridagi bo'shliqni o'chiradi",
    'strip': "matn boshi va ohiridagi bo'shliqni o'chirib tashlaydi",
    "upper": "har bir harfni katta harf qilib beradi",
    "lower": "har bir harfni kichik harf qilib beradi ",
    "n": "matnni qator tashlab yozish uchun",
    "t": "matnga bo'shliq qo'shish uchun",
    "type": "o'zgaruvchi turini aniqlab olishimiz uchun",
    "append": "ro'yhatga yangi element qo'shish uchun",
    "insert": "indexini ko'rsatgan holatda element qo'shish"
    }
#print(py_tr)
sentence = input("Kalit so'zini kiriting:")
gap = py_tr.get(sentence)
#print(gap)
#print(sentence)

if gap == 'none':
   print(f"Bizda bunday so'z yo'q")
else:
    print(f"{sentence} so'zi {py_tr[sentence]} ")

                  
















