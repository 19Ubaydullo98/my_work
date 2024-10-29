# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:24:01 2024

@author: Ubaydullo
"""
# Boshlanishiga oddiy bir funksiya yozamiz bu funksiya ism familiya qabul qiladida 
# bizga ism familiyani jamlab qabul qiladi 

# def get_full_name(ism, familya, otasi):
#     return f"{ism} {otasi} {familya}".title()  # bu yerda title .title() metodini esdan chiqardik 
#  #natija :  ubaydullo obidjanov >>> b           u xato biz endi tekshirib ko'rishimiz mumkin 
# print(get_full_name("vali", "aliyev", "qayumov"))
# # ism_familiya = get_fullname("ubaydullo", "obidjanov")

def get_full_name(ism, familya, otasi = ""):
    if otasi:
        return f"{ism} {otasi} {familya}".title()
    else:
        return f"{ism} {familya}".title()
print(get_full_name("alijon","olimov", "valiyev"))


