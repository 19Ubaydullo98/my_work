# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:18:50 2024

@author: Ubaydullo

XUSUSIYATLARGA STANDART QIYMAT BERISH
Avvalgi darsizmida biz klass yaratish, unga xususiyatlar va metodlar qo'shishni 
ko'rdik. Klassdan obyekt yaratganimizda esa uning xususiyatlarini parametr sifatida 
uzatishni o'rgandik.
Pythonda obyektning ba'zi xususiyatlarini parametr yordamida uzatmasdan, klass 
yaratishda unga standart qiymat berib ketishimiz mumkin. Keling, Talaba klassimizga
qaytamiz. Bu klassimiz 3 ta xususiyatga ega edi: ism, familiya, tyil. Biz yana 
bitta qo'shimcha, bosqich nomli xususiyat qo'shamiz, va unga standart qiymat sifatida
1 beramiz, e'tibor qiling bu xususiyat obyekt yaratilishida parametr sifatida uzatilmaydi:"""

class Talaba:
    def __init__(self,ism, familiya, t_yil):
        self.ism=ism
        self.familiya = familiya
        self.t_yil = t_yil  # bu avvalgi darsimizdagi class edi
        self.kurs = 1  # standart qiymat berish 
    def set_kurs(self,kurs):
        self.kurs = kurs
    def update_kurs(self):
        self.kurs +=1 
    def get_name(self): # shu orqali murojaat qilish 
        return self.ism 
    def get_info(self):
        "Fanga yozilgan Talabalar haqida ma'lumot"  
        return f"{self.ism} {self.familiya}, {self.kurs}-bosqich talabasi"
    

talaba1 = Talaba("Hayotbek", "Nosirjanov", 2000)
print(talaba1.ism)     ##### bu holda murojat qilish hato hisoblanadi. yoki meetod orqli 
print(talaba1.get_name())## bu esa to'g'ri 
print(talaba1.kurs)
####Obyektning standart qiymatiga ham boshqa xususiyatlar kabi nuqta orqali 
#murojat qilishimiz va uning qiymatini almashtirishimiz mumkin:
# talaba1.kurs = 2   #Yana boshqa usuli, obyekt xususiyatini yangilovchi metod yozish yuqorida 
print(talaba1.kurs)
talaba1.set_kurs(3)
print(talaba1.get_info()) # yangi metod asosida 
talaba1.update_kurs()
print(talaba1.get_info()) ## bu yana boshqa metod 

#################################### yangi klasss
# byektga yo'naltirilgan dasturlashning afzalligi, turli obyektlar o'rtasida o'zaro
# munosabatlarni oson yo'lga qo'yish mumkinligida. Buni misolda ko'rish uchun, 
# yangi Fan degan klass yaratamiz va fanimizga talabalar qo'shish imkoniyatini 
# ham yaratamiz (add_student() metodi):
class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni=0
        self.talabalar =[]
        
    def add_talaba(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
    def get_talaba(self): # agar buni doimgi usulda qilganimizda pastda misol ko'rsatilgan 
        return [student.get_name() for student in self.talabalar ]
        # talaba = []  bu sal qiyinroq usuli 
        # for n in self.talabalar:
        #     talaba.append(n.get_name())
        # return talaba
    def get_info_student(self):# agar chiziqli dasturdan foydalangannimizda pastda tushuntirilgan 
        return list(talaba.get_info() for talaba in self.talabalar)
#talaba_ism = "Vali"
#talaba_familiya = "Oripow" bularnni hammasini yozib chiqib undan keyin bir biriga 
#  bog'lash juda qiyin bo'lgan bo'lar edi 
  
    
    
     
    # keling yangi obyektlar yaratamiz 
matematika = Fan("matematika")
talaba2= Talaba("Ubaydullo","Obidjanov", 1998)
talaba3 = Talaba("Jo'raboyev","Ahmadsher",1999)
matematika.add_talaba(talaba1)
matematika.add_talaba(talaba2)
# print(matematika.nomi)
# print(matematika.talabalar_soni)
# print(matematika.talabalar) #natija: [<__main__.Talaba object at 0x0000028E7AF50990>, <__main__.Talaba object at 0x0000028E7AF29650>]
# bunda ikkita obyekt bor bularnni quyidagicha chiqaramiz . lekin tavsiya qilmaymiz
# print(matematika.talabalar[0].get_name()) 
# print(matematika.talabalar[1].get_info())# qo'pol usul 
########^^^ buning uchun yuqorida get_talaba degan metod yaratamiz
print(matematika.get_talaba())
print(matematika.get_talaba()[1]) # huddi shu tarzda chiqishi to'g'riroq

mat_talabalar = matematika.get_info_student()
print(mat_talabalar)
#Shunday qilib biz ikki bir-biriga bog'liq bo'lmagan obyektlar ustida turli 
#munosabatlar o'rnatishimiz mumkin.
##########################################
# NUQTA YOKI METOD?
#########################################
"""Dasturchilar orasida obyektning xususiyatlarini o'zgartiradigan metodlarni 
set (o'zgartir) so'zi bilan, xususiyatlarni qaytaradigan metodlarni esa get (olish)
so'zi bilan boshlash qoida qilib olingan. Masalan: set_name() va get_name() kabi."""
# Fan klasimizni ko'rinishini o'zgartiradigan bo'lsak quyidagicha bo'ladi
        
        
        
########################################
# OBYEKTNING XUSUSIYATLARI VA METODLARINI KO'RISH
######################################
"""Obyektlar bilan ishlaganda, o'z-o'zidan shu obyektga tegishli xususiyatlar va 
metodlarni bilish talab qilinadi. Agar obyekt tegishli bo'lgan klassni o'zimiz 
yaratgan bo'lsak, istalgan payt klass ichini ko'rib olishimiz mumkin. Lekin boshqalar 
yaratgan klass haqida ma'lumot olish talab qilinsa, buning bir nechta yo'li bor.    
dir() FUNKSIYASI
dir() funksiyasi yordamida istalgan obyekt yoki klassning xususiyatlari va 
metodlarini ko'rib olishimiz mumkin:     """ 
print(dir(Talaba))
print(dir(Fan))


"""Lekin bunda har bir klass bilan keluvchi maxsus dunder metodlar ham chiqib
keldi. Dunder metodlar ikki pastki chiziq (__) bilan boshlanadi va maxsus holatlar 
uchun saqlab qo'yilgan. Biz hozircha faqat __init__ metodi bilan tanishdik, 
qolganlari bilan keyingi darslarimizda yana ko'rishamiz. Dunder metodlardan 
keyin esa biz murojat qilishimiz mumkin bo'lgan metodlar ro'yxati kelgan.

<<<Dunder — double underscore (ikki pastki chiziq) so'zlarining qisqartmasi.>>>   """
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))


# Agar dir() funksiyasiga klass emas, obyekt uzatsak metodlardan tashqari xususiyatlar
# ham kelib chiqadi 
print(dir(talaba1))

###################################$%   __dict__ 
#metodi Yuqorida zikr qilingann dunder metodlaridan biri bu __dict__
# metodi bo'lib bu metod obyektning xususiyatlarinni lug'at ko'rinishida qaytaradi:
print(talaba1.__dict__)
##################################################
################################################## HOMEWORK
class Avto:
    def __init__(self, model,rang,narh):
        self.model = model
        self.rang = rang
        self.narh = narh
        self.korobka = "avomat"
        self.kilometr = 0
        self.yil = 2023
        
    def get_model(self):
        return self.model

    def get_colour(self):
        return self.rang
    
    def get_korobka(self):
        return self.korobka
    
    def get_cost(self):
        return self.narh
    
    def get_km(self):
        return self.kilometr
    
    def get_year(self):
        return self.yil 
    
    def get_info(self):
        return f"{self.yil} {self.model}, rang: {self.rang}, Narx: {self.narh}"
        
    def set_korobka(self,karobka):
        self.korobka = karobka
    def set_km(self,kilometr):
        self.kilometr = kilometr
    def update_km(self):
        self.kilometr +=1
    def set_year(self,yil):
        self.yil = yil
    def updat_year(self):
        self.yil +=1 

moshna1= Avto("matiz", "oq", "5400$")    
    
print(moshna1.get_model())    
class Salon :
    def __init__(self,s_nomi,s_manzil, s_tel):
        self.name = s_nomi
        self.adress = s_manzil
        self.car = []
        self.phone = s_tel
        self.saled = []
    def add_car(self, moshna):
        self.car.append(moshna)
    
    def get_info(self):
        return list(n.get_info() for n in self.car)
    #     n=0
    #     while True:
    #         print("Avtasalonga avto qo'shish:")
    #         a = input(f'{n}-avtomobilni qo\'shinng \n>>>')
    #         n +=1
    #         self.s_car.append(a)
    #         chiqish = input("Yana avtomobil qo'shmoqchimisiz No/Yes : ")
    #         if chiqish.lower() == "no":
    #             break 
    #         else:
    #             continue
            

salon = Salon("Shevrolet", "Sergeli_bozori", "+998941234567")
moshna2 = Avto("malibu", "qora", "35000$")
moshna3 = Avto("spark",'oq', "10500$")
salon.add_car(moshna1)
salon.add_car(moshna2)
salon.add_car(moshna3)

print(salon.adress)
print(salon.get_info())

#####
print(dir(Avto))
print(dir(Salon))
print(Salon.__dict__)
print(moshna1.__dict__)


        
        
        
    
    
    
    
     
        



