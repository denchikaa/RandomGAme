from aiogram import Bot,Dispatcher,executor,types

import config
import random

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Здравствуйте")

@dp.message_handler(text = ['1','2','3'])
async def random2(message: types.Message):
    user = int(message.text)
    randomer = random.randint(1, 3)

    await message.answer("Я загадал чило от 1 до 3, Вы должны его отгадать!")
    if user == randomer:
        await message.reply(f"Вы угадали. Мое число {randomer}")

    else:
        await message.reply(f"Вы не угадали. Мое число {randomer}")

executor.start_polling(dp)