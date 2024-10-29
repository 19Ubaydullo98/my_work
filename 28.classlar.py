# 28 - Dars Class 
# Biz oldin ham classlar bilan ish bajarganmiz 
x  = 10 
print(type(x))# natija <class "int">  shu holatda bunda x  int degan klassga tegishli
matn = "Assalomu Aleykum"
print(type(matn)) # matn string clasiga tegishli ekan 
## bularnig o'ziga tegishli metodlari bor string int yoki raqamlarga tegishli 
print(matn.upper())# string clasining funksiyalaridann biri upper metodi edi 
print(matn.capitalize())
print(matn.lower()) # va hokazo 
# har bir class yoki obyektnni o'ziga yarasha funksiyasi bo'ladi biz unni method deymiz
# bi bu metodlarga nuqta orqali murojat qilamizz 

"print(x.capitalize()) "# biz stringga tegishli all metodlarnni boshqa classga qo'llay olmasligimiz mumkin 
 
########################################keling bir funksiya yaratamiz
def  hello():
    print("Assalomu aleykum")
print(type(hello))# natija #<class "function"> biz funksiya degan natija berayapti 

###################################################= KLASS YARATISH
# Biz qanday qilib o'zimizni obyektimizni yaratib olamiz. BUning uchun biz 
# bitta klass yaratib olamiz va bu class obyekt uchun shablon vazifasini bajaradi 

class Talaba:  # bu klasnnign nomi talaba iloji bo'lsa clasning nomini kattada yozish kerak 
    # classnning hususiyatlari va metodlari bor degan edik     buni quyidagicha bajaramiz
    # buning ismi, familyasi, tug'ilgan yili, bor 
    def __init__(self,ism,familya,t_yil):
        self.name = ism
        self.surname = familya
        self.date = t_yil
    
    def get_name(self):
        return self.name
    
    def get_age(self,yil):
        return (yil - self.date) # bu yerda get_age(2024)ga o'xshab murojat qilinadi 
        
    def get_surname(self):
        return self.surname
    
    def tanishtir(self): # bu yerda funksiya ichida print berishimiz yaxshimas 
        print(f"Mening ismim {self.name} {self.surname},tug'ilgan yilim {self.date}")
        return (f"Mening ismim {self.name} {self.surname},tug'ilgan yilim {self.date}")
    
"""1___Talaba — Talaba nomli klass yaratdik. Klasslarga nom berishda uning birinchi 
harfini katta harfdan boshlash tavsiya qilinadi. Agar klass nomi 2 va undan ko'p
 so'zdan iborat bo'lsa har bir so'zni katta harf bilan boshlang.
2____def __init__(self) — klassga tegishli xususiyatlarni saqlovchi maxsus metod (funksiya).
 self kalit so'zi ingliz tilidan "o'zi" deb tarjima qilinadi, va bu klassdan yaratilgan
 obyektning o'ziga ishora qiladi. Ya'ni keyinchalik biz obyekt ichidagi metodga 
 murojat qilganimizda shu obyektning o'zi birinchi bo'lib funksiyaga argument 
 sifatida uzatiladi, obyket ustida turli amallar bajarish imkonin beradi
3____def __init__(self,ism,familiya,tyil) — yaratayotgan klassimizga xos xususiyatlarni
 def __init__(self) funksiyasiga argument sifatida uzatamiz. Bizning Talaba klassimiz 
 ism, familiya va tug'ilgan yilga ega bo'ladi. 
3____Keyingi qatorlarda esa self.xususiyat = argument komandasi yordamida uzatilgan
 argumentlarni klassning xususiyatlari bilan bo'glayapmiz. Bu yerda xususiyat nomi 
 uzatilgan argument nomi bilan mos tushishi shart emas, unga istalgan nom berishimiz
 mumkin (masalan self.name = ism) """
######################KLASSDAN OBYEKT YARATAMIZ        klasdan obyekt yaratamiz 
talaba1 = Talaba("Hasan", "Karimov", 2004)  
#######################KLASSDAN BIR NECHTA OBYEKTLAR YARATISH
talaba2 = Talaba("Olim", "Soatov", 2012)
talaba3 = Talaba("Umid", "Olimov", 1998)
########################################    OBYKETNING XUSUSIYATLARINI KO'RISH
# Mana, talaba1 obyektimiz tayyor. Obyektni yaratish uchun Talaba klassiga murojat
# qildik va talabaning ismi, familiyasi va tug'ilgan yilini parameter sifatida uzatdik. 
print(talaba1.name)
print(talaba1.surname)
print(talaba1.date)
print(type(talaba1))
#Obyektning xususiyatlarini ko'rish uchun nuqta orqali murojat qilishimiz mumkin.

print(talaba1.tanishtir())
##### as  gett nameni sinab ko'raman 
print(talaba1.get_name())
###### get_age ni sinab ko'rish 
print(talaba1.get_age(2024))
###### get_surname ni sinab ko'ramiz 
print(talaba1.get_surname())

#####################################################  pass OPERATORI
"""Pythonda hech qanday vazifani bajarmaydigan pass operatori mavjud. Bu operatordan 
bo'sh metodlar yaratishda foydalanish mumkin. Misol uchun siz klassingiz uchun 
muhim metodlarni bilasiz, lekin metod badani hali tayyor emas. Agar metod badanini 
bo'sh qoldirsangiz, Python IndentationError xatosini qaytaradi. Shunday xolatlarda, 
funksiya badaniga pass operatorini qo'yib ketishimiz mumkin: """
    # def get_email(self):
    #     pass
#pass operatoridan if-else, for, while operatorlari badanida ham foydalanish mumkin.



###############################################################################
# Amaliiyot
###############################################################################
class user:
    def __init__(self,ism,familiya,t_yil,email,login,password,phone):
        self.name = ism
        self.surname = familiya
        self.date = t_yil
        self.login= login
        self.password = password
        self.phone = phone
        self.email = email
#### endi hususiyata yaratamiz 
    def get_info(self):
        return f"Foydalanuvchi: {self.name.title()} {(self.surname).title()},\nemail: {self.email},\nlogin: {self.login}, and pasword: {self.password}"

    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_date(self):
        return self.date
    def get_login(self):
        return self.login
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    def get_phone(self):
        return self.phone
    def get_age(self, yil):
        return yil - self.date


user1 = user("Ubyaydullo", 'Obidjanov', 1998,"Ubaydullo@gmail.com", "19Ubaydullo98", "FA7313898", "+998942750737")  
##^^^^ klassga obyekt yaratdik
user2 = user("Ahmadsher", "Jo'raboyev", 1999,"Ahmadsher@gmail.com","19Ahmadsher99", "AJ7313898", "+99893101334")  
print(user1.get_info())
print(user2.name)
print(user1.date)
print(user1.get_age(2024))
print(user2.get_date())
print(user2.get_info())
print(user1.get_login())
print(user2.get_password())







        