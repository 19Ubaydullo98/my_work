# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:32:05 2024

@author: Ubaydullo
"""
"""                 Inkapsulatsiya 
Obyektga Yo'naltirilgan Dasturlashning tamoyillaridan biri bu inkapsulyatsiya, 
ya'ni obyektning xususiyatlarga to'g'ridan-to'g'ri (nuqta orqali) murojat qilishni 
va ularning qiymatini o'zgartirishni taqiqlab qo'yish. Pythonda bunday yopiq 
xususiyatlarning nomi ikki pastki chiziq bilan boshlanadi:                  """
from uuid import uuid4 # bizga takrorlanmas id raqam yaratib beraman 
class Avto:
    """Avtomobil klassi"""
    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km # bu inkapsulyatsiya 
        self.__id = uuid4() # bu  id har bir moshina uchun takrorlanmas id raqam
                
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
     
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish """
        self.__km+=km if km>=0 else print("Moshinani km ni kamaytirib bo'lmaydi.")    

"""Yuqoridagi kodimizning 22 n -qatorida __km xususiyati avtomobilning necha km yurgani 
haqida ma'lumot saqlaydi va bu ma'lumotni tashqaridan o'zgartirib bo'lmaydi. 
Kodimizning 12-qatorida esa har bir yangi yaratilgan avtomobilga yangi, noyob va 
takrorlanmas ID generasiya qilish uchun uuid4() funksiyasidan foydalanayapmiz. 
Deylik biz mashinalar sotish uchun onlayn bozor yaratsak, bozorimizga qo'shilgan 
har bir moshina endi o'zining ID raqamiga ega bo'ladi va bu ID raqamni to'g'ridan-
to'g'ri (nuqta orqali) ko'rib bo'lmaydi."""
avto1 = Avto("GM", "Matiz", "white", 2016, 5400, 1000)
print(avto1.make)
print(avto1.model)
print(avto1.narh)
# print(avto1.__km) ## bu hususiyatini ko'ra olmaymiz sababi bu inkapsulyatsiya 
# print(avto1.__id)  ## sababi bunga foydalanuvchi tomonidan osonlikcha o'zgartirish kiritolmaydi 
print(avto1.get_km())# bu metod orqali ko'rsak bo'ladi qiymatini 
print(avto1.get_id())

"""Bunday yopiq xususiyatlarni o'zgartirish ham metodlar orqali amalga oshirilishi 
kerak. Misol uchun mashinaning necha km yurganini o'zgartirish uchun klassimizga 
quyidagi metodni qo'shamiz:       yuqoriga qarang ^^^    """
print(avto1.get_km())
avto1.add_km(3000)
print(avto1.get_km())### natija 4000 km yurgan deb chiqayapti bu metod o'zgaruvchini o'zgartirish metodi 

#################################################
#################################################### Classga hos metod be
"""classlarning o'ziga xos metodlari ham bo'lishi mumkin. Misol uchun yuqoridagi 
num_avto xususiyatini ko'rish uchun alohida metod yozishimiz mumkin. Klassga 
oid metodlar @classmethod dekoratori bilan boshlanadi va obyektga oid metodlardan
 farqli ravishda self emas cls (class) argumentini qabul qiladi."""


class Avto:
    avto_num = 0 ## classga berilgan oddiy metod 
    __avto_num = 0 ### bu esa inklaster 
    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km # bu inkapsulyatsiya 
        self.__id = uuid4() # bu  id har bir moshina uchun takrorlanmas id raqam
        Avto.__avto_num +=1  ## classga berilgan oddiy hususiyat        
    @classmethod   # @classmethod bu maxsus dekorator. Dekoratorlar bu o'z ichiga
    # funksiya oluvchi funksiyalar. Dekoratorlar haqida keyingi darslarimizning birida batafsil to'xtalamiz.
    def get_num_avto(cls):
        return cls.avto_num
    
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

avto1 = Avto("GM", "Matiz", "white", 2016, 5400, 1000)
avto2 = Avto("GM", "cobalt", "white", 2020, 10400)
avto3 = Avto("GM", "spark", "black", 2018, 7400, 6000)
print(Avto.avto_num) # bu orqali murojat qilsak bo'ladi yoki obyekt orqali
print(avto1.avto_num) # bu orqali
print(Avto.get_num_avto())  # bu orqali yuborilishi mumkin.
#######################################################
####################################################################3
# VAZIFA
# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar 
# qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
 
class Shaxs:
    odamlar_soni = 0
    __odamlar_soni = 0
    def __init__(self,ism, familiya, pasport, tyil, yosh,pasport_id, metrka_id):
        """Shaxsning hususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil
        self.__id = uuid4()
        self.__yosh = yosh
        self.__passport_id = pasport_id
        self.__metrka_id = metrka_id
        Shaxs.__odamlar_soni +=1
    @classmethod
    def odamlarsoni(cls):
        return cls.odamlar_soni
    def get_id(self):
        return self.__id
    def get_yosh(self):
        return self.__yosh 
    def get_passport_id(self):
        return self.__passport_id
    def get_metrka_id(self):
        return self.__metrka_id
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"Pasport: {self.pasport}, {self.tyil}-yilda tug'ilgan"
        return info 
    def get_age(self, yil):
        """Shaxsni yoshini qaytaruvchi funksiyasi"""
        return (yil - self.tyil)
human1 = Shaxs("Ubaydullo", "Obidjanov", "AA9359240", 1998, 26, "FAk7313898", "sdfasd")
human1 = Shaxs("Ubaydullo", "Obidjanov", "AA9359240", 1998, 26, "FAk7313898", "sdfasd")
print(human1.odamlarsoni())

class Talaba():   # talba voris class ,,, shaxs esa super class 
    talabalar_soni = 0
    __talabalar_soni = 0
    """Talaba classi """
    def __init__(self, pasport, tyil, talaba_id, manzil ):
        """Talabaning hususiyatlari"""
        self.__id =uuid4() 
        self.__bosqich = 1
        self.tyil = tyil
        self.__pasport = pasport
        self.__talaba_id = talaba_id
        self.__manzil = manzil
        Talaba.__talabalar_soni += 1
        Talaba.talabalar_soni +=1
    @classmethod
    def get_talbalar_soni(cls):
        return cls.talabalar_soni
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
    def get_id(self):
        return self.__id
    def get_bosqich(self):
        return self.__bosqich
    def get_pasport(self):
        return self.__pasport
    def get_talaba_id(self):
        return self.__talaba_id
    def get_manzil(self):
        return self.__manzil
    
talaba1 = Talaba("FA423", 1998, "Jsfdf", "namangann")
        
print(talaba1.get_talabalar_soni())








