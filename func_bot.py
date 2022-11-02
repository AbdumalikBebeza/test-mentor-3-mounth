from aiogram import Bot, Dispatcher, types
import random
import asyncio
from decouple import config
TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


async def start_command(message: types.Message):
    await message.answer(f"Добро пожаловать {message.from_user.username}\n"
                         f"Хочешь мемы нажми /mem\n"
                         f"Хочешь послушать музыку нажми /music\n"
                         f"хочешт поиграть в рандомную мини-игру нажми /dice\n"
                         f"можешь покидать кости с ботом нажав на /game\n"
                         f"этот бот создан чисто что бы пройти тест на менторство!\n")


async def music(message: types.Message):
    audios = (
        'media/AUD-20220103-WA0018.mp3',
        'media/Bakr - Эталон Красоты.mp3',
        'media/mende kanday kyne bar_ speed up.mp3',
        'media/Sharara sharara rmx_️.mp3',
        'media/Xcho_Eskizy.mp3',
        'media/Xcho_Malaya.mp3',
        'media/Дама босиком на берегу .mp3',
        'media/Мурашки - V X V PRiNCE.mp3',
    )
    audio = open(random.choice(audios), 'rb')
    await bot.send_audio(message.from_user.id, audio=audio)


async def mem(message: types.Message):
    photos = (
        'media/mem1.jpg',
        'media/mem2.jpg',
        'media/mem3.jpg',
        'media/mem4.jpg',
        'media/mem5.jpg',
        'media/mem6.jpg',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


async def game(message: types.Message):
    data = ['⚽', '🏀', '🎯', '🎰', '🎳', '🎲']
    r = random.choice(data)
    await bot.send_dice(message.chat.id, emoji=r)


async def dice_game(message: types.Message):
    bot_dice = await bot.send_dice(message.chat.id)
    user_dice = await bot.send_dice(message.chat.id)
    await message.answer("первый игральный кость бота а второй игрока")
    if bot_dice.dice.value > user_dice.dice.value:
        await asyncio.sleep(5)
        await message.answer(f"Бот выиграл {message.from_user.full_name}!")
    elif bot_dice.dice.value == user_dice.dice.value:
        await asyncio.sleep(5)
        await message.answer("Ничья")
    else:
        await asyncio.sleep(5)
        await message.answer(f"{message.from_user.full_name} выиграл бота!")


def register_handler_func(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'info'])
    dp.register_message_handler(music, commands=['music'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(game, commands=['dice'])
    dp.register_message_handler(dice_game, commands='game')

