import requests
import logging
from telegram.ext import *
from telegram.ext import Updater, CommandHandler
import responses
from bs4 import BeautifulSoup


def send_message_to_telegram_bot(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    updates_data = response.json()
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")
bot_token = "6922664008:AAFNwcljm-7LoGJsjNmGa63gYHUPzP69ts4"
chat_id = "709403071"
channel_username = "https://t.me/tgoldstore4"
url = 'https://ethiopianclothing.net/collections/ethiopian-kaba'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
price = soup.find_all('span', class_="money")
pricloop = [span.text for span in price[:10]]  
image_wraps = soup.find_all('div', class_='image-element__wrap')


for image_wrap in image_wraps:
    
    img_tag = image_wrap.find('img')
    if img_tag:
        image_url = img_tag.get('data-src')
        send_message_to_telegram_bot(bot_token, chat_id, image_url)
    else:
        print("No image found within this div tag")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('starting bot...')

def command1(update, context):
    for product_price, img_link in zip(pricloop, image_wraps):
        messages = []  
        img_tag = image_wrap.find('img')
        if img_tag:
         image_url = img_tag.get('data-src')
         message = f"Price: {product_price}\n{img_link}\n\n"
         messages.append(message) 

        send_message_to_telegram_bot(bot_token, chat_id, message.strip())


def mess_handl(update, context):
   text = str(update.message.text).lower()
   logging.info(f'user ({update.message.chat.id}) sayes: {text}')

   update.message.reply_text(text)


def error(update, context):
   logging.error(f'update {update} cused error {context.error}')



if __name__ == '__main__':
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('command1', command1))
    dp.add_handler(MessageHandler(Filters.text, mess_handl))
    dp.add_error_handler(error)

    updater.start_polling(1.0)
    updater.idel()
    