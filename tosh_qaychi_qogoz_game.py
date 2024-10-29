import random
a= ['✋','✌️','🤛']
print("Assalomu Aleykum Hurmatli foydalanuvchi, bizning dasturimizga hush kelibsiz!!!")
kom = random.choice(a)
b = """Hurmatli foydalanuvchi o'yinni boshladik. 
Quyidagilardan birini tanlang: Masalan - 1
1: '✋' _qog'oz
2: '✌️'_qaychi
3: '🤛'_quduq """
print(b)


for n in range(1,4):
    user= int(input(">>>"))
    if user==1 and kom == a[0]:
        print(f"natija: durang {a[0]}:{a[0]}")
    elif user==2 and kom == a[1]:
            print(f"natija: durang {a[1]}:{a[1]}")     #### umumiy durrang vaziyat 
    elif user==3 and kom == a[2]:
        print(f"natija: durang {a[2]}:{a[2]}")
################
    elif user==1 and kom == a[1]:
        print(f"natija: men yutdim:  {a[0]}:{a[1]}")
    elif user==1 and kom == a[2]:
        print(f"natija: siz yutqizdiz {a[0]}:{a[2]}")
    
    elif user == 2 and kom == a[0]:
        print(f"natija: siz yutdiz {a[1]}:{a[0]}")
    elif user == 2 and kom == a[2]:
        print(f"natija: men yutdim {a[1]}:{a[2]}")
    
    elif user==3 and kom == a[0]:
        print(f"natija: men yutdim {a[2]}:{a[0]}")
    elif user==3 and kom == a[1]:
        print(f"natija: siz yutdiz {a[2]}:{a[1]}") 
    print("Yana bir bor tanlang: ")
    
