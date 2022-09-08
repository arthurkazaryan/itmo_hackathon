from tgbot.bot.create_bot import bot
from settings import TELEGRAM_BOT_TOKEN
import requests


def send_warning_message(chat_id, text_to_send):

    requests.get(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text_to_send}&parse_mode=HTML")
