# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 22:50:07 2023

@author: Ubaydullo-PC
"""

# Pythonda ham sonlarning bir necha turlari bor misol uchun integer folat va boshqalar 

#NTEGERS — BUTUN SONLAR
#Butun sonlarni ham o'zgaruvchida saqlash, ularning ustida qo'shish (+),
# ayirish (-), ko'paytirish(*), bo'lish (/) kabi arifmetik amalarni bajarish mumkin:
     
    
a = 30      #SONLAR MUSBAT YOKI MANFIY BO'LISHI MUMKIN \

b = 12.3    #BUTUN DUNYODA O'NLIK SONLARNI NUQTA BILAN AJRATIB YOZISHGA KELISHIB OLINGAN 

c = -10

gradus = 37.6
 
print(type(c))

d= a + c  #Python - operatorlar orasidagi bo'shliqlarni inobatga olmaydi. O'qishga qulay bo'lishi uchun yuqoridagi kabi (bo'shliqlar bilan) yozishingiz mumkin.
print(d)


# Uzun sonlarni kiritish 
#zun sonlarni kiritishda, qulaylik uchun, raqamlarni pastki chiziq (_) yordamida
#guruhlash mumkin. Python - son tarkibidagi pastki chiziqlarni (_) inobatga olmasdan,
#uzun sonligicha qabul qiladi.
odamlar = 7_897_999_000   # BIZ GA QULAY BO'LISHI UCHUN SHUNDAY YOZILADI 
print("yer kurrasida odamlar odamlar soni " , odamlar )

###################
#IR NECHTA O'ZGARUVCHIGA QIYMAT BERISH
#irdaniga bir nechta o'zgaruvchiga qiymat berish uchun o'zgaruvchilar va ularga
#mos qiymatlar vergul (,) bilan ajratiladi:
    
x, y, z, = 10, 12, -5
print(x)
     

#########################
a =30
c = 10
print(a/c)# Natija 3.0 o'nlik son bo'lib chiqadi 
# Buni butun son qilib chiqarish uchun bizga double // slashdan foydalalanamiz 
print(a//c) #  endi esa butun son chiqadi 

################################
#KONSTANTA
#ksar dasturlash tillarida konstant qiymatlar tushunchasi bor. Konstantlar
#o'zgarmas bo'ladi (misol uchun ning qiymati konstant, o'zgarmas qiymat). Pythonda
#konstant tushunchasi yo'q, shuning uchun dasturchilar bunday o'zgaruvchilarning
#nomini katta harflar bilan yozadilar (ogohlantirish sifatida). Bu albatta qat'iy
#qonun emas, lekin kelajakda o'zgaruvchilar orasida konstant qiymatlarni ajratish uchun yaxshi usul.
PI = 3.14159
radius =10
aylana_yuzi = PI * radius**2
print(aylana_yuzi)
print("Aylananing yuzi" , aylana_yuzi, " ga teng")

###################
#O'ZGARUVCHI TURINI ALMASHTIRISH
"""
keling quyidagi misolni ko'raylik, maqsadimiz ism va yosh degan ikki o'zgaruvchini
 yangi xabar degan o'zgaruvchiga yuklab, "Jobir 16 yoshda" degan matnni konsolga
 chiqarish:"""
 
ism = "Islomjon"
yosh = 16
'''
malumot = ism + ' ' + yosh + ' yoshda '''
malumot =  ism + ' ' +str(yosh) + ' yoshda'
yosh = str(yosh) # QILSAK BO'LADI LEKIN BU SAL YOSH DEGAN O'ZGARUVCHINI FAQAT MATN KO'RINISHIGA O'TKIZIB QO'YADI 
'''consolda type(yosh) qiymat turinii aniqlab beradi'''
print(malumot)
'''
 Natija: TypeError: can only concatenate str (not "int") to str
Afsuski, kutilgan natija o'rniga xatolik chiqdi. Agar xatoni ingliz tilidan tarjima
 qilsak, matn (str) va son (int) ni jamlab bo'lmaydi degan ma'no chiqadi. 
Demak Pythonda matn (string) va son (int, float) turidagi o'zgaruvchilarni jamlab
 bo'lmas ekan. Xo'sh, bunga yechim bormi? Albatta. 
Pythonda bir turdagi o'zgaruvchini boshqa turga o'tkazish mumkin, bu ingliz tilida
 typecasting detiladi. Buning uchun Pythonda mahsus funktsiyalar bor, keling ular bilan tanishamiz:
str()— int yoki float turidagi sonlarni matnga o'zgartiradi.
int()— matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi. Bunda
 matn butun son ko'rinishida bo'lishi kerak.
float()— matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi.
Demak, yuqoridagi kod to'g'ri ishlashi uchun 3-qatorni quyidagicha o'zgartiramiz:
    '''
    
 #matn turini tekshirish 
print(type(yosh))
print(type(radius))

###############################################################################
# INPUT() SONLAR 
#################################################
# FOYDALANUVCHI TUG'ILGAN YILINI SO'RAGAN HOLATDA YOSHINI ANIQLAB BERADIGAN DASTUR YOZAMIZ 
"1- NAVBATDA BIZ FOYDALANUVCHIDAN TUG'ILGAN YILINI SO'RAYMIZ"
yil = input("Tug'ilgan yilingizni kiriting \n>>>")
yil = int(yil) # deb foydalansak ham bo'ladi 
"""
yosh = 2023 - yil  # foydalanuvchi yoshini hisoblaymiz 
print('sizning yoshingiz', yosh) """
"""
Kutilgan natija o'rniga xatolik. Lekin xato qayerda? Dastur tug'ilgan yilimni
 so'radi, men 1983 deb kiritdim va shu zaxoti xato ro'y berdi va dastur to'xtadi.
 Xatoni tarjima qilsak son (int) va matn (str) o'rtasida ayirish (-) amalini bajarib bo'maydi deyapti.
Gap shundaki, input() funktsiyasi har qanday kiritilgan qiymatni matn (string)
 ko'rinishida qabul qiladi (garchi biz son kiritgan bo'lsak ham). Keling, konsolda
 t_yil degan o'zgaruvchining turini tekshirib ko'ramiz.
 """
'''
 type(yil)
 Out[55]: str   natija chiqadi '''

yil= int(input("Tug'ilgan yilingizni kiriting  \n>>>"))

yosh = 2023 - yil 
print("sizning yoshingiz", yosh)
 
a = int('10')
b = float('10')
temp = str(36.6)

########################################################
# AMALIYOT 
# FOYDALANUVCHI ISTALGAN SONNI KIRITSA UNING UNING KVADRATINI VA KUBINI ChiQARIB BERADIGAN DASTUR 
son = int(input("Istalgan sonni kiriting \n>>> "))
kvadrati = son**2
kubi = son**3
print("Kiritgan soningizni kvadrati:", kvadrati)
print("Kiritgan soningizni kubi:", kubi)

# tug'ilgan yilini aniqlab beradigan dasturcha tuzamiz 
yosh = int(input("Yoshingiz nechida \n>>> "))
yili = 2023-yosh
print("siz ", yili , " da tug'ilgansiz")


# IKKI SONNING YIG'INDISI AYIRMASI KO'PAYTMASI VA BO'LINMASI CHIQARADIGAN FUNKSIYA 

son = int(input('birinchi sonni kiriting: '))
number = int(input('ikkinchi sonni kiriting:'))

yigindi = son + number
ayirma = son - number
kopaytma = son * number
bolinma = son / number


print(f"{son} + {number} = {yigindi}")
print(f"{son} - {number} = {ayirma}")
print(f"{son} * {number} = {kopaytma}")
print(f"{son} / {number} = {bolinma}")



"""
 6 + 5 = 11
 6 - 5 = 1
 6 * 5 = 30
 6 / 5 = 1.2"""