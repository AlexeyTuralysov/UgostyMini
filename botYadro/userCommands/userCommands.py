from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command


router = Router()

@router.message(Command('id'))
async def echo_handler(message: Message) -> None:
        await message.answer(f"Ваш адишник {message.from_user.id}")