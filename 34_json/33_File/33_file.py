# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 07:40:38 2024

@author: Ubaydullo
"""
# BU holatda fileni ochsa bo'ladi lekin tavsiya qilinmaydi 
# file = open("pi.txt")
# pi = file.read()  #fileni o'qib olyapmiz 

# file.close() # agar file ni shu holatdni bajarmasak berkitmasak filemizga zarar yetishi mumkin 
#############################

with open("pi.txt") as file: # bu funksiya faylni avtomatik tarzda yopadi 
    PI = file.read()
    print(PI)
    # bu yerdan qancha  kod yozsak bajarilaveradi 

print(PI)  #bu yerda biz withdan tashqariga chiqadi  va file berkiladi 
pi = PI.rstrip()
pi = PI.replace('\n','')
pi = float(pi)
print(pi)   ## textimizda vergul o'rniga nuqtadan foydalaniladi 
print(type(pi))  # matnimizni float ko'rinishiga o'tkizib oldik

########################### KEling endi papka ichidan file ochishni o'rganamiz 
filename = "python_lessons/Python_tutor/33_File/Talabalar.txt"#lini bitta variablega saqlab oldik 
with open("Talabalar.txt")as file :
    for line in file:  # bu orqali biz har bir qatorni consolega chiqaramiz 
        print(line)

# bu ikkinchi usuli
with open("Talabalar.txt") as file:
    talabalar = file.readlines() # bu yerda readlines faylni ichidagi har bir qatorni 
    #ro'yhat qilib beradi,  agar readline ya'ni s ni o'zini qo'shib yozmasak birinchi qatorni chiqarib beradi 
    
talabalar = [talaba.rstrip() for talaba in talabalar] #  bu kodimiz quyidagicha ishlaydi 
## 'Obidjanov Ubaydullo\n' shuni ohirisidagi shu belgini olib tashlaydi 
print(talabalar)

#####################################################
#####################################################
new_file = "new_file.txt" # pythonda faylga yozayapkanimizda faylni ichida ma'lumot bo'lsa uni o'chirib yozadi 
name = "Obidjanov Ubaydullo"   # aks holda yangi nomli fayl ochadi 
yil = 1998          #w bilan yangi filega yozamiz  
with open(new_file, "w") as file:# w write degani agar buni qo'ymasak faqat oqish uchun ochiladi file
    file.write(name + "\n")
    file.write(str(yil) + "\n") # python faqat fileni string ko'rinishida ochadi 
#########################################

yangi_fayl = "fileni_ustiga_yozish.txt"
with open(yangi_fayl, 'a') as fayl:
    fayl.write('Ubaydullo Obidjanov\n')
    fayl.write('1998\n')
    
#######################################################################
#####################################################################
# O'ZGARUVCHILARNI FAYLDA SAQLASH
# Yuqorida biz ma'lumotlarni matn ko'rinishida saqlashni ko'rdik. Agar dastur 
# davomida turli o'zgaruvchilarni faylda saqlash talab qilinsa pickle modulidan 
# foydalanamiz. Pickle ma'lumotlarni biz qanday ko'rinishda bersak, shunday ko'rinishda 
# faylga yozadi. Yuqoridagi usuldan farqli ravishda, pickle yordamida yozilgan
#  fayllarning tarkibini Pythondan tashqarida ko'rib bo'lmaydi. 
################################################################################

# PICKLE FAYLGA YOZISH
# Pickle dan foydalanish uchun biz avval bu modilni import qilamiz. Faylno ochishda 
# esa, open() funksiyasiga ikkinchi argument sifatida 'wb' (write binary) beramiz, 
# ya'ni ikkilik sanoq tizimida yozishni ko'rsatamiz. Faylga yozish uchun esa 
# pickle.dump() metodidan foydalanamiz:

import pickle
student1 = {"ism":"Vali","familya":"aliyev","sharif":"hasan"}
student2 = {"ism":"Ubaydullo", "familya":"Obidjonov", "sharif":"bek"}

with open("info", "wb") as file:
    pickle.dump(student1, file)
    pickle.dump(student2, file)
with open("info.txt", "wb") as file:
    pickle.dump(student1, file)
    pickle.dump(student2, file)

with open("info.dat", "wb") as file: # fayl kengaytmasi farqi yo'q faqat pythonda o'qiydi 
    pickle.dump(student1, file)
    pickle.dump(student2, file)    
#############################
# E'tibor bering, yuqorida fayl nomini yozishda uning turini ko'rsatmadik, sababi, 
# avval aytganimizdek bu fayllar Pythondan tashqarida ochilmaydi va biz buning 
# oldini olishimiz kerak. Aslida fayl nomiga .txt qo'shimchasini ham qo'shishimiz 
# mumkin, bu bilan dastur xato ishlamaydi, lekin bu bizni kelajakda chalg'itishi 
# mumkin. Istasangiz faylga .dat (data so'zidan olingan) qo'shimchasini qo'shib 
# qo'yishingiz mumkin (info.dat).

# Bu o'zgaruvchilarni alohida alohida qilib faylga saqlab qo'ygan foydadan holi bo'lmaydi'
################################################
# PICKLE FAYLDAN O'QISH
# Pickle fayldan o'qish uchun open() funksiyasini 'rb' (read binary) argumenti bilan 
# chaqiramiz. O'zgaruvchilarni bitta faylga yozganimizda, har bir o'zgaruvchi alohida 
# qatordan yoziladi. Fayldan o'qishda ham har bir qatorni alohida o'qishimiz kerak bo'ladi:                        
                            
with open("info.dat", "rb") as file:
    student1 = pickle.load(file)
    student2 = pickle.load(file)     

print(student1)
print(student2)


############################################################################################################
###############################################################################################################
# Amali mashg'ulot'

# Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching
matn_file = "Matn_file.txt"

with open(matn_file,"w+") as file:
    file.write(" BU holatda fileni ochsa bo'ladi lekin tavsiya qilinmaydi, ")
    file.write("""file = open("pi.txt")""")
    file.write("pi = file.read()  fileni o'qib olyapmiz \n ")
    file.write("file.close() # agar file ni shu holatdni bajarmasak berkitmasak filemizga zarar yetishi mumkin \n ")
    file.write("with open('Talabalar.txt')as file :\n")
    file.write("for line in file:\n")
    file.write(" print(line)")
with open(matn_file, "a") as file:
    file.write("with open(yangi_fayl, 'a') as fayl:")
    file.write(" fayl.write('Ubaydullo Obidjanov\n')")
    file.write("    fayl.write('1998\n')")
with open(matn_file) as file:
    read = file.readlines()

read = [qator.rstrip() for qator in read]
print(read)
#################################################################Sizning tug'ilgan kuningiz 
# π soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. Misol 
# uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi 
# yuqoridagi matnda uchraydimi yo'q toping.

def koy_top():
    """Pi sonini ichidan yil son kunni aniqlaydigon funksiya"""
    kun = input("tug'ilgan kuningizni kriting: ")
    oy = input("tug'ilgan oyingizni kriting: ")
    yil= input("tug'ilgan yilingizni kriting: ")
    t_sana = kun+oy+yil   
    with open("pi_million_digits.txt") as file:
        PI = file.read()
    if t_sana in PI:
        print("Siznign tug'ilgan sanangiz PI ning ichida bor.")
    else: 
        print("Siznign tug'ilgan sanangiz PI ning ichida yo'q")
        
with open("pi_million_digits.txt") as file:
    PI = file.readlines()

# PI = [line.rstrip() for line in PI]
PI = [float(line) for line in PI]

print(PI)
import pickle
with open("pickle.dat","wb") as file:
    pickle.dump(PI, file)
    
with open("pickle.dat","rb") as file:
    pickle = pickle.load(file)
    
# Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni 
# yangi qatordan faylga yozib boruvchi dastur tuzing. Dastur qayta chaqirilganida 
# yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas)

def ism_fam():
    """ISm familyani so'rab faylga saqlovchi funksiya"""
    ism = input("Ismingizni kiriting: ")
    familya = input("Familyangizni kiriting: ")
    with open("ism_fam.txt", 'a') as file:
        file.write(ism +" ")
        file.write(familya+"\n")
        
with open('ism_fam.txt', "r" ) as file:
    fi = file.read()
print(fi)    

    
