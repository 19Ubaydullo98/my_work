# # -*- coding: utf-8 -*-
# """
# Created on Sat Mar 30 15:03:49 2024

# @author: Ubaydullo
# """


# # JSON NIMA?
# # JSON (JavaScript Object Notation) bugungi kunda ma'lumotlarni saqlash va internet 
# # orqali uzatish uchun qo'llaniladigan eng mashxur format hisoblanadi. Dastavval 
# # JavaScript tili uchun yaratilgan bu format, bugungi kunda deyarli barcha dasturlash 
# # tillari tomonidan ishlatiladi. Qolaversa, JSON formatidagi fayllarining tarkibini 
# # oddiy matn muharriri yordamida koʻrish va tahrirlash mumkin.

# # Aksar holatlarda dastur va server orasidagi maʻlumotlar aynan JSON koʻrinishida 
# # uzatiladi. 

# # Demak, dasturimiz davomida maʻlumotlarni JSON ko'rinishida saqlashimiz, internet 
# # orqali boshqa foydalanuvchilarga, dasturlarga yoki serverga yuborishimiz, JSON 
# # fayllarni Pythonda ochib, unga ishlov berishimiz va turli amallar bajarishimiz mumkin.

# "JSON o'zgaruvchilar, tarkibidan qat'iy nazar matn ko'rinishida saqlanadi."

# # PYTHON Jsonga 
# import json ## Json modulini yuklab olamiz

# # json.dumps(x) - berilgan x o'zgaruvchini JSON matniga o'zgartiradi
# # json.dumps(x,fayl) - berilgan x o'zgaruvchini matniga o'zgartirib, ko'rsatilgan
# # faylga saqlaydi


# # json.dumps()
# # Ma'lumotlarni JSON formatiga o'tkazish uchun json.dumps() funksiyasidan foydalanamiz.

# a = 10 
# a_json = json.dumps(a)
# print(type(a_json))  # natija : <class 'str'>

# sentence = "Iymon bo'lsa imkon topiladi"
# b_json= json.dumps(sentence)
# print(type(sentence))  # natija : <class 'str'>

# royhat = [15,65,54,64]
# royhat_json = json.dumps(royhat)
# print(type(royhat_json))  # natija : <class 'str'>

# #Json ma'lumotlarni matn ko'rinishida saqlaydi

# bemor = {
#     "ism": "Obidjanov Ubaydullo",
#     "yosh" : 26,
#     "oila": True,
#     "farzandlari" : ("Muhammad", "Ali"),
#     "Allergiya": None,
#     "dorilar" : [
#         {"nomi": "analgin", "miqdori":0.5},
#         {"nomi": "Trimol",  "miqdori": 1.2}
#         ]
#     }
# bemor_json = json.dumps(bemor)
# print()   #      funksiya yordamida Json tarkibini ko'rishimiz mumkin:
# print(bemor_json) 
# # Yuqoridagi natija o'qish uchun noqulay ko'rinishda chiqdi. Buni to'g'rilash uchun
# # dumps() funksiyasiga qo'shimcha indent=4 parametrini beramiz. Bu parametr ma'umotlarni
# # saqlashda chapdan qancha joy tashlashni ko'rsatadi:
# bemor_json = json.dumps(bemor, indent=  4) # indent satr boshidan joy tashlaydi
# print(bemor_json)               # ^^ aslida bu kerak emas, buni konsolega chiroyli chiqishi uchun foydalandik
# print(type(bemor_json))


# #######################################
# #   JSON.DUMP()   
# # Ma'lumotlarni JSON formatiga o'tkazish va faylga yozish uchun json.dump() metodidan foydalanamiz
# #
# bemor = {
#     "ism": "Obidjanov Ubaydullo",
#     "yosh" : 26,
#     "oila": True,
#     "farzandlari" : ("Muhammad", "Ali"),
#     "Allergiya": None,
#     "dorilar" : [
#         {"nomi": "analgin", "miqdori":0.5},
#         {"nomi": "Trimol",  "miqdori": 1.2}
#         ]
#     }
# with open("bemor.json", "w") as file:
#     json.dump(bemor,file)   
    
# # endi JSON fayl tarkibini istalgan matn muharriri bilan ochib ko'rishimiz mumkin:
    
#     #######################################
#    # JSONDAN PYTHONGA 
# # JSON formatidagi ma'lumotlarni python ma'lumot turiga keltirish uchun json.loads()
# # yoki json.load() funsiyalaridan foydalanamiz 
# # Yuqoridagi kabi json.loads() funksiyasi to'g'ridan to'gri Json matn bilan ishlasa. 
# # json.load() funksiyasi JSON fayllarini o'qish uchun ishlatiladi.


#         ##############################################
# # json.loads()
# # bu funksiya parametr sifatida fayl qabul qiladi va pythonga ma'lumot turiga o'tkazadi.
# print(type(bemor_json))
# patient = json.loads(bemor_json) # pythonga o'tkazish 
# print(type(patient))


# #######################\
#     # json.load()
# # bu funksiya JSON fayllarini pythonga yuklab olish uchun ishlatiladi 
# filename = "bemor.json"
# with open(filename) as file:
#     bemor = json.load(file)
# # yuqoridagi holatda json fileni yuklab oldik 
# print(bemor)
# print(type(bemor)) 



################################################################
"""JSON BILAN ISHLASH
Ko'pincha internet orqali JSON fayllarni qabul qilganimizda ma'lumotlar bir necha
qavatli lug'at ko'rinishida bo'ladi. JSON matnidan aynan o'zimizga kerakli ma'lumotni 
ajratib olish uchun lug'atni biroz tahlil qilish, uning kalitlari va qiymatlarini
topish talab qilinishi mumkin. Bu ayniqsa juda uzun JSON fayllarga tegishli. 
Shuning uchun JSON bilan samarali ishlash uchun lug'atlar bilan ishlashni yana 
bir bor takrorlab oling.

Quyidagi misolda Google Maps hizmati qaytargan JSON matni lug'at ko'rinishida 
berilgan. Bu Toshkent shahridagi Olmazor tumanining Geografik manzili. 
"""
data = {
    "address_components": [
        {
            "long_name": "Almazar District",
            "short_name": "Almazar District",
            "types": [
                "political",
                "sublocality",
                "sublocality_level_1"
            ]
        },
        {
            "long_name": "Tashkent",
            "short_name": "Tashkent",
            "types": [
                "locality",
                "political"
            ]
        },
        {
            "long_name": "Tashkent Region",
            "short_name": "Tashkent Region",
            "types": [
                "administrative_area_level_1",
                "political"
            ]
        },
        {
            "long_name": "Uzbekistan",
            "short_name": "UZ",
            "types": [
                "country",
                "political"
            ]
        }
    ],
    "formatted_address": "Almazar District, Tashkent, Uzbekistan",
    "geometry": {
        "bounds": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        },
        "location": {
            "lat": 41.3645355,
            "lng": 69.2281531
        },
        "location_type": "APPROXIMATE",
        "viewport": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        }
    },
    "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
    "types": [
        "political",
        "sublocality",
        "sublocality_level_1"
    ]
}
# Keling shu ma'lumotlar orasidan tumanning geografik koordinatalrini topamiz.Avvalo, 
# lug'atga ko'z yugurtirib chiqib, bizga kerak ma'lumotlar quyidagi ko'rinishda berilganini ko'rishimiz mumkin:
    
# "location": {
#             "lat": 41.3645355,
#             "lng": 69.2281531

          
# Bizga aynan latitude (kenglik) va longitude (uzunlik) qiymatlari kerak. Ular esa 
# "location" kaliti ichidagi lug'atda lat va lng kalitlariga tegishli qiymatlarda 
# joylashgan. location kalitining o'zi ham geometry kaliti ichida joylashganini 
# ko'rishimiz mumkin.

# Demak, lu'gat ichidan lat va lng qiymatlarini olish uchun quyidagi kodni yozamiz:
print(data["geometry"])
print(data["geometry"]["location"])
kenglik = data["geometry"]["location"]["lng"]
uzunlik = data["geometry"]["location"]["lat"]
print(kenglik, uzunlik)  # bu manzil bo'ladi shu ko'rinishda 



import json      #      Amaliyot
# shbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: 
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
print(type(data))
import json
data_json = json.dumps(data)
print(data_json)
print(type(data_json))

#######################
# ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring: 
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
print(type(talaba_json))
talaba = json.loads(talaba_json)
print(type(talaba))
for key, value in talaba.items():
    print(value, end= " ")
##############################
# Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
with open("data.json","w") as file:
    json.dump(data, file)

with open("talaba.json", "w") as file:
    json.dump(talaba, file)

# ####################################
# Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi 
# saqlangan. Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet
# talabasi" ko'rinishida konsolga chiqaring.
filename = "students.json"
with open(filename) as file:
    talabalar= json.load(file)
# print(talabalar)
for talaba in talabalar["student"]:
    print(f"{talaba['name']} {talaba['lastname']}, {talaba['year']} - kurs,"
          f" {talaba['faculty']} fakulteti talabasi.")
########################################
filename = "api-result.json"
with open(filename) as file:
    python = json.load(file)
# print(python)
python_json = json.dumps(python, indent= 4)
# print(python_json)
print("                        ",python["query"]["pages"]["13801"]["title"])
print(python["query"]["pages"]["13801"]["extract"])