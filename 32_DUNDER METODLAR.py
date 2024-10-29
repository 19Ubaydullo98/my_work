# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 07:36:03 2024

@author: Ubaydullo
"""

# MAVZU DUNDER METODLAR 
## Har bir  classda o'ziga hos pythonnning metodlari bor bularni biz dir() metodi 
# orqali ko'rishimiz mumkin masalan
class Avto():   # biz bu classning metodllarini dir orqali ko'rishimiz mumkin 
    __avto_num =0
    """Avtomobil haqida metod"""
    def __init__(self,make, model, rangi, yil, narh):
        """Avtomobiga hususiyat  yuklaymiz  """
        self.make =  make
        self.model = model
        self.rangi = rangi
        self.yil = yil
        self.narh = narh
        Avto.__avto_num +=1    
    def __str__(self):  #print(avto1) deb consolega bersak bizga pastdagini chiqarib beradi 
        return f"{self.make} {self.model}"
    def __repr__(self):  ## bu ham _str_ bilan bir hil faqat bu ko'proq ommabop
        return  f"{self.make} {self.model}"

avto1 = Avto("Gm","malibu", "qora", 2022, 25000)
print(avto1.make)
# biz bu yerda print(avto1)ga consolega bersak bizga tushunarsizz narsa berishi mumkin 
print(avto1)#  endi natija quyidagicha    Gm malibu
#repr(avto10)
#str(avto1) 
#############################################Taqqoslash 
# biz to'g'rida to'g'ri pythonnda ikki obyektni taqqoslay olmaymiz ular uchun
# alohida metodlari bor bor bular __lt__, __eq__, __l__va hokazzo 
class Avto:  
    __avto_num =0
    """Avtomobil haqida metod"""
    def __init__(self,make, model, rangi, yil, narh):
        """Avtomobiga hususiyat  yuklaymiz  """
        self.make =  make
        self.model = model
        self.rangi = rangi
        self.yil = yil
        self.narh = narh
        Avto.__avto_num +=1   
    def __repr__(self):
        return f"Avto: {self.rangi} {self.make} {self.model}"
    def __eq__(self, ikkinchi_obyekt ):
        return self.narh == ikkinchi_obyekt.narh
    
    def __lt__(self, y ):
        return self.narh< y.narh
    
    def __le__(self, y ):
        return self.narh <= y.narh
    
avto1 = Avto("Gm","malibu", "qora", 2022, 25000)
avto2= Avto("Daewo","nexia","oq", 2010, 3500)
# print(avto1==avto2)
# print(avto1>=avto2)buni taqqoslash uchun biz klassga metod yozishimiz kerak bo'ladi 
print(avto1>avto2)
print(avto1==avto2)
print(avto1<=avto2)

###################################$
# OBYEKT UZUNLIGI
# Pythonda len() funksiyasi yordamida turli obyektlarning uzunligini bilishimiz mumkin, 
# misol uchun matn, ro'yxat, lug'at, set va hokazo.
class Avtosalon:
    '''Avtsalon klassi'''
    def __init__(self, nomi):
        self.nomi = nomi
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.nomi} avtosaloni"
    
    def add_avto(self, *avto):
        """bunda faqat Avto clasiga oid moshinalarni tekshirib qo'shadi """
        for avto in avto:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kriiting:")
    def __getitem__(self,index):
        """Index orqali avtoga murojat qilib keyin har bir elementni chiqaramiz """
        return self.avtolar[index]
    
    def __len__(self):
        """Salon1 klasining avtolar sonini yoki uzunligini chiqarib beruvchi funksiya"""
        return len(self.avtolar)
    def __setitem__(self,index, qiymat):
        self.avtolar[index] = qiymat
        
    def __call__(self):
        """Obyektnimizniga chaqirish uchun ishlatiladi """
        return  list(avto for avto in self.avtolar)
    def __call__(self, *qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto) # klassning ichida shunga self orqali murojat qildik
        else:
            return [avto for avto in self.avtolar]
        
        
    def __add__(self, qiymat):
        if isinstance(qiymat, Avtosalon):
            yangi_salon = Avtosalon(f"{self.nomi} {qiymat.nomi}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat, Avto):
            self.add_avto(qiymat)
        else:
            print(f"Avtosalonga {type(qiymat)} qo'shib bo'lmaydi")
        
        
salon1 = Avtosalon("Musofir")
avto3 = Avto("gm", "matiz", "qora",2016,5400)
avto4 = Avto("Gm","cobalt", "Moykriy", 2022, 13500)
print(salon1) ##AvtoSalon klassimizga __repr__metodini qo'shganimiz uchun natijamiz chiroyli ko'rinishda chiqdi.
################################################
"""Keling endi salonga avtomobil qo'shish uchun yangi add_avto() metodini yozamiz. 
Bu metodimiz Avto klassiga oid obyektlarni qabul qilishi kerak. add_avto() ga 
uaztilgan parametr Avto klassiga tegishli yoki yo'qligini tekshirish uchun maxsus
isinstance() funksiyasidan foydalanamiz.

Bu funksiya biror obyekt ma'lum klassga tegishli ekanligini tekshirish uchun ishlatiladi:"""
        
print(isinstance(salon1,Avto))  #natija: False
print(isinstance(salon1,Avtosalon)) #Natija : True 

salon1.add_avto(avto1,avto2,avto3,avto4)
# print(salon1.avtolar)
print(salon1[2])
print(salon1[0])
print(salon1[1])
print(salon1[3])
print(len(salon1)) ########salondagi elementlarni soninichiqarib beradigan funksiya 
# Endi salon1 obyektimizning elementlariga murojat qilinganda __getitem__metodi
# obyekt ichidagi avtolar ro'yxatidan ko'rsatilgan element (avtomobilni) qaytaradi.
###############################################################

# Keling endi obyekt elementlariga o'zgartirish kiritib ko'ramiz:
# salon1[0]= Avto("BMW", "X7", "qora", 2024, 97500)
print(salon1[0]) # Natija: Hatolik ko'rsatadi 
""" Endi bunga yangi set metodini qo'shishimiz kerak bo'ladi 
yuqorida __setitem__ metodini qo'yganimizdan so'ng natija: to'g'ri ko'rsata boshladi"""



###############################################"####"####"##
"""OBYEKTNI CHAQIRISH
Obyektlarni huddi funksiyalarni chaqirgandek chaqirish ham mumkin. Odatda biror 
funksiyaga murojat qilganda funksiya nomidan so'ng qavslar ochiladi va yopiladi. 
Agar funksiya argument qabul qilsa, ular qavs ichida beriladi. """

print(10)
print(len("Assalomu Aleykum"))

# biz obyektimizga hama shunday chaqirsak bo'ladi masalan salon1()
# salon() Natija: ko'ngildagidek emas

#PARAMETRSIZ CHAQIRISH
# Misol uchun, kelign yuqoridagi AvtoSalon klassiga oid obyektlar chaqirilganda 
# salondagi avtomobillar ro'yxatini ko'rsatadigan qilaylik. Buning uchu AvtoSalon 
# klassiga quyidagi metodni qo'shamiz:
""" def __call__(self):
    return list(avto for avto in self.avtolar)"""
print(salon1())

#PARAMETR BILAN CHAQIRISH
#Yuqorida salon1 ni parametrsiz chaqrishini ko'rdik. Keling endi parametr bilan 
# chaqirishni ham yo'lga qo'yaylik. Bunda, yuborilgan parametr yangi avto obyekti 
# bo'lsin, va bu parametr salondagi avtolar ro'yxatiga qo'shilsin. Metodimizni 
# quyidagicha o'zgartiramiz:
"""def __call__(self,*qiymat): ## call orqali obyekni chaqiramiz yani salon() qavslar orqali
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)  bu klassning ichida bo'layotganligi sababli 
                                     self orqali murojat qilingan 
                
        else:
            return [avto for avto in selfavtolar:]"""
avto5 = Avto("Mozda", "6", "Qizil", 2015, 35000)
avto6 = Avto("volkswagen", "polo", "qora",2020,2000)
avto7 = Avto("Toyota", "Accord", "Oq", 2017, 42000)
salon1(avto5, avto6, avto7)
print(salon1())
 

#########################################################
#########################################################
# OPERATORLARNI QAYTA TALQIN QILISH (OVERLOADING)
# Pythonda obyektlar o'rtasida turli arifmetik amallarni bajarish mumkin va bu 
# amallar obyektning turiga qarab, Pytnon tomonidan turlicha talqin qilinadi. Masalan:
# Sonlar:
x, y = 10, 40
print(x+y)
print(y-x)

# matn
st = "Hello"
st1 = "world"
st_um = st + st1
print(st_um)
print(st*5)


# ro'yhat
son = [2,1,5,6,7]
son1 = [2,5,64,9,7]
print(son+son1)
print(son*8)


# Keling, bu amallarni bizning obyektimizga ham qo'llab ko'ramiz. Boshlanishiga
# 2 ta avtosalon yarataylik, va har biriga alohida avtolar qo'shaylik. Ishimizni
# osonlashtirish uchun add_avto() metodimizni ham istalgancha parametr qabul qilishga 
# moslab o'zgartiramiz:
# __add__        qo'shish
# __sub__        ayrish
# __mul__        ko'paytirish
# __pow__        daraja  
# __div__        bo'lish

salon1 = Avtosalon("Musofir")
salon2 = Avtosalon("Iymon")

avto1 = Avto("Gm","malibu", "qora", 2022, 25000)
avto2= Avto("Daewo","nexia","oq", 2010, 3500)
avto3 = Avto("gm", "matiz", "qora",2016,5400)
avto4 = Avto("Gm","cobalt", "Moykriy", 2022, 13500)
avto5 = Avto("Mozda", "6", "Qizil", 2015, 35000)
avto6 = Avto("volkswagen", "polo", "qora",2020,2000)
avto7 = Avto("Toyota", "Accord", "Oq", 2017, 42000)
salon1.add_avto(avto1,avto2,avto3,avto4)
salon2.add_avto(avto5,avto6,avto7)
""" def __add__(self,yangi_salon):
        if isinstance(yangi_salon, Avtosalon):            
            new_salon = Avtosalon(f"{self.name} {yangi_salon}")
            new_salon.avtolar = self.avtolar + yangisalon.avtolar
            return new_salon
       """
salon = salon1 +salon2
print(salon)
print(salon()) 

# Istasak, qo'shish operatori yordamida salonga yangi Avto qo'shish imkoniyatini
 # ham yaratishimiz mumkin:
""" yuqoridagi kodga elif qo'shamiz

    elif isinstance(yangi_salon, Avto):
        self.add_avto(yangi_salon)
    else: 
        print(f"Avtosalonga {type(yangi_salon)} qo'shib bo'lmaydi")"""
    
avto9 = Avto("BMW", "X7", "qora", 2024, 97500)
salon1+avto9
print(salon1[:] )

###############################################################################
#   AMALIYOT 
###############################################################################

"""" Avvalgi darslarda yaratilgan obyektlarga (Shaxs, Talaba, ) turli dunder metodlari
qo'shishni mashq qiling"""
class Shaxs:
    def __init__(self,ism, familiya, pasport, tyil, parol):
        """Shaxsning hususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil
        self.__parol = parol
        
    def __repr__(self):  # obyektga murojat qilganimizda bizga pasdagidaga chiqadi 
        return f"Ism: {self.ism}, familiya: {self.familiya} "
    
inson1 = Shaxs("Ali", "Valiyev", 'AA9359240', 1998, "BB7313898")

print(inson1)

####################################
class Talaba(Shaxs):   # talba voris class ,,, shaxs esa super class 
   """Talaba clasi """
   def __init__(self,ism,familiya,pasport, tyil, parol, Id,):
       """Talabaning hususiyatlari"""
       super().__init__(ism,familiya,pasport,tyil,parol)  #5-qatorda (def __init__ ichida) klassimiz super klassning xususiyatlarini meros olishini ko'rsatdik 
       self.id = Id
       self.bosqich = 1
       
   def add_bosqich(self):
       self.bosqich +=1
   def __str__(self):
       return f"{self.ism} {self.familiya} {self.tyil} da tug'ilgan"
   def __lt__(self, y ):
       return self.bosqich< y.bosqich
   def __le__(self,y):
       return self.bosqich <=y.bosqich
   def __gt__(self,y ):
       return self.bosqich > y.bosqich
   def __ge__(self,y):
       return self.bosqich >= y.bosqich
   def __eq__(self, y):
       return self.bosqich == y.bosqich
   def __ne__(self,y):
       return self.bosqich != y.bosqich
   
   
talaba1 = Talaba("Ubaydullo", "Obidjanov", "ssdf65", 1998, "adfs463545",16784651)
talaba2 = Talaba("vali", "Aliyev", "ssdf65", 1998, "adfs463545",16784651)
talaba3 = Talaba("G'ani", "Obidjanov", "ssdf65", 1998, "adfs463545",16784651)
talaba4 = Talaba("Omon", "Ubaydullayev", "ssdf65", 1998, "adfs463545",16784651)
talaba1.add_bosqich()
talaba1.add_bosqich()
talaba2.add_bosqich()
talaba3.add_bosqich()
talaba3.add_bosqich()
talaba3.add_bosqich()
talabalar = [talaba1, talaba2, talaba3, talaba4]
for talaba in talabalar:
    print(talaba.bosqich)
print(talaba1>talaba2)
print(talaba1>talaba3)
print(talaba1>talaba4)
print(talaba2>= talaba2)
print(talaba2>= talaba3)
print(talaba2>= talaba4)


class Fan:
    def __init__(self,nomi ):
        self.nomi = nomi
    
    def __str__(self):
        return f"{self.nomi} fani"
fan = Fan("Fizika")
print(fan)
class Professor(Shaxs):
    def __init__(self, ism, familiya, pasport, tyil, yutuq,talabalar_soni,ish_joyi,manzil,parol):
        "professorning hususiyatlari"
        super().__init__(ism, familiya, pasport, tyil,parol)
        self.yutuq = yutuq 
        self.talabalar_soni= talabalar_soni
    
    def __str__(self):
        return f"Professor: {self.familiya} {self.ism}"
teacher = Professor("Vosil", "Qobulov", "faae6e9", 1969, "Nnobel", 266, "Sergeli", "Chilonnzor",568754)
print(teacher)

class Talaba:
    """Kursga kiradigan talabalar """
    def __init__(self,ism , familiya):
        self.ism= ism
        self.familiya = familiya
        self.bosqich  = 1
    
    def add_bosqich(self):
        self.bosqich +=1
    def __repr__(self):
        return f"Talaba: {self.ism} {self.familiya}"
    
class Fan:
    def __init__(self,nomi ):
        self.nomi = nomi
        self.student = []
        
    def __str__(self):
        return f"{self.nomi} fani"
    
    def add_student(self,*talaba):
        for st in talaba:
            if isinstance(st,Talaba ):  
                self.student.append(st)
    def __getitem__(self, index):
        return self.student[index]
    
    def __setitem__(self,index,y):
        self.student[index] = y 
    
    def __len__(self):
        return len(self.student)
    
    def __add__(self,qiymat):
        if isinstance(qiymat,Talaba ):
            yangi_student =Talaba(f"{self.nomi} {qiymat.nomi}") 
            yangi_student.student = self.student + qiymat.student
            return yangi_student
        
        else:
            print(f"{self.nomi} faniga {type(qiymat)} qiymatni qo'shib bo'lmaydi.")
    def __call__(self):
        return [talaba for talaba in self.student]
    
student1 = Talaba("Sherzod", "G'aniyev")
student2 = Talaba("Ali", "Valiyev ")
student3 = Talaba("Vali", "Aliyev")
fan = Fan("Fizika")
fan.add_student(student1,student2,student3)
print(fan[:])
print(fan[1])
fan[0] = student3
print(fan[0])
print(len(fan))
fan.add_student(student1)
print(len(fan))
print(fan[:])
print()

