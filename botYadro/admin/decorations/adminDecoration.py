from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext

AdminSp = {1061542041}
def for_admin(func):
    async def wrapper(message: types.Message, state: FSMContext):
        if message.from_user.id in AdminSp:
            return await func(message, state)
        else:
            await message.reply("Вы не админ")

    return wrapper

