# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 23:14:04 2023

@author: Ubaydullo-PC
"""""""

FUNKSIYA NIMA?
Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi. Biz 
shu paytgacha bir nechta tayyor funksiyalardan foydalanib keldik. Misol uchun 
print() funksiyasi konsolga matn chiqarish uchun, range() funksiyasi esa ma'lum 
oraliqdagi sonlarni yaratish uchun ishlatiladi.  
 # biz bitta dasturimizda bir necha marta ishlatadigon kodlarimiz keladigon bo'lsak
 # consolga: x= 12 type(x) list(range(10)) shunga o'xshagan funksiyalardan foydalandik
 
 '
Aslida har qanday funksiyaning ortida ham bir necha qatordan iborat kod bo'ladi, 
lekin biz funksiyaga murojat qilganda uning nomini yozamiz xolos. Funksiya ortidagi 
kod esa biz uchun yashirin bo'lib qolaveradi. Funksiyalarning qulayligi ham shunda. 
Dastur davomida ma'lum bir kodlarni qayta-qayta yozmaslik uchun biz ularni jamlab, 
bitta funksiya ichiga joylashimiz va dastur davomida bu kodlarga funksiya nomi
 orqali murojat qilishimiz mumkin. 
 
 
Funksiyalar turlicha bo'ladi, ba'zi funksiyalar sizdan qiymat qabul qilib, 
konsolga biror ma'umot chiqaradi, ba'zilari esa sizdan qabul qilgan qiymat 
ustida turli amallar bajarib yangi qiymat qaytaradi. Foydalanuvchidan mutlaqo 
qiymat qabul qilmaydigan funksiyalar ham mavjud. 


Ushbu mavzuda siz qanday qilib Pythonda yangi funksiya yaratish, unga murojat 
qilish, tekshirish va to'g'rilashni o'rganasiz. Shuningdek darsimiz yakunida 
dasturimizni bir nechta faullarga ajratishni va funksiylarani alohida, module 
deb ataluvchi fayllarga joylashni ham o'rganamiz.                      """
############################################################
"""                               FUNKSIYA YARATAMIZ
Keling oddiy, salom_ber deb nomlangan funksiya yaratamiz. Bu funksiya murojat 
qilganimizda konsolga "Assalom alaykum!" degan xabarni chiqarsin.                                       """

def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")
    
# keling tahlil qilaylik: 
    # def funksiya yarataotganimizni belgisi 
    # so'ng funksiyaga nom berdik
    # izoh funksiya uchun 
    # va funksiyamizni asosiy qismi "Assalomu aleykum " degan so'zni consolga chiqaradi 
    #    bizning funksiyamiz qiymat qabul qilmaydi, shuning uchun qavslar ichi bo'sh
    
#Funksiyaga nom berishda fe'l, ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan 
#foydalaning. Bu bilan siz o'zgaruvchi va funksiya o'rtasini farqlashingiz 
#oson bo'ladi. Misol uchun, yuqorida biz funksiyamizni salom emas salom_ber deb nomladik.
"""ARGUMENT VA PARAMETER
Funksiya yaratishda, qavs ichida berilgan, funksiya to'g'ri ishlashi uchun
uzatiladigan qiymat parameter deb ataladi. Yuqoridagi misolda ism bu salom_ber
 funksiyasining parametri. 
Foydalanuvchi funksiyaga murojat qilishda funksiyaga uzatgan qiymat esa argument
 deb ataladi. salom_ber('hasan') kodida 'hasan' bu argument.                           """
 
"""⭕️"Ba'zi manbalarda yoki darslarda argument va parametr so'zlari almashtirib
 ishlatilishi ham kuzatiladi.           """
###################################################################################
"""                     FUNKSIYAGA QIYMAT UZATISH
Avvalgi sodda funksiyamiz foydalanivchidan hech qanday qiymat olmaydi va barchaga 
birday "Assalomu alaykum!" deb javob qiladi. Keling funksiyaga o'zgartirish kiritamiz, 
foydalanuvchi ismini qabul qilib, unga ismi bilan murojat qilsin. Buning uchun 
funksiya nomidan keyin, qavs ichida foydalanuvchi berishi kerak bo'lgan qiymatni ko'rsatamiz.     """

def say_hello(ism):## ism degan o'zgaruvchi qandaydir qiymat kutadi 
    """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya yaratamiz"""
    print(f"Assalomu aleykum, hurmatli {ism.title()}!")
    
say_hello("ubaydullo")# fun_miz ubaydulloni oladida ismga qiymat qilib beradi 
name = "Azimjon"
say_hello(name)# fun_miz name degan o'zgaruvchini yuqoridagi ismga tenglab qo'yadi 
# agar funksiyamizga qandaydir qiymat bermasak bu funksiya hatolik chiqaradi 
#
#say_hello()  #TypeError: say_hello() missing 1 required positional argument: 'ism'
 
#########################%$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""                          DOCSTRING
Avval aytganimizdek, funksiya yaratganda, funksiya qanday ishlashi haqida qisqacha
ma'lumot berib ketish o'zimiz uchun ham, kelajakda bizni funksiyamizni ishlatadigan
 boshqa dasturchilar uchun ham juda foydali bo'ladi. Quyidagi funksiyaning 2-qatorda
 biz funksiya haqida ma'lumot berdik. Bu qator docstring deyiladi. Murakkab funksiyalar
 uchun docstringni bir necha qatorga bo'lib yozishingiz mumkin """

def say_hello(ism):## ism degan o'zgaruvchi qandaydir qiymat kutadi 
    """Foydalanuvchi ismini qabul qilib,
    unga salom beruvchi funksiya"""  # bu funksiyamiz uchun tarif 
    print(f"Assalomu aleykum, hurmatli {ism.title()}!")

#Xo'sh, bu ma'lumot qachon va qayerda ko'rsatiladi? Dastur yozish jarayonida
#funksiya nomini yozishingiz bilan, docstring ko'rsatiladi:
# ko'p funksiyalarimda bu narsa chiqqan lekin e'tibor bermaganmiz masalan 
# print() shu qo'shtirnoqni yopishimiz bilan bizga print haqida ma'lumot beradi 
# misol uchun type() , list(), range(), va hakozo..........
#say_hello()  # huddi shu ko'rinishda ma'lumot olinadi 
# funksiyamiz izohini consolga chiqarish uchun print(funksiya_nomi.__doc__)shu ko'rinishda bo'ladi
print(say_hello.__doc__)  ## shu ko'rinishda bo'ladi 

###################################################################
"""FUNKSIYAGA BIR NECHA BOR MUROJAT QILISH
Funksiya yaratishning asl maqsadlaridan biri, biz unga qayta-qayta, yangi qiymatlar
 bilan murojat qilishimiz mumkin.                               """
say_hello("Islomjon")
say_hello("diyorbek")

##############################################################################
"""FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH
Shunday funksiyalar bor, bir emas bir nechta parameter talab qilishi mumkin,
foydalanuvchi esa o'z navbatida bir nechta argumentlar taqdim qilishi kerak.
 Funksiyaga argument uzatishning bir necha usuli bor, keling ular bilan birma
 bir tanishamiz.         """
 ###########################################################################
""" TO'G'RI TARTIBDA UZATISH
Bu usulda, funksiya parametrlari qaysi tartibda yozilgan bo'lsa, argumentlar
 ham aynan shu ketma-ketlikda uzatilishi kerak. Keling bitta misol ko'ramiz.
 Quyidagi funksiya foydalanuvchining ismi va familiyasini parametr sifatida
 qabul qilib, ularni jamlab xabar chiqaradi.            """

def salom__ber(name, surname):
    """Foydalanluvchi ismini va familyasini qabul qilib 
    unga salom beruvchi funksiya """
    print(f"Foydalanuvchi ismi: {name.title()}\n"
          f"Foydalanuvchi familyasi: {surname.title()}")
    
salom__ber("hoshimjon","Erkinov")# lekin argumentni noto'g'ri bersak natija 
# biz istagandek chiqmasligi aniq familya o'rinida ism, ism o'rnida familya
#Ko'p xolatlarda esa, argumentlarni noto'g'ri tartibda uzatish xatolikka ham
#olib kelishi mumkin.
def yosh_hisobla(ism, t_yil):
    "Foydalanuvchi yoshini hisoblaydigan funksiya "
    print(f"{ism.title()} {2023-t_yil} yoshda")
    
yosh_hisobla("Ubaydullo", 1998)
#yosh_hisobla(1998,"ubaydullo")  # ism bilan yoshni o'rni almashib qolyapti 
# natija:AttributeError: 'int' object has no attribute 'title' 
###############################################################################
"""                       KALIT SO'Z BILAN UZATISH
Yuqoridagi kabi holatlarning oldini olish uchun argumentlarni parametr nomi bilan 
qo'shib uzatishimiz mumkin. Buning uchun funksiyaga o'zgartirish kiritish talab qilinmaydi.        """

yosh_hisobla(t_yil=2010, ism = "Bahodir")
#Kalit so'z usulidan foydalanganda parametr nomi to'g'ri yozilganiga ahamiyat bering.
 
#                         STANDART QIYMAT
""" Funksiya yaratishda, istalgan parametr uchun standart qiymat ko'rsatib 
ketishimiz mumkin. Agar foydalanuvchi shu parametr uchun qiymat (argument) 
kiritmasa, funksiya bajarilishi jarayonida standart qiymat ishlatiladi. Standart 
qiymatni funksiya yaratish vaqtida parametr = qiymat ko'rinishida beriladi.         """
def yosh_hisobla(t_yil, joriy_yil = 2023):
    """foydalanuvchi ylidan foydalanib unga yoshini qaytaruvchi dastur"""
    print(f"Siz {joriy_yil - t_yil} yoshdasiz")
 
yosh_hisobla(25, 2023)
yosh_hisobla(69)

#Funksiya yaratishda, standart qiymatga ega parametrlar doim oxirida yozilishi 
#kerak. Aks holda xatolik yuzaga keladi.

#########################################################################
"""         FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR
Funksiyalarga murojat qilishda turli xatoliklarga yo'l qo'shimiz tabiiy.
 Bunday holatlarda Python qaytargan xatoni sinchiklab o'qib, xato qayerdaligini
 topishimiz va uni to'g'rilashimiz zarur. Quyida men avvalroq yaratgan 
 funksiyalarimizni xato usullar bilan chaqiraman. Xato nimada ekanini topa olasizmi?"""
 

def tugilgan_yil(ism, t_yil):
    "oydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya "
    print(f"Hurmatli {ism.title()} siz {2023-t_yil} yilsiz")
name= input("Ismingizni kritiing: ")
yosh = int(input("Yoshingizni kriting: "))
tugilgan_yil(name, yosh)

def kvad_kub(son):
    "Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya "
    print(f"{son} ning kvadrati {son**2} kubi esa {son**3}")

number = int(input("Son kiriting: "))
kvad_kub(number)
 
def toq_juft(son):
    "foydalanuvchidan son qabul qilib uni toq yoki juft ekanligini aniqlovchi funksiya"
    if son%2 == 0:
        print("Siz kiritgan son juft!")
    else:
        print("Siz kiritgan son toq!")
        
a = int(input(f"Son kiriting: "))
toq_juft(a)

def katta_kichik(a,b):
    "foydalnuvchidan ikkita son olib uni solishtiruvchi funksiya"
    if a>b:
        print(f"{a} katta {b} dan")
    elif a<b:
        print(f"{b} katta {a} dan")
    else:
        print("Siz kiritgan sonlar bir birig teng!")
    
num_1 = int(input(f" Birinchi sonni kiriting: "))
num_2 = int(input("Ikkingchi sonni kriiting: "))
katta_kichik(num_1, num_2)


        