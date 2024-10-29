#####             MODUL          ##############
"""funksiya biizga dasturimiz ichida takrorlanadigan kodlarni funksiya ichiga yashirib 
qo'yomiz va istalgan payt bu funksiyaga murojat qilamiz. BUnday qilishimizdan 
asosiy maqsadimiz esa Kodlarimizni ixchamlash va tushunarli qilib qo'yish va yana 
shu maqsadda biz Moduldan foydalanishimiz mumkin.
  MOdul bu alohida fayl bo'lib, dasturimizda foydalaniladigan kodlar, funksiya, o'zgaruvchilarni
shuni ichida saqlab qo'yishimiz mumkin. bizga bu asosiy dasturimizdan chalg'imasdan 
kod yozish uchun foyda beradi.
   Modul va buni ichidagi funksiyalarimidan istalgan vaqt yuklab olishimiz mumkin va
foydalanishimiz, boshqa dasturchilar bilan ulashishimiz va kelajakda boshqa loyihalarimizda
bundan foydalanishimiz mumkin 

Umuman olganda dastur bir necha o'nlab modullardan foydalanishimiz tabiy hol."""

##############           MODUL YARATAMIZ                ############"""
# Modul yaratish uchun asosiy dasturimizdagi funksiyalarni yangi faylga
# ko'chiramiz xolos. Modulga oson murojat qilishimiz uchun, faylimiz asosiy 
# dasturimiz bilan bitta papkada bo'lgani afzal. Bunda adashib ketmaslik uchun, 
# loyihangizning (dasturning) asosiy faylini main.py deb nomlash o'rinli. 

###################################j
# # Moduldan foydalanish 
# import avto_info_mod     #### umumiy bitta papkada turishi kerak 
# avto_1 = avto_info_mod.car_info("gm", "malibu", 'qora', 'avtomat', 2023, 33000) #. tadasn oldin modul nomini yozis kere 
# avto_info_mod.info_print(avto_1)
# #############
# import avto_info_mod  as aim # modul nomi uzunlik qilsa unga qisqa nom berish 
# avto_1 = aim.car_info("gm", "malibu", 'qora', 'avtomat', 2023, 33000)
# aim.info_print(avto_1)

#################### en qulay usuli ichida gar bir funsiyani nomi bilan chaqirib olsak 
# from avto_info_mod import car_info, info_print   # keyinchalik modul nomini  qayt-qayta yozish shart emas 
# avto_1 = car_info("gm", "onix", 'oq', 'avtomat', 2023, 17000)
# info_print(avto_1 )

################################################ bu yerda alohida ajratilgan obyektni
# from avto_info_mod import car_info as info, info_print as iprint #  ham biror nom bilan saqlab olsak bo'ladi 
# avto_1 = info("gm", "onix", 'oq', 'avtomat', 2023, 17000)
# iprint(avto_1)
################################# yulduzcha orqali model ichidagi barcha funksiyalrni
# from avto_info_mod import *  # chaqirib olamiz lekin bu usul ko'p ham qo'llanilmaydi 
# avto_1 = car_info("gm", "onix", 'oq', 'avtomat', 2023, 17000)   #chunnki katta katta modellar ichida turli hil funksiya va o'zgaruvchilar bo'lishi mumkin 
# info_print(avto_1)
#########################################
########################################################################             Modulda o'zgaruvchilar  saqlash 
""" MOdul ichida nafaqat  funksiyalar , balki turli o'zgaruvchilarni ham saqlash 
mumkin. MOdul ichidagi o'zgaruvchilarga ham xuddi  yuqoridagi usullar bilan 
murojat etamiz.             """
#######################3    Python MOdullar 
# python d.t tayyor modullar bilan keladi, ularni bazilari bilan tanishamiz 
# bunda matematik hisob-kitoblarni bajaruvchi funksiyalar va o'zgaruvchilar joylashgan 
##########  Math moduli        ########################
import math

# 1- sqrt ildizdan chiqaradi 
# 2- pow(x,n)  x ning n chi darajasini qaytarad
# 3-pi= 3,1415926535
# 4-log2(x) va log10(x)= x ning 2 lik va 10 lik logarifmini qaytaruvchi funksiya    
x = 400
print(math.sqrt(400))
y = 729 
print(math.sqrt(y))
####2- pow(x,n)  x ning n chi darajasini qaytaradi
print(math.pow(10,3))

#### 3-pi= 3,1415926535
from math import pi
print(pi)

###### 4-log2(x) va log10(x)= x ning 2 lik va 10 lik logarifmini qaytaruvchi funksiya    
print(math.log2(9))

print(math.log10(9))
###########################################    Random moduli
# random moduli tasodifiy sonlar bilan ishlash uchun qulay 
import random as r 
#1-randint(a,b) a va b oraliiqdagi tasodifiy butun son 
#2-choice(x)  berilgan x argumentni ichidagi tasodifiy element 
#3-shuffle(x)- x ichidagi elementlarni tasodifiy  tartibda qaytaruvchi funksiya. 
#4-sample(x,k)- x ro'yxatni aralashtirib k ta element ajratib olish:#
# Math modullari ichidagi boshqa funksiyalar haqida python rasmiy sahifasida
#(docs.python.org) ma'lumot olishingiz mumkin.

names = ['ali','vali', 'sardor','shamil']
ism = r.choice(names)
print(ism)
print(r.choice(ism)) #ismlar ichidan ixtiyoriy ismni tanlab olib yana shu ismning ixtiyoriy harfini tanlaydi
#####
numbers = list(range(4,26,2))  
print(numbers)
print(r.choice(numbers))
####
numbers = list(range(16)) 
print(numbers)
r.shuffle(numbers) # shuffle hammasini aralashtirib tashlaydi 
print(numbers) 






























