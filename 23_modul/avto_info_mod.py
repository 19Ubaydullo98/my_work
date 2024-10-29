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


#################
def avto_kirit():
    print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")

    
    car = []
    while True:
        print("Quyidagi ma'lumotlarni kiriting:", end="")
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
# print("Salonimizdagi avtolar: ")
# for avto in car:
#     if avto['narxi']:
#         narh = avto['narxi']
#     else: 
#         narh = 'nomalum'
#     print(f"{avto['rangi']} {avto['model']}, {'korobka'} korobka, Narxi: {narh}")
# ##############
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yili']}-yil, {avto_info['narxi']}$")

# print(info_print(avto_kirit))