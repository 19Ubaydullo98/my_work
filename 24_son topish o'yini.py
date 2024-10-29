import random
# a= ['✋','✌️','🤛']
# print("Assalomu Aleykum Hurmatli foydalanuvchi, bizning dasturimizga hush kelibsiz!!!")
# kom = random.choice(a)
# b = """Hurmatli foydalanuvchi o'yinni boshladik. 
# Quyidagilardan birini tanlang: Masalan - 1
# 1: '✋' _qog'oz
# 2: '✌️'_qaychi
# 3: '🤛'_quduq """
# print(b)
# n_kom=0
# c=0

# for n in range(1,4):
#     user= int(input(">>>"))
#     if user==1 and kom == a[0]:
#         print(f"natija: durang {a[0]}:{a[0]}")
#         n_kom +=1    
#         c +=1
#     elif user==2 and kom == a[1]:
#         print(f"natija: durang {a[1]}:{a[1]}")
#         c +=1
#         n_kom +=1 #### umumiy durrang vaziyat 
#     elif user==3 and kom == a[2]:
#         c +=1
#         print(f"natija: durang {a[2]}:{a[2]}")
#         n_kom +=1 
# ################
#     elif user==1 and kom == a[1]:
#         print(f"natija: men yutdim:  {a[0]}:{a[1]}")
#         n_kom +=1   
#     elif user==1 and kom == a[2]:
#         print(f"natija: siz yutdim {a[0]}:{a[2]}")
#         c +=1
    
#     elif user == 2 and kom == a[0]:
#         print(f"natija: siz yutdiz {a[1]}:{a[0]}")
#         c +=1
#     elif user == 2 and kom == a[2]:
#         print(f"natija: men yutdim {a[1]}:{a[2]}")
#         n_kom +=1   
    
#     elif user==3 and kom == a[0]:
#         print(f"natija: men yutdim {a[2]}:{a[0]}")
#         n_kom +=1   
#     elif user==3 and kom == a[1]:
#         print(f"natija: siz yutdiz {a[2]}:{a[1]}")
#         c +=1
# print(f"Umumiy natija men-{n_kom} : siz -{c}")
###############################################################
import random as r

def option_user(x):
    print(f"Keling o'ylagan sonni topish o'ynaymiz ! \n1 dan {x} gacha son o'yladim.  Topa olasizmi ?:")
    a = r.randint(1,x)
    n = 0
    while True :
        n +=1
        son_top = int(input(f">>"))
        if son_top == a: 
            print(f"TOPDINGIZ! men {a} sonini o'ylagan edim. \n {n} ta tahmin bilan topdingiz. tabriklayman!! \n")
            break
        elif son_top<a:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
            # n +=1 buni har birida berish shart emas 
        elif son_top>a:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
                # n +=1   buni har bir taxminga qo'yish shart emas 
    return n
###########################################
def option_kom(x):
    sanoq = 0 
    print(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman. ")
    input("Istalgan tugmani bosing: ")
    a = 1
    b = x
    while True :
        sanoq +=1
        n = r.randint(a,b)
        print(f"Siz {n} sonini o'yladingiz: (t) to'g'ri, bundan kattaroq (+), bundan kichikroq (-) ?? ")
        javob = (input(">>>")).lower()
        if javob.lower() == "t":
            print(f"siz o'ylagan sonni {sanoq} ta taxmin bilan topdim !")
            break
        elif javob == '+' :
                a = n+1
                # sanoq +=1 buni hamma shartga berish shart emas 
        elif javob == '-':
                b = n-1
                # sanoq +=1 buni hamma shartga berish shart emas 
                
    return sanoq                  

def game(x):
    yana = True
    while True:
        taxminlar_user = option_user(x)
        taxminlar_kom = option_kom(x)
        if taxminlar_user > taxminlar_kom:
            print("Men yutdim")
        elif taxminlar_user < taxminlar_kom:
            print("Siz yutdiz")
        elif taxminlar_user == taxminlar_kom:
            print("Durrang!!")
        yana = int(input(f"yana o'ynaysizmi? yes(1) / no(0): "))
        
        
    
             


