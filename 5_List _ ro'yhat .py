   # -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:09:39 2023

@author: Ubaydullo-PC
"""

# Mavzu: Ro'yhat Yani list 
# biz oldingiz darslarimizda bitta o'zgaruvchiga bitta qiymat berdik \
# endi bu galgi darsimizda bitta o'zgaruvchimizga bir nechta qiymat berishni o'rganamiz 
"""
Bugun o'rganadigan navbatdagi mal'umot turi List (ro'yxat) deb ataladi. Ro'yxat 
o'z nomi bilan, bitta o'zgaruvchida bir nechta qiymatlarni saqlash imkonini 
beradi. Bu qiymatlar List elementlari deyiladi. Ro'yxatda son, matn yoki 
aralash turdagi elementlarni saqlash mumkin. 
                                                  """
"Ro'yhatimiz quyidagi tarzda yaratiladi "

kitob = ['badiy', 'ilmiy', 'detektiv', 'iqtisodiy'] # matnli ro'yhat 

kitob_narxi = [2000, 3000, 2400, 5600] # raqamli ro'yhat manfiy musbat ham bo'lishi mumkin 

son_harf = ['bir', 'ikki', 40, 3, 5 ]   # sonli va raqamli ro'yhat 
ismlar = [] # bo'sh ro'yhat  buni ichida hech narsa yo'q hajmi nolga teng

print( kitob)
print(son_harf)
print(kitob_narxi)
"""
# bizda har bitta ro'yhatning uzunligi bor 
Ro'yxatdagi har bir element tartib bilan joylashgani sababli, biz istalgan elementga
 uning tartib raqami (indeksi) bo'yicha murojat qilishimiz mumkin. 
Dasturlash olamida indeks 0 dan boshlanadi! Ya'ni Listning birinchi elementing 
tartib raqami (indeksi) 0 ga, ikkinchi elementning indeksi 1 ga teng va hokazo.
"""

moshnalar = ["mers",'limuzin', 'Bugatti', 'Ferrari', 'BMV']
print('birinchi moshina modeli ' + moshnalar[0])
print('ikkinchi moshina modeli', moshnalar[1])
print(f'uchinchi moshina modeli {moshnalar[3]}')
print(moshnalar[1].title())
print(moshnalar[3].capitalize())

# List elementlari ustida amallar bajarish ;

print(kitob_narxi[1] + kitob_narxi[0])

"""
Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish 
mumkin. Bu usul Listning uzunligini bilmaganda juda asqotadi.  """

print(moshnalar[-1])
print(kitob[-2])   # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 


"""ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH
Dastur davomida listning tarkibi o'zgarishi, yangi elementlar qo'shilishi, ba'zi 
elementlar o'chirilishi tabiiy hol. Misol uchun "Bozorlik ro'yxati" degan dasturni 
tasavvur qilaylik, foydalanuvchi ro'yxatga yangi mahsulotlar qo'shishi, sotib 
olganlarini esa o'chrishi mumkin. 
"""
cost = [1200, 1300, 8500, 9600 , 7600]
cost[0] = 5600  # 1-qiymatni 5600 ga o'zgartiramiz 
cost[-1] = 7800 #ohirgi -qiymatni 7800 ga o'zgartiramiz 
cost[3] = cost[3] + 5200   #4- qiytga 5200 qo'shdik
print(f'YANGILANGAN NARHLAR QUYIDAGILAR: \n{cost}')


"""
Yangi element qo'shish
.append() metodi
Ro'yxatga yangi element qo'shishning oson usuli bu .append() metodi yordamida 
ro'yxatning oxiriga qiymat qo'shish:
"""
uy_jihozlari = ['stol', 'parta', 'ko\'rpa', 'parda']
print(uy_jihozlari)
uy_jihozlari.append('yostiq')
print(uy_jihozlari)   # uy_jihozlari ro'yhatiga  yostiqni qo'shdik

"""
.append() metodi bo'sh ro'yxatni to'ldrisihda juda qulay usul. Odatda dastur boshida 
bo'sh ro'yxat yaratilib, dastur davomida ro'yxat foydalanuvchi tomonidan 
to'ldirib borilishi odatiy hol.
"""
uy_hayvonlari = []
uy_hayvonlari.append('mushuk')
uy_hayvonlari.append('it')
uy_hayvonlari.append('mol')
uy_hayvonlari.append('qo\'y')

print(uy_hayvonlari)  # uy_hayvonlari degan bo'sh ro'yhatga uy hayvonlari ni qo'shdik

"""
.insert() metodi
Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan 
foydalanamiz. .insert() metodi ichida yangi elementning indeksi va qiymati 
beriladi:
"""
cars = ['malibu', 'matiz', 'nexia', ]

cars.insert(0,'nexia')
print(cars)

cars.insert(2,'captiva')
print(cars)

"""Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini 
bilishimiz lozim.
Inedks yordamida olib tashlash uchun del operatoridan foydalanamiz:
"""
cars = ['malibu', 'matiz', 'nexia', ]
del cars[2]
print(cars)
del cars[0]
print(cars)

'''
Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz.
 Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz
 '''
 
 
fruit = ['anjir', 'shaftoli', 'banan', 'olma', 'behi']
fruit.remove('olma')  # ro'yhat ichidan olmani olib tashlaydi 
print(fruit)
"""
.remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi
. Agar ro'yxatning ichida 2 va undan ko'p bir hil qiymatli elementlar bo'lsa, 
ulardan eng birinchisi o'chadi."""

cars = ['malibu', 'matiz', 'cobalt', 'nexia3', 'spark', 'matiz']
cars.remove('matiz')  # cars ro'yhatidan birinchi indexdagi bir hil elementni biirnchisini olib tashlaydi 
print(cars)

'''Elementni sug'urib olish
Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan
 sug'urib olish va undan foydalanish talab qilinishi mumkin. Buning uchun 
 Pythonda .pop(indeks) metodidan foydalanmiz.
'''
bozorlik = ['yog\'', 'gurusch', 'piyoz', 'kartoshka', 'olma']
olingan_mahsulot = bozorlik.pop(-1)
print('men',olingan_mahsulot,'sotib oldim')
print('olinmagan mahsulotlar', bozorlik)
'''
Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib 
olinadi.
'''
bozorlik.pop()
print(bozorlik)

ismlar = ['Ahmadjon', 'Dilmurod', 'Hayotbek']
print(f'Salom {ismlar[0]} bugun choyxona bormi ?')
print(ismlar[1], ',choyhonaga boramizmi ?')
print('Assalomu aleykum', ismlar[2], 'bugun futbol nechida ekan?')

numbers = [200, 300, 256,375, 24.8, 866, -256 ,-23, 24.5]
print(numbers[-1])
print(numbers[2] + numbers[-2])
print((numbers[-2] - numbers[-1])-numbers[-5] )
print(numbers[0]//10)
print(numbers[1]%numbers[2])
print(numbers[-1]**2)

numbers[-1] = 25
numbers[1] = numbers[1]+200
print(numbers)

t_shaxs = ['Alisher Navoiy ', 'Abdulhamid II', 'Abdulla Qodiriy', 'Pirimqul Qodirov']
z_shaxs = ['Robert Kiyosaki', 'Ilon Mask', 'Abdukarim Mirzayev', 'Javlon Jovliyev']

print('Men tarixiy shaxslardan '+ t_shaxs.pop(1) + ' bilan,\nzamonaviy shaxslardan esa ' + z_shaxs.pop(1) +' bilan suhbat qurishni istardim ')

friends = []
friends.append('Dilmurod')
friends.append('Ahmadjon ')
friends.insert(0,'Hayotbek')
friends.insert(2,'Qobiljon')
friends.insert(2, 'Azimjon')
print(friends)

friends.remove("Azimjon")
friends.remove("Qobiljon")
print(friends)

friends.insert(1, 'Humoyin',)
friends.insert(2, 'Mirzohid')
friends.insert( -1, 'Shavkatjon')
print(friends)

new_host = []

new_host.append(friends.pop(-1))
new_host.append(friends.pop(0))
new_host.append(friends.pop(-2))
new_host.append(friends.pop(1))
print(new_host)

