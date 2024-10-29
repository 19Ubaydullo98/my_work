 # -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:30:55 2023

@author: Ubaydullo-PC
"""

"""                   YANA input()
Dasturlar foydalanuvchining muammolarini hal qilish uchun yoziladi. Buning uchun 
esa, foydalanuvchi bilan aloqa o'rnatish, undan turli ma'lumotlarni qabul qilib 
olib talab etiladi. Misol uchun, dasturimiz foydalanuvchiga ismi bilan murojat 
qilishi uchun, avval uning ismini so'rashi kerak. Yoki, foydalanuvchi istagan 
ma'lumotni topish uchun avval undan biror kalit so'z kiritishni so'rash kerak va hokazo.

Biz avvalgi darsimizda input() yordamida foydalanuvchidan qiymat qilishni o'rgangan
 edik. Dastur davomida input() funktsiyasini chaqirganimizda dastur foydalanuvchi
 biror matn kiritiib, Enter tugmasini bosgunga qadar to'xtab turadi. 
 
Foydalanuvchi kiritgan qiymatni biror o'zgaruvchiga yuklash, va undan dastur 
davomida foydalanish mumkin.                                     """
"""
#ism = input("Iltimos ismingizni kiriting: ")
#print(f" Salom, {ism.title()} ")
########################################
'''input() finktsiyasi ichidagi matn ingliz tilida prompt, savol deyiladi. Aslida 
biz savolni ham o'zgaruvchiga yuklab, shaxsiy so'rovnomalar ham yaratishimiz mumkin.     '''

#ism = input("Iltimos ismingizni kiriting: ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida: "
#yosh = input(savol)


#Yuqorida birinchi input() bilan foydalanuvchi ismini so'radik va yangi savol matnini yasab oldik. 

##################
ism = input("Iltimos ismingizni kiriting: ")
savol = f"Salom {ism.title()},yoshing nechida:"
yosh = input(savol)
yosh = int(yosh) # yoshnni butun songa o'takz'
height =input("Bo'yinngiz nechchi:")
height = float(height) # bo'ynni o'nik songda o'tkazayamiz5

print(height)

##############################################################################
'''                  while TSIKLI BILAN TANISHAMIZ
Biz avvalroq for tsikli bilan tanishgan edik. for tsikli ma'lum bir ro'yxatni 
olib, ro'yxat ichidagi qiymatlar tugaginga qadar biror kodni takrorlar edi. while 
ham takrorlash operatori bo'lib, for dan farqli ravishda, toki ma'lum bir shart 
to'g'ri (True) bo'lsa, kodni takrorlayveradi.  '''

#   while so'zi ingiz tilidan "toki" yoki "-gacha" deb tarjima qilinadi.#
# keling while da 5 gacha sanaymiz

son = 1  # son o'zgaruvchisiga 1 ni beramiz
while son<=5: # son qachonki 5 dan kichik yoki teng ekan 5 gaaa yetguncha amal bajarilaveeradi
    print(son, end=" ")
    son = son +1  #  son =+1
print("dastur tugadi")
###########################################################################
#Shu paytgacha yozgan dasturlarimiz faqatgina bir martta bajarilayotgan edi.
#while tsikli yordamida dasturni to'xtatish imkoniyatini foydalanuvchiga berishimiz mumkin.
# keling endi istalgan sonni kvadratini chiqaruvch dastur tuzaylik
print('Kritilgan sonning kubini chiqarib beruvchi dastur.')
ism = input("Iltimos ismingizni kriting: ")
prompt = f"{ism.title()} istalgan sonni kiriting"+" (dastrudan chiqish uchun 'stop' so'zini yozing) : "
value = ''
while value != 'stop':
    value = input(prompt)
    if not value == 'stop':
        print(int(value)**3)
print('Dastur tugadi')
############################################################################
'''                          Ishora (flag)
Yuqoridagi dasturda dasturni to'xtatish uchun yagona shartni tekshirdik 
(qiymat!='exit'), katta dasturlarda bir emas bir nechta shartlarni tekshirish, 
va ulardan biri bajarilgan taqdirda dasturni to'xtatish talab qilinishi mumkin.

masalan: oyinlarda o'yin tugashi uchun qaysidir shart bajarilsa o'yin tugaydi 
bunday shartlarga o'yinchiini otib qo'yishi yoki chuqurga tushib ketishi , 
o'yinda g'olib bo'lishi bilan o'yin tugaydi.
 
Bunday holatlarda biror o'zgaruvchidan ishora (flag) sifatida foydalanishimiz 
mumkin. Agar dastur bajarilishi davomida dasturni to'xtatish shartlaridan biri
bajarilganda ishora o'zgaruvchining qiymatini o'zgartiramiz va dastur o'z-o'zidan to'xtaydi.  '''

print('Kritilgan sonning kubini chiqarib beruvchi dastur.')
savol = "Istalgan sonni kiriting"
savol += "(dastur to'xtashi uchun 'stop' deb yozing): "
ishora = True # biz  o'zgaruvchini  o'rniga bitta ishonch berildi.
while ishora: # tsikmiz True bo'lsa doim takrorlanaveradi 
    qiymat = input(savol)
    if qiymat == 'stop':
        ishora = False
    else:
        print(float(qiymat)**3)
print("Dastur tugadi.")

###############################################################################
'''               BREAK OPERATORI
Break operatori yordamida ma'lum bir shartni tekshirish va while tsikli 
bajarilishini to'xtatib qo'yish mumkin.          '''
print('Kritilgan sonning kubini chiqarib beruvchi dastur.')
savol = "Istalgan sonni kiriting"
savol += "(dastur to'xtashi uchun 'exit' deb yozing): "

while True: # bu abadiy sikl doim takrorlanib turaveradist
    value = input(savol)
    if value == 'exit':
        break
    else:
        print(float(value)**3)
print('Dastur tugadi!')
#####################
# breakni for tsiklda ham ifodalasak bo'ladi
number = list(range(1,11))
for n in number:
        if n == 5:# n miz 5 ga teng bo'lib qolsa dastur tugaydi
            break
        else:
            print(f"{n} soninig kvadrati {n**2} ga teng")
            
#  while tsikli ichida bir nechta break operatori ham bo'lishi mumkin.
""
############################ ###################################################
'''                  CONTINUE OPuERATORI
Continue operatori esa aksincha, ma'lum bir shart bajarilganda qadam tashlab 
o'tish uchun mo'ljallangan. break ning teskarisi bo'ldi mendan pastdagilarni bajarmasdan 
yana yuqordan qaydt:                               '''
number = list(range(1,11))
for n in number:
        if n == 5:# n miz 5 ga teng bo'lib qolsa dastur yana yuqoridan pastga tushadi
            continue
        else:
            print(f"{n} soninig kvadrati {n**2} ga teng")
# natijani ko'rsak orasida 5chisi yo'q 
#33333333333333333333333333
son = 0
while son<10:
    son += 1
    if son%2 == 0: # hozir konsolga juft sonlar chiqadi agar != (==) bo'lsa toq sonlar chiqadi
        continue
    else:
        print(son)
        
#  while tsikli ichida bir nechta continue operatori ham bo'lishi mumkin.
########################################################################################"""
'''          ABADIY TSIKL TUZOG'I
Tsikllar bilan ishlashda abadiy tsikl yaratib qo'yishdan ehtiyot bo'lishimiz 
kerak. Abadiy tsiklga turli mantiqiy xatolar sabab bo'lishi mumkin: noto'g'ri 
shart, o'zgarmas qiymat, kodlar ketma-ketligida xatolik va hokazo. 

Kelin ba'zi misollarni ko'ramiz:                '''
    
son = 0
while son<10:
    if son%2 != 0: # hozir konsolga juft sonlar chiqadi agar != (==) bo'lsa toq sonlar chiqadi
        continue
    else:
        print(son)
#Yuqoridagi kod abadiy davom etadi, sababi biz son ning qiymatini o'zgartirishni 
#esdan chiqardik. yani  son =+1 degan qiymatni qo'shmadik
###        Bu kod ham abadiy davom etadi, lekin nima uchun?
son = 0
while son<10:
    if son%2 != 0: 
        continue
    else:
        print(son)
    son+= 1



