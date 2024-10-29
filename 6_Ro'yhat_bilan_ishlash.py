# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:56:19 2023

@author: Ubaydullo-PC
"""
# Ubaydullo Obidjanov 
"""
RO'YXATNI TARTIBLASH

Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash
talab qilinishi mumkin. Buning uchun list uchun maxsus .sort() metodidan foydalanamiz.
"""
cars = ['bmv','mers', 'bugatti', 'ferrari', 'rols roys', 'tesla']

cars.sort()
print(cars)
"""Diqqat! Tartiblashda katta harflar kichik harflardan avval kelishini hisobga 
oling. Agar matndagi so'zlarning bosh harfi katta-kichik aralash yozilgan bo'lsa,
ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi."""
 
cars = ['bmv','mers', 'Bugatti', 'ferrari', 'rols roys', 'tesla']
cars.sort()
print(cars) # natija birinchi bosh harfi kattasidan boshlaydi 
"""
Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True 
argumentini ham kiritamiz. """
 
cars.sort(reverse=True )
print(cars)
"""
.sort() metodi ro'yxatni tartiblaydi. Ba'zida asl ro'yxat ichidagi elementlarning
ketma-ketligini buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin.
Buning uchun sorted() funktsiyasidan foydalanamiz:"""
host = ['ali', 'elyor', 'dilyor', 'hasan', 'dilorom',]
print(sorted(host)) # sorted metodini asl ro'yhat o'zgarmaydi 

print(host)
"""
sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True
 argumentini beramiz:"""
print(sorted(host, reverse=True)) 


# Yuoqridagi ikki usul bilan sonli ro'yxatlarni ham tartiblashimiz mumkin:
    
num =  [1200,352,65,76,83,-75,-25,-84,23.6,0.26]
num.sort()
print(num)
print(sorted(num, reverse=True))

# RO'YXATNI AYLANTIRISH
#Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi 
#mumkin. Buning uchun .reverse() metodidan foydalanamiz.
fruit = ['olma', 'behi','uzum', 'banan ']
fruit.reverse()
print(fruit)

"""RO'YXATNING UZUNLIGINI BILISH
Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun
len() funktsiyasidan foydalanamiz:"""

#uzunlik = len(fruit)
#print(uzunlik)
print(f'bugungi mevalarimizning umumiy soni: {len(fruit)} ta') # ro'yhat uzunliginni topadi 


"""
Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz 
mumkin. list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:"""

numbers = list(range(0,10))
print(numbers)#Yuqoridagi misolda range(0,10) funktsiyasi 0 dan 9 gacha sonlar
#ketma-ketligini shakllantirdi, list(range(0,9)) esa bu ketma-ketlikni ro'yxatga aylantir
"""
🛑 Diqqat! E'tibor qiling range() funktsiyasi ikkinchi indeksdan bitta avval 
to'xtaydi.
"""
juft_sonlar = list(range(0,20,2))
toq_sonalar = list(range(1,20,2))
print('0 dan 20 gacha bo\'gan juft sonlar quyidagilar \n>>>', juft_sonlar)
print('0 dan 20 gacha bo\'lgan toq sonlar quyidagilar \n>>>', toq_sonalar)

"""🛑Agar sonlar ketma-ketligi 0 dan boshlansa, range() funktsiyasida yakuniy
 indeksni ko'rsatish kifoya. Misol uchun range(0,10) emas range(10) deb yozsak
 ham bo'laveradi."""
son = list(range(10))
print(son)

"""
🛑SONLI RO'YXAT USTIDA SODDA AMALLAR
Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. Misol uchun
ro'yxatdagi eng kichik sonni topish uchun min() funktsiyasidan, eng katta sonni
topish uchun esa max() funktsiyasidan, sonlarning yig'indisini topish uchun esa 
sum() funktsyasidan foydalansak bo'ladi:
"""
cost  = [250,36,85,78,92,35,45]
rich_cost = min(cost)
cheap_cost = max(cost)
summ = sum(cost)
print(f"Eng arzon narx - {rich_cost}$ \nEng qimmat narx - {cheap_cost}$ \nJami summa - {summ}$")

'''
RO'YXATNI KESISH
Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab
qilinishi mumkin, deylik biz quyidagi cars degan ro'yxatdan
birinchi 3 ta elementni ajratib olmoqchimiz, buning uchun 
biz boshlang'ich va oxirgi indekslarni beramiz:
'''
cars = ['bmv','mers', 'Bugatti', 'ferrari', 'rols roys', 'tesla']
#Diqqat! Python 2-indeksdan bitta avval to'xtaydi.
#Yuqoridagi misolda ham 0,1,2-elementlar ajratib olindi.
my_lovely_cars = cars[0:3]
my_bad_cars = cars[3:5]# 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
print(f"""Mening sevimli moshinalarim bu - {my_lovely_cars}
Mening yomon ko'rgan moshinalarim bu- {my_bad_cars}""")


#Agar boshlang'ich indeksni bermasangiz, Python avtomat ravishda
#0 indeksdan boshlab kesadi. Agar 2-indeksni kiritmasangiz, 
#ro'yxat oxirigacha kesadi:

print(cars[:3])
print(cars[2:])


#RO'YXATDAN NUSXA OLISH
#Dastur davomida biror ro'yxatdan nusxa olish talab qilinishi
#mumkin. Buning uchun biz tenglik(=) belgisidan foydalansak 
#bo'ladimi? Quyidagi misolga e'tibor bering:

sonlar = [1,2,3,4,5]
sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
print("bu sonlar ro'yhati ", sonlar)
print("bu sonlar2 ro'yhati ", sonlar2)

#Natija biz kutgandek chiqdimi? Yo'q. Biz 6 va 7 sonlarini 
#sonlar2 degan ro'yxatga qo'shgan edik, lekin bu ikki son 
#sonlar degan asl ro'yxatga ham qo'shilib qoldi. 
#Demak yuqorida biz sonlar2=sonlar deb yozgan komandamiz
#yangi ro'yxat yaratish o'rniga, ikkala o'zgaruvchini ham 
#bitta ro'yxatga bog'lab (yo'naltirib) qo'ydi. Biz sonlar 
#yoki sonlar2 ustida bajargan amallarimiz aslida bitta 
#ro'yxat ustida bajarilyapti.


#Unda, qanday qilib ro'yxatdan nusxa olamiz? Buning uchun 
#yuoqirdagi ka'bi ro'yxatni kesish usulidan foydalanamiz. 
#Faqatgina, kvadrat qavs ichida ikkala indeksni ham ko'rsatmasdan,
#bo'sh qoldiramiz:

numbers1 = [1,2,3,4,5,6]
numbers2 = numbers1[:]# [:] ro'yxatni to'liq ko'chirib oladi
numbers2.append(45)
numbers2.append(26)  
print("Bu numbers1 ramaqamlari:", numbers1)
print("Bu numbers2 raqamlari:", numbers2)

#TUPLES - O'ZGARMAS RO'YXAT
#Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab 
#qilinishi mumkin. Pythonda bunday ro'yxatlar tuples deb
#yuritiladi. Tuple ichidagi qiymatlarni bir marta, dastur
#boshida beriladi va so'ngra o'zgartirib bo'lmaydi. List 
#dan farqli ravishda, Tuple e'lon qilishda kvadrat qavslar
#[] o'rniga oddiy qavslar () ishlatiladi:

kvadrat = (1,3,5,7,9)
print(kvadrat)
print(type(kvadrat))
#Tuple ichidagi elementlarga huddi ro'yxat elementlariga 
#murojat qilingani kabi murojat qilinaveradi:
print(kvadrat[2])
print(kvadrat[3])
print(kvadrat[-1])


animals= ('bear','lion','wolf','rabbit','cow')
#animals[0] = 'tiger'
#animals.remove('bear')
#animals.remove('wolf')
#Demak yuqorida ko'rib turganingiz kabi, bu operatsiya xatolikka
#olib keldi. Shu kabi ro'yxatdan biror elementni o'chirish yoki 
#yangi element qo'shish ham mumkin emas.

#Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas 
#ro'yxatni list() funktsiyasi yordamida List (oddiy ro'yxat) ko'rinishiga 
#keltirib olish, o'zgarishlarni bajarsih va qaytarib tuple() funktsiyasi 
#yordamida o'zgarmas ro'yxatga o'tkazish mumkin:
    
    
animals= ('bear','lion','wolf','rabbit','cow')
animals = list(animals) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
animals.append('snake')
animals.remove('lion')
animals.insert(4,'dog')
print(animals)
animals  = tuple(animals)

print(animals)

########################################################################################################################
#          AMALIY MASHG'ULOT 
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#Ro'yxatning uzunligini konsolga chiqaring
countries = ['tojikiston', 'turkmaniston', 'qozog\'iston', 'qirg\'iziston']
print("Bizning qo'shni davlartlar quyidagilar \n ", countries)

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(countries))
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(countries, reverse = True ))

#Asl ro'yxatni qaytadan konsolga chiqaring
print(countries)
countries.reverse()
print(countries)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari
#tartibda konsolga chiqaring.
davlat = ['bolgariya','armaniston','dubay', 'misr']
davlat.sort()
print(davlat)
davlat.sort(reverse=True)
print(davlat)
"""
120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
"""
juft_sonlar = list(range(120,1200,2))
print(juft_sonlar)
"""
Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
Ro'yxatdagi elementlar sonini hisoblang
Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
"""
print(sum(juft_sonlar))
print(max(juft_sonlar)-min(juft_sonlar))
print(len(juft_sonlar))

print(juft_sonlar[:10],
juft_sonlar[-10:],
juft_sonlar[265:275])
"""
taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
nonushta degan yangi ro'yxatga taomlardan nusxa oling
Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
"""    
meals = ['gamburger', 'chizburger', 'qotirma', 'sho\'rva', 'bifshteks']
nonushta = meals[:]

del nonushta[0]
nonushta.remove('qotirma')
nonushta.pop(1)
nonushta.append('sariyog')
nonushta.insert(0,'mastava')
print('Bizning nonushtada yeydigan taomimiz bu >>> ', nonushta)
"""
Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
"""
print(meals, nonushta)
nonushta = tuple(nonushta)
print(type(nonushta))
nonushta[0] = 'qaymoq va non'



