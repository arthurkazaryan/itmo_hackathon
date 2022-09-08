from django.core.management.base import BaseCommand
from aiogram.utils import executor
from tgbot.bot.handlers import client
from tgbot.bot.create_bot import dp


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):

        async def on_startup(_):
            print('Запуск бота')

        client.register_handlers_client(dp)

        executor.start_polling(
            dp,
            skip_updates=True,
            on_startup=on_startup
        )
