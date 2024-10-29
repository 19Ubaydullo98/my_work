# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:36:50 2024

@author: ubayd
"""
# Funksiya va ro'yhat 

# def bahola(ismlar):
#     """Talabalarni baholash uchun funksiya """
#     Baholar = {}
#     while ismlar:
#         talaba = ismlar.pop()
#         baho = input(f"Talaba {talaba.title()}ning bahosini kiriting: ")
#         Baholar[talaba] = baho
#     return Baholar
# students= ['ali','vali','salim','hoshim']
# um_grade = bahola(students)
# print(um_grade)



###############################
#Amaliyot
def big_letters(katta):
    talabalar = []
    for i in katta:
        talabalar.append(i.title())
    return talabalar
students= ['ali','vali','salim','hoshim']
I = True
while I:
   
    friends = input(f"  Do'stizni yozing: ")
    
    javob = input("Yana do'stizni qo'shmoqchimisiz NO/YES: ")
    if javob.lower == "no":
        I=False
        
print(big_letters(students))
