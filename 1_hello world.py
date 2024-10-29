# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:23:40 2023

@author: Ubaydullo-PC
"""
#Consolni tozalash ctrl+l yoki clear
#Matn muharriri-dasturlar yozish uchun 
#console - kichik kodlar yozib ularni tekshirish uchun 
#qoshimcha malumotlar oynasi - bu yerda quyidagin narsalarni ko'rishimiz mumkin 
#1-turli funksiyalar haqida yordam 
#2-dasturlardagi o'zgaruvchilar ro'yhati 
#3-grafiklar 
#4-fayllar 
#consolda  biz oddiy arfimetrik amallarni bajarib ko'rishiimiz mumkin 
#-*/+ va boshqa amallarni bajarish  
#Biz bugun o'rganadigan funksiyamiz print
#Print('Assalomu aleykum')
#print(Hayrli tong ! )
#print(2+2*3)
#print(19/4) va boshqalar 

+ qo'shish '
- ayrish w
/bo'lish '
* kopaytirish 
** darajaga ko'tarish '
% qoldiqni aniqlab beradi 


###### syntaxError: invalid syntax

#   ##- Yuqoridagi misolda # belgisidan keyin yozilgan matn izoh (comment) deyiladi. \
#BU BELGI INGLIZ TILIDAGI (Hashtag belgisi) --> bu belgini qayerga qo'ygan
# bo'lsak shu belgidan qatorni ohirigachi kodimiz ishlamaydi, bu orqali 
#kodlarimizga izoh, sana mavzu nomi , avtorni yoki kodni yonidan izoh qoldirib 
#ketishimiz mumkin  

#print () funksiyasi matn yoki ifodalarni konsolga chiqarish vazifasini bajaradi.
#Lekin bu funktsiya to'g'ri ishlashi uchun bir nechta qoidalarga amal qilish lozim.
#Jumladan, agar konsolga matn chiqarmoqchi bo'lsak, matnimiz albatta qo'shtirnoq 
#yoki (" ") yoki birtirnoq(' ') orasida yozlishi kerak.
#keyingi kod
  
#print(Hayrli tong!)
#print('Hayrli tong )
#print('Hayrli tong'
#natija:  invalid syntaxError (sinteksda xatolik bor ) birinchi hatolik manzili
# chiqadi qaysi qator nima hatolik biz matnnni konsolda chiqarish uchun matnni 
 #"" qo'sh tirnoq uchun yoki bir tirnoqda yozish kerak

#'to\'g\'ri kod:'  
#print('Hayrli tong !')
#natija hayrli tong 

#print('Men "netbook" sotib oldim ') #bu to'g'ri 
#print("Men "netbook" sotib oldim ") #bu noto'g'ri  
#print("Men \"netbook\" sotib oldim ") # agar matnni qo'shtirnoq ichida yozmoqchi 
#bo'lsak \ --> back slash belgisini ishlatishimiz kerak qo'shtirnoq oldidan 


#Agar matnni bir necha qatorga bo'lib yozish talab qilinsa, uchtalik 
#qo'shtirnoq(""" """)yoki birtirnoqdan (''' ''')foydalanish mumkin:

#print('''Hayot o'zi nima demak?
#Yer yuzini sayr etmak.
#Hayot o'zi nima demak?
#Yashash uchun kurashmak.
#Kurashingiz, qardoshlar !''')

#print("Hayot o'zi nima demak? \n Yer yuzini sayr etmak.\n Hayot o'zi nima demak")
#Yuoqridagi matnni birtirnoq orqali ham konsolga chiqarish mumkinmi?
#Matndagi yo'q, g'am so'zlaridagi birtirnoqlar bunga to'sqinlik qilmaydimi? Qiladi.
#Buning oldini olish uchun esa matndagi birtirnoq belgisidan avval \ belgisini qo'yish lozim.

#print('Odami ersang, demagil odami, \nOniki, yo\'q xalq g\'amidin g\'ami')

#SINTEKS XATOLIK (SYNTAX ERROR)
#Har bir tilda orfografik va grammatik qoidalar bo'lgani kabi, dasturlash tillarining 
#ham o'ziga yarasha qonun-qoidalari bor. Bu qoidalar to'plami sinteks (syntax)
#deb ataladi. Sinteks xatolik (Syntax Error) deb esa shu qoidalarning buzilishiga aytiladi. 
#Misol uchun keraksiz joyda qo'yilgan nuqta, vergul yoki bo'sh joy, shuningdek 
#ma'lum funktsiyalar nomini xato yozish (print() o'rniga prit()), ochilmay yoki 
#yopilmay qolgan qavs, noo'rin bo'shliq, qolib ketgan kalit so'z (keyword) kabilar 
#ham Syntax Error hisoblanadi.
#Syntax Error eng ko'p uchraydigan xatolik bo'lib, Python bunday xatolik bor dasturlarni bajarmaydi. 
#Biz darslarimiz davomida turli sinteks qoidalar haqida o'z o'rnida yana to'xtalamiz.




#ARIFMETIK AMALLAR
#Amaliyotga qaytamiz, print() funktsiyasi nafaqat matn, balki turli
# ifodalarni ham konsolga chiqaradi.

#print(8+9)
#print(15/5+6)
#print(27/5) 
#print(20/5) #Ko'rib turganingizdek, / belgisi bo'lish amalini bajaradi va natija 
#har doim o'nlik son ko'rinishida bo'ladi (agarchi bo'lish amali natijasida butun son xosil bo'lsa ham):\
#print(30//60)#Bo'lish amalidan butun son ko'rinishidagi natija olish uchun // belgisidan foydalanamiz
 

#print('to\'qqizning kvadrati:', 9*9 )
#print("3x3=", 3*3)

#        AMALIYOT
#Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval misol matnini izoh ko'rinishida yozing:
#5 ning 4-darajasini toping
#22 ni 4 ga bo'lganda qancha qoldiq qoladi?
#Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
#Diametri 12 ga teng bo'lgan doiraning yuzini toping  ( deb oling)
#Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)

# Javoblar
print(5**4)#bu kod beshning 4chi darajasini chiqaradi
print('Yigirma ikkini 5 ga bo\'lgandagi qoldiq:', 22%5) # qoldiq chiqaradi 
print('Tomonlari 125 ga teng kvadratning yuzi:', 125*125 )
print('Tomonlari 125 ga teng kvadratning peremtri :', 125*4 )
print("Diametri 12 ga teng bo'lgan doiraning yuzi:", 6*6*3.14)
print('Katetlari 6 va 7 ga teng bo\'lgan to\'g\'ri burchakli uchburchakning gipatenuzasi: ',(6**2+7**2)**0.5)









print