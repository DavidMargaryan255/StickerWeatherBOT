import telebot
import requests
import json

def number_to_emoji(number):
    return ' '.join([f'{d}\uFE0F\u20E3' for d in str(number)])

bot = telebot.TeleBot('7060898035:AAFhBE-rroyCZgEcTdxVB2C1MVTNkTPj6lM')
API_KEY = 'dda82ef907f6cae64dad2657ddc51a7f'

condit = {
    "clear sky": "☀️",
    "few clouds": "🌤",
    "scattered clouds": "⛅️",
    "broken clouds": "☁️",
    "overcast clouds": "☁️",
    "shower rain": "🌧",
    "rain": "🌦",
    "thunderstorm": "🌩",
    "snow": "🌨",
    "mist": "😶‍🌫️"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Բարև սիրելի հաճախորդ, Դուք այցելել եք Գագիկ Սուրենյանի գրասենյակ")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        num = round(float(data["main"]["temp"]))
        description = data["weather"][0]["description"]
        if num>9:
            num1=int(num/10)
            num2=num%10
            emoji_number1 = number_to_emoji(num1)
            emoji_number2 = number_to_emoji(num2)
            bot.send_message(message.chat.id ,f'{emoji_number1}{emoji_number2}')
        elif num<10 and num >=0:
            emoji_number = number_to_emoji(num)
            bot.send_message(message.chat.id ,f'{emoji_number}')
        else:
            emoji_number = number_to_emoji(num)
            bot.send_message(message.chat.id ,f'➖{emoji_number}')
        if description in condit:
            bot.send_message(message.chat.id, f'{condit[description]}')
        else:
            bot.send_message(message.chat.id, f'Weather: {description.capitalize()}')
    else:
        bot.send_message(message.chat.id, "City not found or API request failed.")

bot.polling(none_stop=True)
