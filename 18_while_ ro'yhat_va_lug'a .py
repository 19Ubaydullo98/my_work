# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:40:43 2023

@author: Ubaydullo-PC
"""
"""                        WHILE YORDAMIDA RO'YXATNI TO'LDIRISH
Quyidagi dasturga e'tibor bering, avval ismlar degan bo'sh ro'yxat yaratib oldik.
Keyin esa while tsikli yordamida foydalanuvchidan ro'yxatga ism qo'shishni so'raymiz.
So'ngra foydalanuvchidan yana ism qo'shmoqchi yoki yo'q ekanin so'raymiz va 
foydalanuvchining javobiga ko'ra yoki while ni boshiga qaytamiz, yoki tsiklni to'xtatamiz."""
friends = []
n=1
while True:
    savol = f"{n}-do'stingizni kiriting: "
    dost = input(savol)
    friends.append(dost)
    javob = input("Yana ism qo'shasizmi (ha\yo'q): ")
    if javob.lower() != "ha":
        break
    else:
        n +=1
print("Do'stlaringiz ro'yhati:")
for n in friends:
    print(f"{n.capitalize()}")             
###############################%$%$%$%$%$%$%$%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                        
"""                      WHILE YORDAMIDA LUG'ATNI TO'LDIRISH
Yuqoridagi usul bilan lu'gatlarni ham shakllantirishimiz mumkin. Quyidagi kodda 
ism bu kalit, yosh esa klaitga mos keluvchi qiymat. while tsiklining davomiyligi
 esa ishora ning qiymatiga bog'liq.                                """
######################################$%YEDRYYYYYYYYYYYYYYYYYYYYYYYYYYYYYFUYGYFYjjkl
print("Do'stlariz yoshini saqlaymiz")
friends = {}
ishora = True
while ishora:
    ism = input("Do'stingizni ismini kiriting:")
    yosh = input("Do'stingizni yoshini kiriting: ")
    friends[ism] = int(yosh)
    
    answer = input("Yana do'stizni kriitishni hohlaysizmi(ha\yo'q): ")
    if answer.lower()  == "ha":
        continue
    else:
        ishora = False
print("Do'stlariz ro'yhati")
for k,v in friends.items():
    print(f"{k.title()}ning yoshi: {v}")
##################################LK:K:K:############L:KK:K:#################:LL::
"""                         RO'YXAT ELEMENTLARINI O'CHIRISH
Avvalgi darslarimizning birida ro'yxat elementini o'chirish uchun .remove(qiymat)
 metodi bilan tanishgan edik. Esingizda bo'lsa, bu metod ro'yxatdan eng birinchi
 uchragan qiymatni o'chiradi. Agar ro'yxatimizda ma'lum bir qiymat bir necha bor
 takrorlangan bo'lsa, ularning barchasini o'chirib tashlash uchun while tsiklidan
 foydalanishmiz mumkin.                                  """
cars = ['matiz', 'cobalt','nexia', 'treker', 'cobalt','captiva','spark','cobalt', 'malibu']
car = 'cobalat'
while car in cars:
    cars.remove(car)
    
print(cars)

#Yuqoridagi tsikl toki cars degan ro'yxatda 'nexia' qiymati tugagunga qadar takrorlanaveradi.


for car in cars: #
    if car.lower() == 'cobalt':
        cars.remove(car)
print(cars)


###################################################################################
'''                           'RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH
Quyidagi misolni ko'raylik. Bizda talabalar ro'yxati bor. while tsikli toki 
ro'yxatda talabalar bor ekan aylanaveradi. Tsikl ichida biz .pop() metodi 
yordamida talabaning ismini ro'yxatdan sug'urib oldik va foydalanuvchidan 
talabani baholashni so'radik. Talabaning ismi va bahosini lug'at elementi
ko'rinishida saqlab qo'ydik (talaba - kalit, baho - qiymat).     '''
students = ['ali', 'vali' , 'salim', 'hasan']
baholanganlar = {}
while students:
    talaba = students.pop()
    grade = input(f"{talaba.title()}ning bahosini kiriting: ")
    baholanganlar[talaba] = grade
    print(f"{talaba.title()} baholandi")
    
#Yuqorida biz while tsikli yordamida ro'yxat va lug'atlar ustida bajarish mumkin 
#bo'lgan ba'zi misollarni ko'rdik. Albatta dasturlash davomida bundan boshqa holatlar 
#ham uchrashi tabiiy. 


#######################################################################################################################   

#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir
# qabul qilib, yangi ro'yxatga joylang.
mahsulot = []
while True:
    savol  = "Add a product in your basket: "
    product = input(savol)
    mahsulot.append(product)
    question = input("are you going to add a product (yes/no): ")
    if question.lower() == 'yes':
        continue
    else:
        break
#######################################################   

mahsulot={
    'olma':5000,
    'behi':8000,
    'banan':20000
    }
product = ['behi','shaftoli','banan','anor']

while product: 
    buy = product.pop()
    if not buy in mahsulot.keys():
        print(f"bizda {buy} mahsulot tugagan.")
    else:
        print(f"{buy} mahsulotimizning narxi: {mahsulot[buy]}")
        


print("Xaridingiz uchun rahmat!")































    