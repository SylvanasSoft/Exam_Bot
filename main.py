import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from reply import start, bot_menu, man_woman, week_days
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, BIGINT, insert, select
from sqlalchemy.orm import declarative_base, Mapped, Session, mapped_column

# https://t.me/illegal_testing_bot
TOKEN = "6408363442:AAFQdRmPBBJpTi1_S59VC6zppaFXDVTFGrA"
dp = Dispatcher()
choosing = "Quydagilardan birontasini tanlang 👇🏿"

file = "AgACAgIAAxkBAAICyGVxoNZw4V7dYVKyA4LCyFZsEB56AAJS0zEbVxSRSwfrKkVSj3XlAQADAgADcwADMwQ"
photo_caption = "Assalomu alaykum !\nBu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi"

load_dotenv()
Base = declarative_base()


class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_CONFIG = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


engine = create_engine(Config().DB_CONFIG)
session = Session(engine)


class User(Base):
    __tablename__ = 'bot_users'
    id: Mapped[int] = mapped_column(__type_pos=BIGINT, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(__type_pos=BIGINT, unique=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=True)


Base.metadata.create_all(engine)


@dp.message(CommandStart())
async def bot_start(msg: Message) -> None:
    user_data = {
        'user_id': msg.from_user.id,
        'first_name': msg.from_user.first_name,
        'last_name': msg.from_user.last_name,
        'username': msg.from_user.username
    }
    user: User | None = session.execute(select(User).where(User.user_id == msg.from_user.id)).fetchone()
    if not user:
        query = insert(User).values(**user_data)
        session.execute(query)
        session.commit()
    await msg.answer_photo(photo=file, caption=photo_caption, reply_markup=bot_menu())


@dp.message(lambda msg: msg.text == "Start ✅")
async def start_training_handler(msg: Message):
    await msg.answer(text=choosing, reply_markup=start())


@dp.message(lambda msg: msg.text == "Woman️")
@dp.message(lambda msg: msg.text == "Men")
async def man_woman_handler(msg: Message):
    await msg.answer(text=choosing, reply_markup=man_woman())


@dp.message(lambda msg: msg.text == "1-oy")
@dp.message(lambda msg: msg.text == "2-oy")
@dp.message(lambda msg: msg.text == "3-oy")
@dp.message(lambda msg: msg.text == "4-oy")
async def weekday_handler(msg: Message):
    await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=week_days())


@dp.message(lambda msg: msg.text == 'Dushanba')
@dp.message(lambda msg: msg.text == 'Seshanba')
@dp.message(lambda msg: msg.text == 'Chorshanba')
@dp.message(lambda msg: msg.text == 'Payshanba')
@dp.message(lambda msg: msg.text == 'Juma')
@dp.message(lambda msg: msg.text == 'Shanba')
async def training(msg: Message):
    await msg.answer(text="Dalshe ma'lumot yo'q 😉😄", reply_markup=week_days())


@dp.message(lambda msg: msg.text == '🔙 Back')
async def back(msg: Message):
    await msg.answer_photo(photo=file, caption=photo_caption, reply_markup=start())


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
