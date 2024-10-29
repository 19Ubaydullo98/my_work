# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:45:00 2023

@author: Ubaydullo-PC
"""
"""
if-elif-else KETMA-KETLIGI

biz b'yini o'yin o'ynaqaganimizds shartlar chiqadi o'ngga burilsangiz bu ish bo'ladi
yoki boshqsini bossangiz boshqa o'zgarish bo'ladi hullas o'yin yoki dasturlarda 
bitta emas bir nechta shartlar beriladi, endi shu shartalarni quyidagicha tushunamiz 

Dastur davomida bir nechta shartni tekshirish talab qilinishi mumkin. Bunday
holatda biz if-elif-else ketma-ketligidan foydalanamiz. elif - else va if so'zalrining 
jamlanmasi bo'lib, "aks holda, agar" deb tarjima qilinadi. Bunday if bilan boshlangan 
ketma-ketlik bir nechta elif lardan iborat bo'lishi mumkin. 

Python avval if shartini tekshiradi, shart bajarilmasa elif ga o'tadi, birinchi 
elif sharti bajarilmasa keyingi elif ga o'tadi va hokazo davom etaveradi.

Diqqat!if-elif-else ketma-ketlikda biror shart bajarilishi bilan, Python qolgan 
shartlarni tekshirmaydi.

Keling bir misol ko'ramiz. Hayvonot bo'giga kirish quyidagicha belgilangan:
4 yoshdan kichik bolalarga kirish bepul
4 yoshdan 12 yoshgacha kirish 5000 so'm
12 yoshdan kattalarga 10000 so'm
Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini
chiqaruvchi dastur yozamiz.
"""
yosh = float(input("Yoshingizni kriting: "))
if yosh <= 4 :
    print("4 yosdan kichik bolalarga krish bepul.")
elif yosh <= 12:
    print("Sizga kirish 5000 so'm")
elif yosh>12:
    print("sizga krish chiptasi 100000 - so'm ")
###########################################
#Kod yozishda yaxshi amaliyotlardan biri, kodlarni qisqa yozish va buyruqlarni 
#qayta-qayta takrorlamaslik. Bu kelajakda kodni o'zgartirishda ham juda qo'l keladi. 

yosh = float(input("Yoshingizni kriting: "))
if yosh <= 4:
    price = 0
elif yosh <= 12:
    price = 5000
else:
    price = 10000
print(f" Sizga kirish {price} so'm")
#######################################################
# Avval aytganimizdek,  if-elif-else zanjirida bit nechta elif lar bo'lishi mumkin.
# Misol uchun, hayvonot bog'i qariyalar uchun chegirma e'lon qilsa, kodimizni 
# quyidagicha o'zgartirishimiz mumkin:

yosh = float(input("Yoshingizni kriting: "))
if yosh <= 4:    # 4 YOSHDAN KICHIKLARGA BEPUL
    price = 0
elif yosh <= 12:  # 12 YOSHDAN KICHIK VA 4 YOSHDAN KATTALRGA 5000 SO'M
    price = 5000
elif yosh > 60:   # 60 YOSHDAN KATTALARGA BONUS 8000 SO'M 
    price = 8000
else:
    price = 10000
print(f" Sizga kirish {price} so'm")

#  if-elif-else zanjirida ham else qismi majburiy emas:
    
##########################################################################
""" AND, OR OPERATORLARI
Yuqorida aytganimizdek, if-elif-else zanjirida shartlarning biri bajarilishi
 bilan, Python qolgan shartlarni tekshirmaydi va ularni bajarmaydi. Lekin ba'zida 
 biz 2 yoki undan ko'p shartlarni tekshirishni talab qilishimiz mumkin, buing uchun
 AND va OR operatorlaridan foydalanamiz.
 
OR OPERATORI
OR ingliz tilidan "yoki" deb tarjima qilinadi, va ikki va undan ko'p shartlardan
biri bajarilishini tekshirishda ishlatiladi. Quyidagi misolni ko'raylik, foydalanuvchidan 
hafta kunini so'raymiz va agar kun shanba yoki yakshanba bo'lsa, bugun dam olish 
kuni degan xabarni chiqaramiz, aks holda bugun ish kuni degan xabarni chiqaramiz:
"""
kun = input("Hafta kunini kiriting: ")
if kun.lower()== "shanba" or kun.lower() == "yakshanba":# bu yerda ko'ramizki 
# ikkita shart berilyapti ikkalasidan biri rost bo'lsa ham Javob True bo'ladi 
    print('Bugun dam olish kuni')
else :
    print('Bugun ish kuni')

"""
AND OPERATORI
AND ingliz tilidan "va" deb tarjima qilinadi, va ikki va undan ko'p shartlarning
 barchasi bajarilishini tekshirishda ishlatiladi. AND operatori bilan yozilgan
 shartlarning barchasi bajarilgandagina TRUE qiymati qaytadi, agar shartlardan biri bajarilmay qolsa ham FALSE qiymati qaytadi.
    """
day = input("Bugun nima kun: ")
gradus = float(input("BUgungi havo haroratini kriting: "))
if day.lower()=="yakshanba" and gradus >= 30:
    print("let's go to swimm")
elif day.lower()=="yakshanba" and gradus <30:
    print("NO. we aren't going to go swimm")
    
    
#############################
#BIR NECHA SHARTLARNI KETMA KET YOZISH 
# Shartlarni yozishda bir necha or yoki AND operatorlarini 
#birga ishlatish

day = input('Bugun haftaning qaysi kuni: ')
harorat = float(input("what is wheather: "))
if (day.lower() == "yakshanba" or day.lower() == "shanba") and harorat >= 30:
    print("Let's go to swimm")
elif (day.lower()=="yakshanba"or day.lower()=="shanba") and harorat<30:
    print("We are at home")#####
############################

"""            BOOLEAN MA'LUMOTLAR TURI
Avvalgi darsimizda biz turli ifodalarni solishtirishda TRUE yoki FALSE qiymatlari
qaytishini ko'rdik. Bu qiymatlar boolean (mantiqiy) qiymatlar deb ataladi, va 
dasturlashda juda keng qo'llaniladi. Pythonda o'zgaruvchilarda boolean 
qiymatlarni ham saqlash mumkin. 
"""
a = 'olma'
print(a)
'''
a == 'olma' bu yerda a o'zgaruvchimiz olmaga tengmi deb so'radik va
Out[3]: TRUE       HA TO'G'RI DEEGAN JAVOB OLDIK 

a == 'behi'        bu yerda a o'zgaruvchimiz BEHIGA tengmi deb so'radik va
Out[4]: False     YO'Q teng emas degan javob oldik 
'''

##### misol sifatida choyxonnani olaylik 

osh = 20000  # o'rtacha ovqat narxi 20 ming so'm 
choy = True # choy olsa ha bo'ladi 
salat = False # salat olmasa yo'q bo'ladi 

if choy : # CHOY OLDI HA BO'LAD
    print(osh+5000)
elif salat:
    print(osh + 7000)
#################
osh = 20000  # o'rtacha ovqat narxi 20 ming so'm 
choy = False # choy olsa ha bo'ladi 
salat = True  # salat olmasa yo'q bo'ladi 

if choy : # CHOY olmagan yo'q bo'ladida keyinngi shartnni tekshiradi
    print(osh+5000)
elif salat:     # BUNDA SALAT OLGAN BU TRUE BO'LADIDA SHU SHARTNNI BAJARADI 
    print(osh + 7000)
####################################################

osh = 20000  # o'rtacha ovqat narxi 20 ming so'm 
choy = True # choy olsa ha bo'ladi 
salat = False # salat olmasa yo'q bo'ladi 

if choy and salat : # agar ikkalasi ham true bo'lsa buni bajaaradi 
    osh = osh + 10000 # choy 5000 va salat 5000 so'm qo'shib qo'yamiz 

elif choy or salat: # bulardan bittasi ha bo'lsa ham bu shartni bajaradi 
    osh = osh + 5000 # choy yoki salat bulardan biri true bo'lsa bu amal bajariladi 

print(f" jami nar {osh}")  # ikkalasini ham true qilib ko'ramiz 
#Boolean o'zgaruvchilarni saqlashda TRUE va FALSE qiymatlari o'rniga
# 1 va 0 sonlarini ham ishlatish mumkin. yuqoriga true = 1 false = 0 qo''yamiz 
####################################3""

"""
SHARTLARNI KETMA-KET TEKSHIRISH
if-elif-else zanjirining kamchiligidan biri, shartlardan biri bajarilishi bilan, 
qolgan shartlar tekshirilmaydi. Shung uchun ba'zida shartlarni ketma ket tekshirish 
uchun, har bir shartni alohida if bilan ajratish talab qilinishi mumkin."""

meal = 15000  # mijoz choyhonadan 15000 so'mlik ovqqat harid qildi  va qo'shimchasiga 
non = True  # non sotib olgani uchun  true = ha qo'yayapmiz 
salat= False # salat sotib olmaganni uchun false = yo'q qo'yayapmiz 
choy = True
assarti = False 
kompot = True 
########### endi biz har bitta olgan narsasi uchun shart qo'yib chiqamiz
if non : # non olgan bo'lsa 
    meal = meal + 3000 # non narxi 3000 so'm 
    print("Mijoz non oldi.")
if salat: # salat olgna bo'lsa 
    meal = meal + 5000
    print("Mijoz salat oldi.")
if choy : # choy olgan bo'lsa 
    meal = meal + 2000    
    print("Mijoz choy oldi.")
if assarti: # agar assarti olgan bo'lsa 
    meal = meal + 8000
    print("Mijoz assarti oldi.")
if kompot: # agar kompot olgan bo'lsa 
    meal = meal + 10000
    print("Mijoz kompot oldi.")

print(f"Sizning jami hisobingiz: {meal}")
#########################################################################
'''RO'YXAT TARKIBINI TEKSHIRISH
in OPERATORI
in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini
tekshirishimiz mumkin.  '''#
# misol uchun: o'quv qurollari ro'yhati tuzaylik
equipment = ['pencil', 'pen', 'schoolbag', 'book', 'notebook', 'marker',]
print('pen' in equipment) # in operatori penni equipment ro'yhatidan qidiradi 
print('meal' in equipment)  # bor bo'lsa true, yo'q bo'lsa false chiqaradi 

equipment = ['pencil', 'pen', 'schoolbag', 'book', 'notebook', 'marker',]
me = input("Yangi o'quv yiliga qanday o'quv qurollari olmoqchisiz: \n>>>")

if me.lower() in equipment:
    print("Buyurtmangiz qabul qilindi.")
else:
    print("Kechirasiz bizda bunday o'quv qurol yo'q!")

###################################
'''              not in OPERATORI    
 # endi bu in operatorini aksi 
 not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz
 mumkin.'''
equipment = ['pencil', 'pen', 'schoolbag', 'book', 'notebook', 'marker']

print('pen' not in equipment) # not in operatori penni equipment ro'yhatidan qidiradi 
print('meal' not  in equipment)  # bor bo'lsa false yo'q bu ro'yhatda bor deydi ,
# yo'q bo'lsa true deydi chunki pen bu ro'yhaatda yo'q deb chiqaradi 

equipment = ['pencil', 'pen', 'schoolbag', 'book', 'notebook', 'marker',]
me = input("Yangi o'quv yiliga qanday o'quv qurollari olmoqchisiz: \n>>>")
if me.lower() not  in equipment:  # agar foydalannuvchi yozgann narsa ro'yhatda yo'q bo'lsa shu shartnni bajaradi 
    print("Kechirasiz buzda bunday o'quv qurol yo'q!")
else:
    print("Buyurmangiz qabul qilindi.")
    ####################################################################
    '''
    not operatorini boshqa shartlarning oldidan ham qo'yishimiz mumkin. Misol uchun: 
    if not a==5 ifodasi if a!=5 ifodasi bilan bir hil natija qaytaradi.
    '''
    a=9
    if not a==5:
        print("to'g'ri teng emas")

    if a!=5  :
        print("to'g'ri teng emas")

    #####################################################
    '''             IKKI RO'YXATNI SOLISHTIRISH
    Ikki ro'yxatning tarkibi quyidagicha tekshiriladi:
    '''
    taomlar = ['osh','qazonkabob', ' kabob', 'somsa','norin']
    buyurtma = ['kabob',"sho'rva", 'somsa','osh']
    for buyur in buyurtma:
        if buyur in taomlar:
            print(f'menyuda {buyur} bor.')
        else:
            print(f'Kechirasiz! menyuda {buyur} yo\'q. ')
    ########################################################
    """
    RO'YXAT BO'SH EMASLIGINI TEKSHIRISH
    Yuqoridagi dasturimizda biz foydalanuvchi buyurtma berdi deb tasavvur qilyapmiz.
    Lekin foydalanuvchidan bo'sh ro'yxat kelsachi? Demak for tsiklini bajarishdan
     avval ro'yxat bo'sh emasligiga amin bo'lishimiz kerak. Buning uchun avvalgi 
     kodimizni quyidagicha o'zgartiramiz:   """
     
number = [33,45,65]
iymon = []
if number:   # bu bo'sh ro'yhat bo'lmasa buni bajaradi 
    print(f"{number}")

if iymon:   # bu bo'sh bo'lmasa shartnni bajaradi lekin bo'sh bo'lsa else chiqadi
    print(f"{iymon}")
else:
    print("bu ro'yhat bo'sh ")
###############################################################################     
     
taomlar = ['osh','qazonkabob', ' kabob', 'somsa','norin']
buyurtma = ['kabob',"sho'rva", 'somsa','osh']
if buyurtma:
    for buyur in buyurtma:
        if buyur in taomlar:
            print(f'menyuda {buyur} bor.')
        else:
            print(f'Kechirasiz! menyuda {buyur} yo\'q. ')
else:
    print("Sizning savatcha bo'sh")
    
#############################################################################
#  Vazifa 
"""
AMALIYOT

Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa
"Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
"""
# 1-mashq
number = float(input('Juft son kriting: '))

if not number%2 == 0 : 
    print("Bu son juft emas.")
else:
    print("Rahmat")
###################################### 2 mashq 
age = float(input("Iltimos yoshingizni kiriting: "))
if age < 4:
    narh = "chipta siz uchun bepul"
elif age < 18:
    narh = 10000
elif age <60:
    narh = 20000
else:
    narh = 'chipta siz uchun bepul '
print(narh)
############################################# 3-mashq
one_num = float(input("1-sonni kiriting: "))
two_num = float(input("2-sonni kiriting: "))
if one_num< two_num:
    print(f"{one_num}<{two_num}")
else:
    print(f"{one_num}>{two_num}")
############################################## 4-mashq
product = ['apricot',"apple",'pear','peach',"pomegranate","grape",'watermelon','melon',"fig",]
basket = []
for num in range(1,6):
    basket.append(input(f"{num}-mahsulotni kiriting: "))
print(basket)

if basket:
    for mahsulot in basket:
        if mahsulot in product:
            print(f"Do'konimizda {mahsulot} bor")
        else:pro
            print(f"Do'konimizda {mahsulot} yo'q")
############################################## 5-mashq 
product = ['apricot',"apple",'pear','peach',"pomegranate","grape",'watermelon','melon',"fig",]
savat = []
for n in  range(1,6) :
    savat.append(input(f"Savatga {n}-mahsulotni qo'shing:  "))
bor_mahsulotlar = []
mavjud_emas = []
for meva in savat:
    if meva in product:
        bor_mahsulotlar.append(meva)
    else:
        mavjud_emas.append(meva)

print(f"dokonimizda quyidagi mahsulorlar yo'q: \n{mavjud_emas}")
#33333333333333333333333333333333333333333333333333    6-mashq
users = ['ali','vali', 'umid','dilshod', 'ahmad' ]
login = input("Yangi login tanlang: ")
if not login in users:
    print("Xush kelibsiz")
else:
    print("Login band, yangi loin tanlang!")
