def summa(*sonlar): #args (*arguments) usuli bunda arguments istalgancha qiymat
# qabul qilib oladi va ularni o'zgarmas ro'yhat Tuple qilib oladi.
    yigindi = 0 
    for i in sonlar:
        yigindi += i 
    return yigindi

print(summa(15,6,169,96,16,6,16))
def summa(*sonlar):
    return sum(sonlar)# soddaroq usuli

###############################
# agar funksiya bir nechta argument qabul qilsa *args doim ohirida yoziladi

def summa(x,y,*sonlar):
    return x+y+sum(sonlar)# agar argumentni 2 tadan kam bersak xatolik chiqadi
print(summa(1,15,6,169,96,16,6,16))

######################################################
#   *kwargs UsULI   
# agar funksiya kalit_qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa 
#va bunday parametrlar soni noma'lum bo'lsa, argument oldidan ikkita yulduzdcha 
#qo'yiladi(**kwargs)
def  avto_info(kompaniya, model, **malumotlar):
    """this is function about data return about car's information """
    malumotlar["kompaniya"] = kompaniya
    malumotlar["model"] = model
    return malumotlar
car_1 =avto_info("GM"," Onix", rang = "oq", yil = 2023,)
car_2 =avto_info("GM"," Matiz", rang = "oq", yil = 2016,narxi = "5400$")
print(car_2)
## funksiya ichida birinchi foydalanuvchi kiritgan qo'shimcha qiymatlardan iborat 
# ma'lumotlar dev nomlangan lug'at shakllantiriladi. Undan keyin esa mahburiy parametrlarni
# lug'atga qo'shamiz.
###########################################################
# # Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing. 
# def kopaytma(*sonlar):
#     """ Istalgancha qabul qilib ko'paytmasini chiqaruvchi funksiya"""
#     son = 1 
#     for n in sonlar:
#         son *=n 
#     return son
# print(kopaytma(1,2,3,5,6))
# ##################
# # talabara haqida ma'lumotlar lug'at ko'rinishida chiqaruvchi funksiya
# def data(name, surname, **add):
#     add["name"] = name
#     add["surname"] = surname
#     return add

# student_1 = data("Islomjon", "Isroiljanov", age = 14, sinf = 7 )
# student_2= data("Diyorbek", "Alimov", age = 14, sinf = 7,adress= "Uychi")
# print(student_1)
# print(student_2)











