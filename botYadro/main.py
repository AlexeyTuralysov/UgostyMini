import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery, InlineKeyboardButton, file, LabeledPrice
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import CommandStart, Command
from sqlalchemy.ext.asyncio import AsyncSession

from admin.commands import router as admincommands
from userCommands.userCommands import router as usercommands

from aiogram import F
import asyncio

from Base.models.model import TelegramProfile
from sqlalchemy.future import select

from Base.database import get_session
from Base.models.model import TelegramPostsWithBot

from aiogram.types.input_file import FSInputFile

from admin.builder.classBuilder import builderPostsClass




TOKEN = ""
PAYMENT_PROVIDER_TOKEN = '381764678:TEST:108057'

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
dp.include_routers(admincommands)
dp.include_router(usercommands)

import logging



logging.basicConfig(level=logging.INFO)


@dp.message(Command("pay"))
async def process_payment(message: Message):
    # Цены на товары
    prices = [
        LabeledPrice(label="Бургер", amount=50000),  # 50000 копеек = 500 рублей
        LabeledPrice(label="Картофель фри", amount=30000)
    ]

    # Отправка счета на оплату
    await bot.send_invoice(
        message.chat.id,
        title="Заказ в Durger King",
        description="Ваш заказ: Бургер и картофель фри",
        payload="burger-order-001",  # Идентификатор заказа
        provider_token=PAYMENT_PROVIDER_TOKEN,
        currency="RUB",
        prices=prices,
        start_parameter="burger-order",
        photo_url="https://example.com/burger.jpg",  # Картинка товара
        photo_width=512,
        photo_height=512,
        photo_size=512,
    )


async def getUsers():
    async for session in get_session():
        res = await session.execute(select(TelegramProfile))
        TgBotUsers = res.scalars().all()
        return TgBotUsers




async def get_lastPost(session: AsyncSession):
    result = await session.execute(
        select(TelegramPostsWithBot).order_by(TelegramPostsWithBot.id.desc()).limit(1)
    )
    last_post = result.scalar_one_or_none()  # Извлекаем один пост или None, если нет
    return last_post





@dp.message(Command("ms"))
async def echo_handler(message: Message) -> None:
    async for session in get_session():

        res = await session.execute(select(TelegramProfile))
        users = res.scalars().all()

        lastPost = await get_lastPost(session)


        photo = FSInputFile(lastPost.thumbnail)


        builder = builderPostsClass(message,
                                    state=None,
                                    thumbnail=None,
                                    thumbnail_src=photo,
                                    text=lastPost.text,
                                    button_text=lastPost.button_text,
                                    button_link=lastPost.button_link)

        if not users:
            break

        for user in users:
            # Используем метод PostTemplate для отправки
            await builder.PostTemplate(chat_id=user.chat_id)

        await message.reply("Успешная рассылка!")



@dp.message(Command("last"))
async def echo_handler(message: Message) -> None:
    async for session in get_session():


        lastPost = await get_lastPost(session)
        

        if lastPost:

            caption = f"Последний пост:\n\n{lastPost.text}\n\n"
            if lastPost.button_text and lastPost.button_link:
                caption += f"Кнопка: {lastPost.button_text}\nСсылка: {lastPost.button_link}"

            if lastPost.thumbnail and os.path.exists(lastPost.thumbnail):


                photo = FSInputFile(lastPost.thumbnail)

                await message.answer_photo(photo=photo, caption=caption)
            else:
                await message.answer(caption)
        else:
            await message.answer("Нет постов в базе.")






@dp.message(CommandStart())
async def echo_handler(message: Message) -> None:
    async for session in get_session():

        async with session.begin():
            #test = session.query(exists().where(TelegramProfile.id_telegram == message.from_user.id)).scalar()
            q = select(TelegramProfile)
            check_user_in_base = await session.execute(q)
            curr = check_user_in_base.scalars()

            try:
                newUser = TelegramProfile(id_telegram=message.from_user.id, chat_id=message.chat.id)
                session.add(newUser)
                await session.commit()
                await message.answer(f"Вы сохранены {message.from_user.id}!")



            except:
                await message.answer(f"Вы уже ЕСТЬ {message.from_user.id}!")

        await message.answer(f"Операция выполнена")



@dp.message(Command("/status"))
async def echo_handler(message: Message) -> None:
    async for session in get_session():
        res = await session.execute(select(TelegramProfile))
        users = res.scalars().all()

        if users:

            sers_list = "\n".join([f"{user.id_telegram} (ID: {user.chat_id})" for user in users])
            await message.answer(f"Всего пользователей {sers_list}")

        else:

            await message.answer(f"никого нету")





instruction_caption = (
    'step 1',
    'step 2',
    'step 3',
    'step 4',
    'step 5',
    'step 6',
    'step 7',
    'step 8'
)

#ITEMS = [f"Product {i}" for i in range(1, 21)]  # Список товаров от 1 до 20
ITEMS_PER_PAGE = 5


def getPages(page: int, total_pages: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    if page > 1:
        builder.add(InlineKeyboardButton(text="назад", callback_data=f"prev:{ page - 1}"))

    if page < total_pages:
        builder.add(InlineKeyboardButton(text="вперед", callback_data=f"next:{ page + 1}"))

    return builder.as_markup()


async def showProducts(chat_id: int, message_id: int, page: int) -> None:

    total_pages = (len(instruction_caption) + ITEMS_PER_PAGE - 1 ) // ITEMS_PER_PAGE
    startPage = (page - 1) * ITEMS_PER_PAGE
    endPage = startPage + ITEMS_PER_PAGE

    itemsOnPage = instruction_caption[startPage:endPage]

    message_text = f"Страница {page}/{total_pages}\n\n"
    message_text += "\n".join(itemsOnPage)

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message_text,
        reply_markup=getPages(page=page, total_pages=total_pages)
    )


@dp.callback_query(F.data.startswith('prev:'))
async def backPage(callback: CallbackQuery) -> None:

    page = int(callback.data.split(":")[1])

    await showProducts(callback.message.chat.id, callback.message.message_id ,page=page)
    await callback.answer()

@dp.callback_query(F.data.startswith('next:'))
async def nextPage(callback: CallbackQuery) -> None:
    page = int(callback.data.split(":")[1])
    await showProducts(callback.message.chat.id, callback.message.message_id , page=page)
    await callback.answer()

@dp.message(Command("prod"))
async def prod_handler(message: Message) -> None:
    send_mesage = await bot.send_message(
        message.chat.id, text="Загрузка страницы...",
        reply_markup=getPages(page=1, total_pages=(len(instruction_caption) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE))
    await showProducts(chat_id=message.chat.id,message_id=send_mesage.message_id ,page=1)



@dp.message(Command('pages_'))
async def pages(message: Message) -> None:

        await message.answer(f"ваш адйи {message.from_user.id}")



async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())