import logging
from aiogram.utils import executor
from aiogram import Dispatcher, Bot

import func_bot
from func_bot import TOKEN, start_command
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
func_bot.register_handler_func(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
