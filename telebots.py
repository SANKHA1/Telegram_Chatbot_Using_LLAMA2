# import telegram
import requests
import telebot
from google.generativeai import configure, GenerativeModel

# Replace with your credentials
bot_token = '6949015079:AAHJ7-aang9ZQ2-RB2OT-mUrRvQa94Zsukc'
gemini_api_key = 'AIzaSyATMbR4kzDQDm_VgAG-EQXZxSajfVjdBBg'

# bot = telegram.Bot(token=bot_token)
bot= telebot.TeleBot(bot_token)
# bot= telebot.bot(bot_token)
configure(api_key=gemini_api_key)  # Configure Google Generative AI library
# model = GenerativeModel.create("gemini-pro")  # Create a Gemini Pro model instance
# model = GenerativeModel.from_model_id("gemini-pro")
model = GenerativeModel("gemini-pro")
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = f"{message.text}\n\nRespond as a helpful and informative bot:"
    # response = model.generate_text(prompt, max_tokens=150, temperature=0.7)
    # response = model.generate_content(prompt, max_tokens=150, temperature=0.7)
    response = model.generate_content(prompt)
    bot.send_message(chat_id=message.chat.id, text=response.text)

bot.polling()
