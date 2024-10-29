# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:44:01 2023

@author: Ubaydullo-PC
"""

'''                       XATOLAR
Har qanday dasturchi kod yozishda xato qiladi. Ko'p yozgan odam esa ko'p xato 
qiladi va bu tabiiy. Ba'zi xatolarimiz Python tomonidan dastur bajarilishdan
 avvaloq aniqlanadi. Ba'zilari esa dastur bajarish jarayonida aniqlanib, 
 dasturimiz to'xtab qoladi. Keling, bugun dasturlashni yangi boshlaganlar eng
 ko'p yo'l qo'yadigan xatolar bilan tanishamiz.  '''
##################################################################
'''                SyntaxError - SINTEKS XATOLIK
Biz syntax error bilan oldingi darsimizda tanishgan edik. Bu eng ko'p uchraydigan xato
bo'lib, odatda dasturlash tili qoidalariga amal qilmaslik natijasida kelib chiqadi.
Aksar dasturlash muhitlari sintaks xatolikni dastur bajarilishidan avvaloq aniqlab, 
dasturchiga ishora beradi. Sintaks xatolik bor dasturni Python bajarmaydi.'''

#print "Hello world"   # consolda quyidagicha hatolik chiqadi.
        
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# agar ingli tilida tarjima qilolmasangiz google translate orqali qilish kere 
###############################
'''               EOL va EOF xatolik
EOL (End of Line - qator yakuni) xatoligi sintaks xatolikning bir turi bo'lib,
odatda qator oxirida qo'shtirnoq (birtirnoq) ni yopish esdan chiqqanda yuzaga 
keladi.    '''

#print("Hello World!

####     Natija: SyntaxError: unexpected EOF while parsing
#EOF xatoligining muammoli tarafi, Python aynan qaysi funktsiya yopilmay qolganini
#ko'rsata olmaydi, ya'ni kodni sinchiklab ko'zdan kechirib chiqish talab qilinadi.
############################################
'''         IndentationError - JOY TASHLASHDA XATOLIK
Python tilida qator boshidan yoki joy tashlab yozish muhim ahamiyatga ega. Qator 
boshidan asossiz joy qoldirish IndentationError ga olib keladi. '''
#       print('hello world')                        
'''
Quyidagi kodga e'tibor bering, qator boshida 1 dona bo'sh joy qolgani uchunoq
 Spyder muhiti xatolikni aniqlab, qizil bilan belgilab qo'ydi.    '''
# print("hello world")
'''
Ba'zi joylarda esa aksincha, bo'sh joy tashlab yozish talab qilinadi. Masalan, 
for tsiklida yoki if-elif-else shartlarining ichida va hokazo'''
for son in range(0,10): #to'g'ri
    print(f"{son+1} ")  #to'g'ri
##
#for son in range(0,10): #to'g'ri
#print(f"{son+1} ")  #noto'g'ri
##
#for son in range(0,10):
# print(son)   # bu yerda ikkala print oldidan har hil son tashlangan 
    # print(sonn)
'''  QANCHA JOY TASHLAYMIZ?
Aslida, hech bo'lmaganda 1 harflik bo'sh joy qoldirish ham bizni IndentationError 
dan xalos qiladi. LEKIN, biz dastur davomida bir hil joy tashlashga odatlanishimiz kerak.
 
Qoida sifatida kamida 4 ta harflik joy yoki 1 ta TAB (klaviaturadagi tab tugmasi) 
joy tashlashni odat qilishimiz kerak. Va eng muhimi ikkalasini aralashtirmasligimiz
lozim. Ya'ni agar siz joy tashlash uchun Space (probel) ishlatsangiz, oxirigacha
shunday qiling, agar Tab ishlatsangiz oxirigacha tab ishlating. Ikkalasini aralashtirmang!'''

# SPACE   YOKI   TAB 
#########################################################
'''
RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK
Run time error — dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini
to'xtatadi. Sintaks xatolikdan farqli ravishda Python bunday xatolarni dasturni 
bajarishdan avval aniqlay olmaydi. Run time error ning bir necha turi bor. 
Keling, ulardan ba'zilari bilan tanishamiz.
'''# turlari  
'''
type error 
name error 
value error 
index error 
zero division error '''
###
#               TypeError
#Biror amalni (funktsiya, metod) noto'g'ri ma'lumot turi ustida bajarish. 
#num = input("Istalgan sonni kiriting: ") # bu yerda input faqat matn qabul qiladi
num = float(input("Istalgan sonni kririring: "))# bu esa son qabul qiladi 
print(f"{num} sonning kvadrati {num**2} ga teng")

#natij: TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
#Yuqoridagi kodda biz foydalanuvchi kiritgan qiymatni matndan songa o'tkazib 
#olishni unutdik, natijada sonning kavdratini hisoblashda Python xato berdi.

#### 
'''               NameError
O'zgaruvchi, funktsiya, obyekt nomini noto'g'ri yozish natijasida kelib 
chiquvchi xatolik.     bunda o'zgaruvchi, funksiya, biror obyekt, yoki boshqa 
bir operator nomini hato kiritganmiz      '''
num = list(range(0,10))    
#for son in number:
 #   print(son)
# natija: NameError: name 'number' is not defined
# biz bu yerda asosann num o'zgaruvchiga ikkinchi bor murojat qilayotganimizda 
# nno'to'g'ri murojat qildik 
# misol uchunn
#pint(num)  # print metodini noto'g'ri yozdik 
#####
'''   ValueError
Funktsiyaga noto'g'ri qiymatni yuborish natijasidagi xatolik'''
number = int(input("istalgan son kiriting: "))# intni o'rnig float yoki butun son kiritishni so'rash kerak 
if number >= 0:
    print("musbat son ")
else:
    print("manfiy son ")
'''
# natija: ValueError: invalid literal for int() with base 10: '45.3'
#bu yerdagi hatolik int faqat butun sonni oladi o'nlik sonni olmaydi 

Dastur xato bermasligi uchun yoki int() funktsiyasini float() ga almashtrishimiz
kerak, yoki foydalanuvchidan butun son kiritishni talab qilishimiz kerak.      '''

#####
'''                       IndexError
Yangi dasturchilar yo'l qo'yadigan yana bir xato bu indeks xatolik. Ya'ni 
ro'yxat elementlariga murojat qilishda indeksni noto'g'ri kiritish.            '''
fruit = ['olma', 'behi', 'anjiz']
#print(fruit[3])# fruit ro'yhatining 3-indexdagi elementini chiqar deddik lekin 
# natija: IndexError: list index out of range
# fruitda 3 ta element bor lekin index 0 dan boshlanadi va 2 gacha bo'ladi.
#####
'''n          ZeroDivisionError
Dastur jarayonida 0 ga bo'lish yuzaga kelgandagi xatolik      '''
x, y, z = 20,60,80
print(240/(x+y-z))      