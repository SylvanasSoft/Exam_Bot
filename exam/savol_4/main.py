import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from reply import start, bot_menu, man_woman, week_days
from utils import *

# https://t.me/illegal_testing_bot
TOKEN = "6408363442:AAFQdRmPBBJpTi1_S59VC6zppaFXDVTFGrA"
dp = Dispatcher()
choosing = "Quydagilardan birontasini tanlang 👇🏿"

file = "AgACAgIAAxkBAAICyGVxoNZw4V7dYVKyA4LCyFZsEB56AAJS0zEbVxSRSwfrKkVSj3XlAQADAgADcwADMwQ"
photo_caption = "Assalomu alaykum !\nBu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi"


class UserStates(StatesGroup):
    first_menu = State()
    choosing_male = State()
    months = State()
    weeks = State()
    back = State()


@dp.message(CommandStart())
async def bot_start_handler(msg: Message) -> None:
    await msg.answer_photo(photo=file, caption=photo_caption, reply_markup=bot_menu())


@dp.message(UserStates.first_menu)
@dp.message(lambda msg: msg.text == "Start ✅")
async def start_training_handler(msg: Message, state: FSMContext):
    await msg.answer(text=choosing, reply_markup=start())
    await state.set_state(UserStates.choosing_male)


@dp.message(lambda msg: msg.text == "Admin 👨🏻‍💻")
async def admin_handler(msg: Message):
    await msg.answer(text="https://t.me/ieee01", reply_markup=bot_menu())


@dp.message(lambda msg: msg.text == "Filial 📍")
async def admin_handler(msg: Message):
    await msg.answer_location(latitude=41.304476, longitude=69.253043, reply_markup=bot_menu())


@dp.message(lambda msg: msg.text == "NewsPost")
async def news_handler(msg: Message):
    text1 = f"""
title: {data1.get('title')}
desc: {data1.get('caption')}
time: {data1.get('time')}
"""
    text2 = f"""
title: {data2.get('title')}
desc: {data2.get('caption')}
time: {data2.get('time')}
"""
    text3 = f"""
title: {data3.get('title')}
desc: {data3.get('caption')}
time: {data3.get('time')}
"""
    text4 = f"""
title: {data4.get('title')}
desc: {data4.get('caption')}
time: {data4.get('time')}
"""
    await msg.answer_photo(photo=data1.get('photo_file'), caption=text1)
    await msg.answer_photo(photo=data2.get('photo_file'), caption=text2)
    await msg.answer_photo(photo=data3.get('photo_file'), caption=text3)
    await msg.answer_photo(photo=data4.get('photo_file'), caption=text4)


@dp.message(UserStates.choosing_male)
async def man_woman_handler(msg: Message, state: FSMContext):
    if msg.text == '🔙 Back':
        await msg.answer_photo(photo=file, caption=photo_caption, reply_markup=start())
        await state.set_state(UserStates.first_menu)
    else:
        await msg.answer(text=choosing, reply_markup=man_woman())
        await state.set_state(UserStates.months)


@dp.message(UserStates.months)
async def weekday_handler(msg: Message, state: FSMContext):
    if msg.text == '🔙 Back':
        await msg.answer_photo(photo=file, caption=photo_caption, reply_markup=start())
        await state.set_state(UserStates.first_menu)
    else:
        await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=week_days())
        await state.set_state(UserStates.weeks)


@dp.message(UserStates.weeks)
async def training(msg: Message, state: FSMContext):
    if msg.text == '🔙 Back':
        await msg.answer_photo(photo=file, caption=photo_caption, reply_markup=start())
        await state.set_state(UserStates.first_menu)
    else:
        await msg.answer(text="Dalshe ma'lumot yo'q 😉😄", reply_markup=week_days())


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
