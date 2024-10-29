# # """
# # QIYMAT QAYTARUVCHI FUNKSIYA 
# # @author: ubaydullo
# # """
# # """
# # Avvalgi darsimizda yaratgan barcha funksiyalarimiz konsolga ma'lumot 
# # chiqarayotgan edi. Aslida, aksar holatlarda bu g'ayritabiiy. Sababi, dasturchi 
# # sifatida biz konsolga chiqqan ma'lumotdan unumli foydalana olmaymiz. Konsoldagi 
# # qiymatni o'zgaruvchiga yuklab, undan kelajakda foydalanib ham bo'lmaydi. Mana 
# # shunday holatlarda, funksiyadan unumli foydalanish uchun undan biror qiymatni 
# # qaytarish maqsadga muvofiq bo'ladi.   """

# # #                  FUNKSIYADAN ODDIY QIYMAT QAYTARISH
# # #Keling ism va familiya degan parametrlarni olib, toliq_ism qaytaradigan sodda 
# # #funksiya yasaymiz.
# # def full_name_surname(ism, familya):
# #     """ full name and surname return function """
# #     full_n_s = f"{ism} {familya}"
# #     print(full_n_s)
# # # Bu funksiyadan foydalanish uchun quyidagicha foydalanamiz
# # full_name_surname("Ubaydullo", "Obidjanov")
# # # bu funksiyani kamchiligi shuki biz bu funksiyadagi {full_n_s} degen o'zgaruvchidan 
# # # foydalana olmaymiz funksiya faqatgina bu o'zgaruvchini consolga chiqardi holos 
# # # deylik kod yozish davomida bizga bu matn qayta qayta kerak bo'ldi, bizga bu matn 
# # # qanday qilib consolga emas o'zgaruvchiga saqlab olishimiz mumkin keling funksiya 
# # # bunday qilib ko'raylik

# # def full_name_surname(ism, familya):
# #     """ full name and surname return function """
# #     full_n_s = f"{ism} {familya}"
# #     #print(full_n_s)    bu yerda printni o'chirib tashlab o'rniga returndan foydalanamiz
# #     return full_n_s   #🛑 return ing(qaytarish ) return bu o'zgaruvchi emas uning 
# #    # qiymatini qaytaradi       mana funksiyani odatdagidek ishlatib  ko'raylik

# # full_name_surname("Ubaydullo", "Obidjanov") # bu yerda hech narsa chiqmaydi 
# # #yuqoridagi kodga qaraymiz 
# # #print(full_n_s) # deb bersak bizga hatolik chiqadi 
# # # sababi {full_n_s} funksiyani ichida qoladi yani LOCAL NAMES DEYILADI 
# # #🛑BIZGA FUNKSIYAMIZ QAYTARGAN QIYMAT KERAK BO'LSA BIZ UNI QANDAYDIR O'ZGARUVCHIGA 
# # # BERISHIMIZ KERAK KELING QUYIDAGICHA QILAMIZ 
# # talaba_1 = full_name_surname("Ubaydullo", "Obidjanov") # bu yerda funksiyamiz 
# # # qaytargan qiymatni talaba_1 ga bery1apmiz 
# # talaba_2 = full_name_surname("JO'raboyev"," Dilmurod") 
# # print(talaba_1)# keyinchalik bu talaba 1dan keyinchalik foydalanishimiz mumkin 
# # print(talaba_2)
# # talaba_3 = full_name_surname("Mirzamahmudov", "Behruzbek")
# # talba_4 = full_name_surname("Isroiljanov", "Islomjon")
# # print(f"Bugun darsga kelmagan o'quvchilar: {talaba_3}, {talba_4}")
# # # quyidaginga o'xshab funksiyamizdan va o'zgaruvchilarimizdan foydalanishimiz mumkin 
# # print(f"Talaba {talaba_1.title()} darsga kechikib keldi.")

# # ##############################################################################
# # #                       IXTIYORIY ARGUMENTLAR
# # # Avvalgi darsizmida funksiyalarga standart parametr berishni ko'rgan edik. Huddi
# # #   shu usul bilan, ba'zi argumentlarni ixtiyoriy qilishimiz mumkin. Ya'ni funksiya 
# # #   ishlashi uchun bu agrumentarni kiritish majburiy emas, ixtiyoriy bo'ladi.
# # # Keling avvalgi funksiyamizni o'zgartiramiz va unga yana bitta otasiningismi 
# # # degan paramter qo'shamiz, lekin bu parametr ixtiyoriy bo'ladi. Buning uchun 
# # # funksiya yaratishda otasining_ismi='' deb yozib ketamiz. 
# # def full_name_make(name,surname,father_name = ''):
# #     """ full name return  function """
# #     if father_name :
# #         full_name = f"{name} {surname} {father_name}"
# #     else: 
# #         full_name= f"{name} {surname}"
# #     return full_name.title()
# # talaba_1 = full_name_make('Husan', 'Obidov', 'Anvarovich')
        
# # talaba_2 = full_name_make('Hasan', 'Hakimov' )

# # print(f"Bugun darsga kelmagan o'quvchilar: \n{talaba_1}, \n{talaba_2}")

# # #################################################################################
# #                 FUNKSIYADAN LUG'AT QAYTARAMIZ
# # Funksiyadan sodda qiymat emas, ro'yxat, lu'gat va boshqa ma'lumot turlarini ham 
# # qaytarishimiz mumkin.  Quyidagi funksiya ham mashina haqidagi ma'lumotlarni 
# # jamlab, ularni lug'at ko'rinishida qaytaradi:

def car_info(kompaniya, model, rangi, korobka, yili, narxi= None):
    """ Bizga lug'at qaytaruvhchi funksiya"""
    car = {
        "model":model,
        "kompaniya": kompaniya, 
        "rangi": rangi,
        "korobka": korobka,
        "yili" : yili,
        "narxi": narxi
        }
    return car

car_1 = car_info('Shevrolet', 'matiz', 'oq', 'mehanik', 2016)
car_2 = car_info("daewo",'nexia','moykrasniy', 'avtomat',2004, 4500)
cars = [car_1, car_2]
for i in cars:
    if i['narxi']:
        cost = i['narxi']
    else: 
        print(f"{i['rangi']}, {i['model']} narxi: {cost}")
print("yangi avtolar ro'yhatini shakllantiramiz ")
car=[]
while True:
    kompaniya = input("Qaysi Kompaniya: ")
    model = input("Model: ")
    rangi = input("colour: ")
    korobka= input("Korobka: ")
    yili = input("yili: ")
    narxi = input("narxi: ")   
    car.append(car_info(kompaniya, model, rangi, korobka, yili))
    javob=input("again do you want to add new car ? NO/YES: ")
    if javob.lower()== "no":
        break 
    ############################################################################################
    
#     #VAZIFA 
#1.Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email
#  manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi
#  funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni
#  kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)


 #2.. Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar
 # degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni
 # konsolga chiqaring.

# def data(name, last_name, birth, adress, email ="", phone=None,):
#     """ foydalanuvchi haqida umumiy ma'lumot"""
#     malumot = {
#         'name': name,
#         "last_name": last_name,
#         "birth": birth,
#         "Adress" : adress,
#         "email": email,
#         "phone": phone
#         }
#     return malumot
# user_1= data("Ubaydullo", "Obidjanov", "1998.04.03","Chortoq")
# user_2 = data("Jo'raboyev"," Dilmurod"," 1998.04.21","Chortoq","1940Ubaydullo@gmail.com",98212198)
# customer =[]
# while True:
#     name= input("Ismizni kiriting: ")
#     last_name = input("input your last name: ")
#     birth=input("Input your birth date: ")
#     adress = input("Input your birth adress: ")
#     email = input("Input your email adress: ")
#     phone = input("input your phone number: ") 
#     customer.append(data(name, last_name, birth, adress,email,phone))
#     answer = input("again, do you add some date Not/Yes: ")
#     if  answer.lower()!= "yes":
#         break
# print(customer)

# for i  in customer:
#     print(
#         f"{i['name'].title()} {i['last_name']},"
#         f"{i['birth']} da tug'ilgan, phone number: {i['phone']} "
#     )
  ########################################
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# def katta(son1,son2, son3):
#     ''' find the largest number'''
#     katt = []
#     if son1> son2 and son1>son3:
#         katt.append(son1)
#     elif son2>son1 and son2>son3:
#         katt.append(son2)
#     elif son3>son1 and son3>son2:
#         katt.append(son3)
    
#     return katt
# son1 = float(input("birinchi sonni kriting: "))
# son2 = float(input("ikkinchi sonni kriting: "))
# son3 = float(input("uchinchi sonni kriting: "))
# kattason= katta(son1, son2, son3)
# print(kattason)
# def kattasi(x, y, z):#Soddaroq usuli
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max
# print(kattasi(21,30,30))
#################################################
#4.Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
# diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

# def aylana(r):
#     """Aylana haqida ma'lumot"""
#     data = {
#         "diametri": 2*r,
#         "radiusi" : r,
#         "uzunligi": 2*3.14*r,
#         "yuzasi": 3.14*r**2
#         }
#     return data
# radius = int(input("Aylana radiusini kiriting: "))
# print(aylana(radius))
#################################################
#5.Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub
# sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub(num1, num2):
#     """Tub sonlar """
#     tub_son = []
#     for son in range(num1,num2+1,):  #2....10
#       tub = True 
#       if son == 1:
#           tub = False
#       elif son == 2:
#          tub = True
#       else: 
#          for i in range(2,son):
#              if son%i==0:
#                  tub = False
#       if tub:
#         tub_son.append(son)
        
#     return tub_son

# print(tub(4,16))    
# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi
#  sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan 
#  oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi 
#  ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  
#  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# def fibionacci(son):
#     son1 = [1]
#     n = 1
#     for i in range(son):
#         son1.append(n)
#         n = son1[i] + n
     
#     return son1
# print(fibionacci(10))
       #to'g'ri javob 

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonacci(0))

yosh = 24
matn= "Mening \yoshim {} da."

print("Hello \0 world ")
print(matn.format(yosh))


print('Hello')









