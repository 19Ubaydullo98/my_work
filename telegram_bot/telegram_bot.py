from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = '6552407128:AAH5pqyj0IoV4zyv-QFDFbpW1F1yRn9VDdo'
bot = telebot.TeleBot(TOKEN, parse_mode=None)
matn = input("Matn kriting: ")
# print(to_cyrillic(matn))

#Biz klaviaturadagi barcha harflar kompyuterga o'girilishida isascii kodi orqali 
#hisoblaydi va buni hozir ko'ramiz 
# matn='osh'
# print(matn.isascii()) #Natija: True

# matn = 'ош'
# print(matn.isascii()) # Natija: False 
# Biz Shu orqali foydalanuvchi kiritgan so'znni lotin yoki kril ekanini bilib olamiz 
 
if matn.isascii():
    print(to_cyrillic(matn))
else: 
    print(to_latin(matn))
    


