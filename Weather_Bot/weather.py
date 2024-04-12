import telebot
#0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣
import requests
import json
def number_to_emoji(number):
    return ' '.join([f'{d}\uFE0F\u20E3' for d in str(number)])
bot = telebot.TeleBot('7060898035:AAFhBE-rroyCZgEcTdxVB2C1MVTNkTPj6lM')
API ='dda82ef907f6cae64dad2657ddc51a7f'
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,"Բարև սիրելի հաճախորդ, Դուք այցելել եք Գագիկ Սուրենյանի գրասենյակ")
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city=message.text.lower()
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data=json.loads(res.text)
    num=round(float(data["main"]["temp"]))
    print(type(num))
    if num>9:
        num1=int(num/10)
        num2=num%10
        emoji_number1 = number_to_emoji(num1)
        emoji_number2 = number_to_emoji(num2)
        bot.send_message(message.chat.id ,f'{emoji_number1}{emoji_number2}')
bot.polling(none_stop=True)
