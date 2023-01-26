import asyncio
from aiogram import Bot, Dispatcher, executor

loop = asyncio.new_event_loop()
bot = Bot("1878898481:AAHBhPKTn63PV5fCAGN4O8Ubuu7lLiJse7Q", parse_mode='HTML')
dp = Dispatcher(bot, loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
