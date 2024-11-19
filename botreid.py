import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

API_TOKEN = '7594972467:AAFjn09gryrF7yawVn05fFSOP6V6udGWCtM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать в бот-расчетчик рейдов! Используйте /help, чтобы увидеть доступные команды.")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    help_text = (
        "/bobovka - Информация о Бобовой гранате\n"
        "/c4 - Информация о С4\n"  # Изменено на /c4
        "/torpeda - Информация о Торпеде\n"
        "/raketa - Информация о Ракете\n"
        "/molotov - Информация о Молотове\n"
        "/patron - Информация о Патроне\n"
        "/sachelnka - Информация о Сачельке\n"
        "/all - Все типы взрывчатки"
    )
    await message.reply(help_text)

@dp.message_handler(commands=['bobovka'])
async def bobovka_info(message: types.Message):
    info = (
        "🔷Бобовая граната / Бобовка🔷\n"
        "🔶Стены🔶\n"
        "Деревянная стена: 13 бобовок, 1560 серы\n"
        "Каменная стена: 46 бобовок, 5520 серы\n"
        "Железная стена: 112 бобовок, 13440 серы\n"
        "МВК стена: 223 бобовки, 26760 серы\n\n"
        "🔶Двери🔶\n"
        "Деревянная дверь: 6 бобовок, 720 серы\n"
        "Железная дверь: 18 бобовок, 2160 серы\n"
        "МВК дверь: 56 бобовок, 6720 серы\n"
        "Гаражная дверь: 42 бобовки, 5040 серы\n\n"
        "🔶Окна и оконные решетки🔶\n"
        "Деревянная оконная решетка: 13 бобовок, 1560 серы\n"
        "Железная оконная решетка: 56 бобовок, 6720 серы\n"
        "МВК решетка: 84 бобовки, 10080 серы\n"
        "Окно из укрепленного стекла: 56 бобовок, 6720 серы\n\n"
        "🔶Внешние стены и ворота🔶\n"
        "Деревянные ворота: 26 бобовок, 3120 серы\n"
        "Каменные ворота: 46 бобовок, 5520 серы\n"
        "Высокая деревянная стена: 26 бобовок, 3120 серы\n"
        "Высокая каменная стена: 46 бобовок, 5520 серы\n\n"
        "🔶Прочее🔶\n"
        "Шкаф: 3 бобовки, 360 серы\n"
        "Решётчатый настил: 18 бобовок, 2160 серы\n"
        "Люк с лестницей: 18 бобовок, 2160 серы\n"
        "Металлическая витрина магазина: 84 бобовки, 10080 серы\n"
        "Автоматическая турель: 16 бобовок, 1920 серы\n"
        "Гантрап/ловушка: 7 бобовок, 840 серы\n"
    )
    await message.reply(info)

@dp.message_handler(commands=['c4'])
async def c4_info(message: types.Message):
    info = (
        "🔷С4 / Сишка🔷\n"
        "🔶Стены🔶\n"
        "Деревянная стена: 1 штука, 2200 серы\n"
        "Каменная стена: 2 штуки, 4400 серы\n"
        "Железная стена: 4 штуки, 8800 серы\n"
        "МВК стена: 8 штук, 17600 серы\n\n"
        "🔶Двери🔶\n"
        "Деревянная дверь: 1 штука, 2200 серы\n"
        "Железная дверь: 1 штука, 2200 серы\n"
        "МВК дверь: 3 штуки, 6600 серы\n"
        "Гаражная дверь: 2 штуки, 4400 серы\n\n"
        "🔶Окна и оконные решетки🔶\n"
        "Деревянная оконная решетка: 1 штука, 2200 серы\n"
        "Железная оконная решетка: 2 штуки, 4400 серы\n"
        "МВК решетка: 2 штуки, 4400 серы\n"
        "Окно из укрепленного стекла: 2 штуки, 4400 серы\n\n"
        "🔶Внешние стены и ворота🔶\n"
        "Деревянные ворота: 2 штуки, 4400 серы\n"
        "Каменные ворота: 2 штуки, 4400 серы\n"
        "Высокая деревянная стена: 2 штуки, 4400 серы\n"
        "Высокая каменная стена: 2 штуки, 4400 серы\n\n"
        "🔶Прочее🔶\n"
        "Шкаф: 1 штука, 2200 серы\n"
        "Решётчатый настил: 1 штука, 2200 серы\n"
        "Люк с лестницей: 1 штука, 2200 серы\n"
        "Металлическая витрина магазина: 3 штук, 6600 серы\n"
        "Автоматическая турель: 1 штука, 2200 серы\n"
        "Гантрап/ловушка: 1 штука, 2200 серы\n"
    )
    await message.reply(info)

@dp.message_handler(commands=['torpeda'])
async def torpeda_info(message: types.Message):
    info = (
        "🔷Торпеда🔷\n"
        "🔶Стены / пиллары🔶\n"
        "Деревянная стена: 20 штук, 420 серы\n"
        "Каменная стена: 81 штука, 1620 серы\n"
        "Железная стена: 200 штук, 4020 серы\n"
        "МВК стена: 400 штук, 8040 серы\n\n"
        "🔶Двери🔶\n"
        "Деревянная дверь: 8 штук, 180 серы\n"
        "Железная дверь: 32 штуки, 660 серы\n"
        "МВК дверь: 100 штук, 2040 серы\n"
        "Гаражная дверь: 75 штук, 1500 серы\n"
    )
    await message.reply(info)

@dp.message_handler(commands=['raketa'])
async def raketa_info(message: types.Message):
    info = (
        "🔷Ракета🔷\n"
        "🔶Стены🔶\n"
        "Деревянная стена: 2 штуки, 2800 серы\n"
        "Каменная стена: 4 штуки, 5600 серы\n"
        "Железная стена: 8 штук, 11200 серы\n"
        "МВК стена: 15 штук, 21000 серы\n\n"
        "🔶Двери🔶\n"
        "Деревянная дверь: 1 штука, 1400 серы\n"
        "Железная дверь: 2 патрона, 2800 серы\n"
        "МВК дверь: 5 штук, 7000 серы\n"
        "Гаражная дверь: 3 штуки, 4200 серы\n\n"
        "🔶Окна и оконные решетки🔶\n"
        "Деревянная оконная решетка: 1 штука, 1400 серы\n"
        "Железная оконная решетка: 2 штуки, 2800 серы\n"
        "МВК решетка: 4 штуки, 5600 серы\n"
    )
    await message.reply(info)

@dp.message_handler(commands=['molotov'])
async def molotov_info(message: types.Message):
    info = (
        "🔷Молотов🔷\n"
        "🔶Стены🔶\n"
        "Деревянная стена: 3 молотова\n"
        "Каменная стена: 6 молотов\n"
        "Железная стена: 10 молотов\n"
        "МВК стена: 15 молотов\n\n"
        "🔶Двери🔶\n"
        "Деревянная дверь: 2 молотова\n"
        "Железная дверь: 4 молотова\n"
        "МВК дверь: 7 молотов\n"
    )
    await message.reply(info)

@dp.message_handler(commands=['patron'])
async def patron_info(message: types.Message):
    info = (
        "🔷Патрон🔷\n"
        "🔶Стены🔶\n"
        "Деревянная стена: 56 шт  патронов,1400 серы\n"
        "Каменная стена: 200 шт патронов, 5020 серы\n"
        "Железная стена: 400 шт патронов, 10000 серы\n"
        "МВК стена: 800 шт патронов, 20000серы\n\n"
        "🔶Двери🔶\n"
        "Деревянная дверь: 20шт патронов,500серы\n"
        "Железная дверь: 63ипатронов, 1575 серы\n"
        "МВК дверь: 200шт патронов,5020 серы\n"
       "Гаражная дверь: 150шт патронов,3750 серы\n"
    )
    await message.reply(info)

@dp.message_handler(commands=['sachelnka'])
async def sachelnka_info(message: types.Message):
    info = (
        "🔷Сачелька🔷\n"
        "🔶Стены🔶\n"
        "Деревянная стена: 2 сачельки\n"
        "Каменная стена: 4 сачельки\n"
        "Железная стена: 6 сачелек\n"
        "МВК стена: 8 сачелек\n\n"
        "🔶Двери🔶\n"
        "Деревянная дверь: 1 сачелька\n"
        "Железная дверь: 3 сачельки\n"
    )
    await message.reply(info)

@dp.message_handler(commands=['all'])
async def all_info(message: types.Message):
    all_info_text = (
        "Доступные команды:\n"
        "/bobovka - Информация о Бобовой гранате\n"
        "/c4 - Информация о С4\n"
        "/torpeda - Информация о Торпеде\n"
        "/raketa - Информация о Ракете\n"
        "/molotov - Информация о Молотове\n"
        "/patron - Информация о Патроне\n"
        "/sachelnka - Информация о Сачельке\n"
    )
    await message.reply(all_info_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)