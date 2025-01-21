import os
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram import types

from admin.builder.classBuilder import builderPostsClass
from admin.decorations.adminDecoration import for_admin

from Base.database import get_session


from .db_operation import NewPostDataInBase

import logging



logging.basicConfig(level=logging.INFO)

class Post(StatesGroup):
    thumbnail = State()
    thumbnail_src = State()
    text = State()
    button_text = State()
    button_link = State()


router = Router()


@router.message(Command('create'))
@for_admin
async def create_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Post.thumbnail)
    #await message.answer("Закинь  картинку в формате .jpg")
    await message.answer_photo(types.FSInputFile("./static/embeddedpic/Asset 2.png"), caption="Отправь мне картинку в формате .jpg или же .png")




@router.message(Post.thumbnail)
async def thumbnail_handler(message: Message, state: FSMContext) -> None:
    if message.text == "/empty":
        await state.update_data(thumbnail=None)
        await state.set_state(Post.button_text)
        await message.answer("Заголовок для кнопки (если кнопка не нужна, напишите: /empty)")
    else:
        await state.update_data(thumbnail=message.photo[-1].file_id)

        await state.update_data(thumbnail_src=f"{message.photo[-1].file_id}.jpg")
        await message.bot.download(file=message.photo[-1].file_id, destination=f"./static/thumbnailPost/{message.photo[-1].file_id}.jpg")



        await state.set_state(Post.button_text)
        #await message.answer("Заголовок для Кнопки")
        await message.answer_photo(types.FSInputFile("./static/embeddedpic/Asset 3.png"), caption="Отправь мне заголовок для Кнопки")


@router.message(Post.button_text)
async def button_text_handler(message: Message, state: FSMContext) -> None:
    if message.text == "/empty":
        await state.update_data(button_text=None)
        await state.set_state(Post.button_link)
        await message.answer("Cсылка (если кнопка не нужна, напишите: /empty)?")
    else:
        await state.update_data(button_text=message.text)
        await state.set_state(Post.button_link)

        #await message.answer("Cсылка?")
        await message.answer_photo(types.FSInputFile("./static/embeddedpic/Asset 5.png"),
                                   caption="Отправь мне ссылку в формате желательно с https, чтобы твои пользователи не видели сообщение о возможной угрозе.")


@router.message(Post.button_link)
async def button_link_handler(message: Message, state: FSMContext) -> None:
    if message.text == "/empty":
        await state.update_data(button_link=None)
        await state.set_state(Post.text)
        await message.answer("Введите текст")
    else:
        await state.update_data(button_link=message.text)
        await state.set_state(Post.text)
        #await message.answer("Введите текст")
        await message.answer_photo(types.FSInputFile("./static/embeddedpic/Asset 4.png"),
                                   caption="Отправь мне текст для твоего поста.")



@router.message(Post.text)
async def post_text_handler(message: Message, state: FSMContext) -> None:
    async for session in get_session():
        async with session.begin():

            await state.update_data(text=message.text)
            data = await state.get_data()

            thumbnail = data.get('thumbnail')
            thumbnail_src = data.get('thumbnail_src')
            text = data.get('text')
            button_text = data.get('button_text')
            button_link = data.get('button_link')

            logging.info(f"Перед сохранением в БД: Thumbnail: {thumbnail}, Text: {text}, Button Text: {button_text}, Button Link: {button_link}")


            builder = builderPostsClass(message,
                                        state,
                                        thumbnail,
                                        thumbnail_src,
                                        text,
                                        button_text,button_link)

            await builder.buildPost()

            logging.info(f"Передача данных в БД: {thumbnail}, {text}, {button_text}, {button_link}")


            await NewPostDataInBase(thumbnail_src, text, button_text, button_link)
            await state.clear()


