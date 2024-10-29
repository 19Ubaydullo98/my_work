# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 22:25:18 2024

@author: Ubaydullo
"""
from uuid import uuid4

class Shaxs:
    def __init__(self,ism, familiya, pasport, tyil):
        """Shaxsning hususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil
        self__id = uuid4()

    
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"Pasport: {self.pasport}, {self.tyil}-yilda tug'ilgan"
        return info 
    def get_age(self, yil):
        """Shaxsni yoshini qaytaruvchi funksiyasi"""
        return (yil - self.tyil)

inson = Shaxs("Ubaydullo", "Obidjanov", "FA7313898", 1998)
print(inson.get_age(2024))
print(inson.get_info())
print(inson.get)
 

# # VORIS KLASS YARATISH
# # Endi avvalgi darsimizda yaratgan Talaba klassimizni qaytadan yaratamiz. Bu 
# # safar, avvalgidan farqli ravishda, Talaba ni yaratishda, Shaxs dan super klass 
# # sifatida foydalanamiz:
    

# class Talaba(Shaxs):   # talba voris class ,,, shaxs esa super class 
#     """Talaba clasi """
#     def __init__(self,ism,familiya,pasport, tyil,  ):
#         """Talabaning hususiyatlari"""
#         super().__init__(ism,familiya,pasport,tyil)  #5-qatorda (def __init__ ichida) klassimiz super klassning xususiyatlarini meros olishini ko'rsatdik 
#         # self.id = Id
#         # self.bosqich = 1
# talaba = Talaba('Ali', "Valiyev", "AA9359240", 1998)
# print(talaba.get_info()) # Talaba klasida get_info metodi mo'lmasa ham chiqardi.
# class Talaba(Shaxs):   # talba voris class ,,, shaxs esa super class 
#     """Talaba clasi """
#     def __init__(self,ism,familiya,pasport, tyil, Id):
#         """Talabaning hususiyatlari"""
#         super().__init__(ism,familiya,pasport,tyil)  #5-qatorda (def __init__ ichida) klassimiz super klassning xususiyatlarini meros olishini ko'rsatdik 
#         self.id = Id #s hususiyat qo'shayapmiz 
#         self.bosqich= 1
        
       
#     def get_id(self):
#         """Talabani id raqamini oluvchi metod """
#         return self.id
    
#     def get_bosqich(self):
#         """Talabaning bosqichini oluvchi metod """
#         return self.bosqich
# # Shu zayilda yangi klassimizga istalgancha yangi xususiyatlar va metodlar 
# # qo'shishimiz mumkin. Bunda, agar yangi xususiyat yoki metod super klassga ham 
# # aloqador bo'lsa uni birdan super klassga qo'shish tavsiya qilinadi.
# ############### <<< voris klass boshqa klass uchun super klass bo'lishi mumkin >>>####################


# # POLIMORFIZM — SUPER KLASS METODLARINI QAYTA YOZISH
# # Voris klassga super klassdan meros qolgan istalgan metodni qayta talqin qilish 
# # mumkin. Avvalgi misolimizdagi get_info() super metodini ko'raylik, bu metod 
# # talabaning ismi, familiyasi, passport raqami va tug'ilgan yilini qaytaradi:
#     def get_info(self):
#        """Shaxs haqida ma'lumot"""
#        info = f"{self.ism} {self.familiya}."
#        info += f" Id raqam:{self.id}, {self.bosqich} - bosqich. "
#        return info 
# talaba1 = Talaba("Odiljon", "Obidjanov", "AA4567913", 2002," CB002349")
# ### super va voris klassdagi bir hil metodnni ko'ramiz 
# print(talaba.get_info())   # super klassga tegishli metod     
# print(talaba1.get_info()) # 

# ##################### OBYEKT ICHIDA OBYEKT
# ##################################################
# """Ba'zida klassimiz xususiyatlar 
# va ular bilan ishlaydigan metodlarga to'lib ketishi, bu esa o'z navbatida obyektga 
# murojat qilishni qiyinlashitirishi mumkin. Shunday holatlarda ba'zi xususiyatlarni
#  alohida klass ko'rinishida yozish va keyinchalik bu klassdan yaratilgan 
#  boshqa obyektning xususiyati sifatida foydalanish mumkin.
 
# Misol uchun, yuqoridagi Shaxs klassimizga yana bir manzil degan xususiyat qo'shaylik.
#  Odatda manzil bir nechta qismlardan iborat bo'ladi (xonadon, ko'cha, mahalla, 
#  tuman/shahar, viloyat, indeks va hokazo) va ularning har biri uchun Shaxs ichida
#     alohida xususiyat yaratmasdan, alohida manzil degan klassga yuklash maqsadga 
# muvofiq bo'ladi."""
# class Talaba(Shaxs):   # talba voris class ,,, shaxs esa super class 
#     """Talaba clasi """
#     def __init__(self,ism,familiya,pasport, tyil, Id, manzil ):
#         """Talabaning hususiyatlari"""
#         super().__init__(ism,familiya,pasport,tyil)  #5-qatorda (def __init__ ichida) klassimiz super klassning xususiyatlarini meros olishini ko'rsatdik 
#         self.id = Id #s hususiyat qo'shayapmiz 
#         self.bosqich= 1
#         self.manzil  = manzil
        
       
#     def get_id(self):
#         """Talabani id raqamini oluvchi metod """
#         return self.id
    
#     def get_bosqich(self):
#         """Talabaning bosqichini oluvchi metod """
#         return self.bosqich
#     #############################################
# class Manzil:
#     def __init__(self,viloyat, tuman, street, uy):
#         self.viloyat = viloyat
#         self.tuman= tuman
#         self.street = street
#         self.uy = uy 
    
#     def get_manzil(self):
#         manzil = f"{self.viloyat}-viloyati, {self.tuman}-tumani,"
#         manzil += f" {self.street} - ko'chasi, {self.uy} - uy "
#         return manzil
# # Keling endi talaba obyektini boshqa yaratamiz
# talaba_manzil  = Manzil("Namangan","Chortoq", "Barhayot", 64)
# print(talaba_manzil.get_manzil())
# talaba1 = Talaba("Odiljon", "Obidjanov", "AA4567913", 2002," CB002349", talaba_manzil)
# # print(talaba1.manzil)
# print(talaba1.manzil.get_manzil()) # bu holatda murojat qilsa to'g'i bo'ladi 

# ####################################################################
# class Talaba(Shaxs):   # talba voris class ,,, shaxs esa super class 
#     """Talaba clasi """
#     def __init__(self,ism,familiya,pasport, tyil,  ):
#         """Talabaning hususiyatlari"""
#         super().__init__(ism,familiya,pasport,tyil)  #5-qatorda (def __init__ ichida) klassimiz super klassning xususiyatlarini meros olishini ko'rsatdik 
#         self.bosqich= 1
#         self.fanlar = []
#         self.fan_soni= 0
        
#     def fanga_yozil(self,fan):
#         self.fanlar.append(fan)
#         self.fan_soni +=1
#     def remove_fan(self,yozilgan_fan):
#         if yozilgan_fan in self.fanlar:
#             self.fanlar.remove(yozilgan_fan)
#             self.fan_soni -=1
#         else:
#             print("siz bu fanga yozilmagansiz: ")
              
        
        

# class Fan:
#     def __init__(self,nomi ):
#         self.nomi = nomi
    
        
        

# matem = Fan("matematika")
# ingliz_tili = Fan("Ingliz_tili")
# at = Fan("Informatika")

# talaba1 = Talaba("ubaydullo", "Obidjanov", "AA9359240", 1998)
# talaba1.fanga_yozil(matem)
# talaba1.fanga_yozil(at)
# print(talaba1.fan_soni)
# talaba1.remove_fan(at)
# talaba1.remove_fan(matem)
# print(talaba1.fan_soni)

# # #############################################################################
# # Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan
# #  Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)

# class Shaxs:
#     def __init__(self,ism, familiya, pasport, tyil):
#         """Shaxsning hususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.pasport = pasport
#         self.tyil = tyil
#     def get_ism(self):
#         """Shaxs ismini qaytaruvchi funksiya"""
#         return self.ism
#     def get_familiya(self):
#         "Shaxsni familiyasin qaytaruvchi funksiya"
#     def get_age(self, yil):
#         """shaxsni yoshini qaytaruvchi funksiya"""
#         return yil - self.tyil
# class Professor(Shaxs):
#     def __init__(self, ism, familiya, pasport, tyil, yutuq,talabalar_soni,ish_joyi,manzil):
#         "professorning hususiyatlari"
#         super().__init__(ism, familiya, pasport, tyil, )
#         self.yutuq = yutuq 
#         self.talabalar_soni= talabalar_soni
#         self.ish_joyi= ish_joyi
#         self.manzil = manzil 
#     def get_ism(self):
#         """Shaxs ismini qaytaruvchi funksiya"""
#         return self.ism
#     def get_familiya(self):
#         "Shaxsni familiyasin qaytaruvchi funksiya"
#     def get_age(self, yil):
#         """shaxsni yoshini qaytaruvchi funksiya"""
#         return yil - self.tyil
#     def get_manzil(self):
#         return self.manzil
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}."
#         info += f"\nPasport: {self.pasport}, {self.tyil}-yilda tug'ilgan"
#         info += f"\nHozirgacha {self.talabalar_soni} nafar o'quvchiga ta'lim bergan"
#         info += f"\nIsh joyi : {self.ish_joyi}. "
#         info += f"\nHe have been living in {self.manzil}"
#         return info
# class Manzil:
#     """Umumiy Manzil"""
#     def __init__(self, district, street,house_num):
#         self.district = district
#         self.street = street 
#         self.house_num = house_num
#     def get_adress(self):
#         return f"district: {self.district}, street: {self.street}, Number house: {self.house_num}"
# professor_manzil = Manzil("Namangan", "Bo'lon", 64)        
        
# print(professor_manzil.get_adress())        
# professor = Professor('Syuzan', "Fletcher", "AB43115", 1995, "O'zbekiston Jaloliddin manguberdi ko'krak nishoni", 853, "MXA", professor_manzil.get_adress())
# print(professor.get_info())
# print(professor.get_manzil())

# ##############WSDFGHIJ$####################################FKGHJ$##############
# class User(Shaxs):
#     def __init__(self,ism, familiya, pasport,tyil, login, password, email, phone, adress):
#         """user klasini hususiyatlari """
#         super().__init__(ism, familiya,pasport,tyil)
#         self.login = login
#         self.password = password
#         self.email = email
#         self.phone = phone
#         self.adress = adress
#     def get_login(self):
#         return self.login 
#     def get_password(self):
#         return self.password
#     def get_email(self):
#         return self.email
#     def get_phone(self):
#         return self.phone
#     def get_manzil(self):
#         return self.adress.get_adress()
#     def get_info(self):
#          """Shaxs haqida ma'lumot"""
#          info = f"{self.ism} {self.familiya}."
#          info += f"\nPasport: {self.pasport}, {self.tyil}-yilda tug'ilgan"
#          info += f"\nLogin: {self.login}, password: {self.password},"
#          info += f"\nEmail pochta: {self.email}, "
#          info += f"\nPhone number: {self.phone}"
#          info+= f"\nYashash manzili: {self.adress}"
#          return info
# foydalanuvchi_manzil = Manzil("Namangan", "Bo'lon", "64-uy")
# foydalanuvchi= User('Ubaydullo', "Obidjanov", "AA9359240", 1998, 'Ubaydullo98', "AA9359240", "Ubaydullo1940@gmail.com","+998942750737",foydalanuvchi_manzil)        

# print(foydalanuvchi.get_info())    
# print(foydalanuvchi.get_manzil())
# ##############################################################################
# class Saler(User):
#     def __init__(self, ism, familiya, pasport, tyil,login, password, email, phone, dokon, adress ):
#         """do'konchi hususiyatlari"""
#         super().__init__(ism, familiya,pasport,tyil,login, password, email, phone,adress)   
#         self.dokon = dokon
#     def get_dokon(self):
#         return self.dokon
    
#     def get_info(self):
#          """Shaxs haqida ma'lumot"""
#          info = f"{self.ism} {self.familiya}."
#          info += f"\nPasport: {self.pasport}, {self.tyil}-yilda tug'ilgan"
#          info += f"\nLogin: {self.login}, password: {self.password},"
#          info += f"\nEmail pochta: {self.email}, "
#          info += f"\nPhone number: {self.phone}"
#          info+= f"\nYashash manzili: {self.adress}"
#          return info
# sotuvchi_manzil = Manzil("Samarqand", "Registon", 56)
# sotuvchi = Saler("Hoshimjon", "obidov", "FA7313898", 1996,"hoshimjon96","H1996O", "Hoshimjon@gmail.com", "+998945000405", "chortoq dehqon Bozor", sotuvchi_manzil.get_adress())
# print(sotuvchi.get_info())
# print(sotuvchi.get_age(2024))
# print(sotuvchi.get_email())
# print(sotuvchi.get_login())
# print(sotuvchi.get_password())

# ###################################################################################
# class Mijoz(Saler):
#     def __init__(self, ism, familiya, pasport, tyil,login, password, email, phone, adress, karta_raqam,jami_puli ):
#         """Mijozning hususiyatlari """
#         super().__init__(ism, familiya,pasport,tyil,login, password, email, phone, adress) 
#         self.karta_raqam= karta_raqam
#         self.jami_puli = jami_puli
#         self.olgan_mahsulotlar = []
#     def add_mahsulot(self, maxsulot):
#         self.olgan_mahsulotlar.append(maxsulot)
#     def get_karta_raqam(self):
#         return self.karta_raqam
#     def get_jami_pul(self):
#         return self.jami_puli
#     def get_mahsulotlar(self):
#         return self.olgan_mahsulotlar

# ########################################################################################
# class Admin(User):
#     """ User klasidan foydalanuvchi klasini yaratyapmiz bu yerda super klass User"""
#     def __init__(self,ism, familiya, pasport,tyil, login, password, email, phone, adress, ):
#         super().__init__(ism, familiya, pasport,tyil, login, password, email, phone, adress)
       
        
#     def ban_user(self):
#         return f"Foydalanuvchi bloklandi"
        
# talaba = Admin("Sherbek", "Hakimov", "FA54314", 1969, "Sher69", "AAA8656", "sherbek.@gmail.com", "+998945744565", "O'zbekiston")

# print(talaba.ban_user())        
        
        
        

