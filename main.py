import time
from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
import string

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

HELP = (f"/start - Приветствие. \n"
        f"/help -  Помощь по командам. \n"
        f"/info -  Справка о паролях \n"
        f"/me -  Обо мне. \n")

@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    await message.answer(f'''
    Привет, {message.from_user.first_name}, я бот - генератор паролей  🎰 
Если нужно сгенерировать надежный пароль - обращайтесь  😉
Введите число символов для будущего пароля (от 6 до 64)  ⌨️
/help -  Помощь по командам 🤓
    ''')

@dp.message_handler(commands=['help'])
async def help_command(message):
    await message.answer(HELP)
    await message.delete()

@dp.message_handler(commands=['info'])
async def help_command(message):
    await message.answer("""🤓Сила пароля характеризуется энтропией — числовым представлением количества случайности, которая содержится в пароле. Поскольку речь идёт о больших числах, то вместо 1 099 511 627 776 (2^40) нам проще сказать «40 бит энтропии». И поскольку взлом пароля — это перебор вариантов, то чем их больше, тем больше времени нужно затратить на взлом.

Для случайных символов, сгенерированных менеджером паролей, энтропия считается по формуле: log2(<количество разных символов> ^ <длина>)

😎Пароли, сгенерированные мной имеют силу не менее 40 бит.""")
    await message.delete()

@dp.message_handler(commands=['me'])
async def help_command(message):
    await message.answer("""Я бот - генератор паролей, созданный чтобы защитить приватные данные кожаных. Мою внешность создала MidJourney, а мои мозги - заслуга пользователя 'Ilya'. 
    Я объединяю строчные, заглавные буквы английского алфавита с числами и различными знаками в список, а потом почти рандомно генерирую из них пароль заданной длины. 💻""")
    await message.delete()


@dp.message_handler()
async def get_password(message: types.message):
    passlenght = message.text
    try:
        passlenght = int(passlenght)
        if passlenght > 64 or passlenght < 6:
            await message.reply('❌Недопустимый размер пароля❌')
        else:
            a = string.ascii_letters
            b = string.octdigits
            c = string.punctuation

            await message.answer("Заряжаю пароль энтропией ...")
            time.sleep(1)

            password = ''.join(random.sample((a+b+c), passlenght))

            await message.reply(f"""🎉Мои поздравления! 
            Ваш пароль готов: {password}""")
            await message.answer('Введите число символов для будущего пароля (от 6 до 64) и приступим 🚀')


    except Exception as ex2:
        print(ex2)
        await message.answer('Введите число символов для будущего пароля (от 6 до 64) и приступим 🚀')

if __name__ == '__main__':
    executor.start_polling(dp)