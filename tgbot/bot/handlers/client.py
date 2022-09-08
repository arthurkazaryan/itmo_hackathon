from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from accounts.models import Profile
from django.contrib.auth.models import User
from tgbot.bot.create_bot import bot
from tgbot.bot.keyboards.user import kb_client


import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


class FSMRegister(StatesGroup):
    username = State()


async def commands_start(message: types.Message):
    reply_message = f"{message.from_user.first_name}, Добро пожаловать в телеграм-бот команды ХаХатонщики!\n" \
                    f"Пройдите авторизацию, если вы еще не авторизованы."

    await bot.send_message(message.from_user.id, reply_message, reply_markup=kb_client())


async def commands_register(message: types.Message):
    reply_message = f"{message.from_user.first_name}, введите, пожалуйста, ваш логин на сайте ХаХатонщиков.\n" \

    await bot.send_message(message.from_user.id, reply_message, reply_markup=kb_client())
    await FSMRegister.username.set()


async def commands_username(message: types.Message, state: FSMRegister):

    try:
        user = User.objects.filter(username=message.text)[0]
        user_profile = Profile.objects.filter(user=user)[0]
        user_profile.chat_id = message.from_user.id
        user_profile.save()
        reply_message = f'Вы успешно зарегистрированы в сервисе ХаХатонщиков.'
    except:
        reply_message = f'{message.text} пользователя не существует.'
    await state.finish()
    await message.reply(reply_message)


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(commands_start, commands=['start'])
    dispatcher.register_message_handler(commands_register, commands=['register'])
    dispatcher.register_message_handler(commands_username, state=FSMRegister.username)
