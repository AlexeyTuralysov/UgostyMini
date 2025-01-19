from aiogram.fsm import state
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class builderPostsClass:
    def __init__(self, message, state, thumbnail, thumbnail_src, text,button_text,button_link):
        self.message = message
        self.state = state
        self.thumbnail = thumbnail
        self.thumbnail_src = thumbnail_src
        self.text = text
        self.button_text = button_text
        self.button_link = button_link

    """
    Билдер для создания рассылки 
    """
    async def PostTemplate(self, chat_id):

        if self.button_text and self.button_link:
            big_button_1 = InlineKeyboardButton(text=self.button_text, url=self.button_link)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[[big_button_1]])


            if self.thumbnail_src:
                await self.message.bot.send_photo(chat_id=chat_id, photo=self.thumbnail_src, caption=self.text, reply_markup=keyboard)
            else:
                await self.message.bot.send_message(chat_id=chat_id, text=self.text, reply_markup=keyboard)


        elif self.thumbnail_src:
            await self.message.bot.send_photo(chat_id=chat_id, photo=self.thumbnail_src, caption=self.text)


        else:
            await self.message.bot.send_message(chat_id=chat_id, text=self.text)

    """
       Билдер для создания поста 
     """
    async def buildPost(self):
        if self.button_text and self.button_link:
            big_button_1 = InlineKeyboardButton(text= self.button_text, url= self.button_link)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[[big_button_1]])

            if self.thumbnail:
                await self.message.answer_photo(photo=self.thumbnail, caption= self.text, reply_markup=keyboard)
            else:
                await self.message.answer(self.text, reply_markup=keyboard)

        elif self.thumbnail:
            await self.message.answer_photo(photo= self.thumbnail, caption= self.text)
        else:
            await self.message.answer(self.text)

        if self.thumbnail:

            await self.state.update_data(thumbnail= self.thumbnail)

        else:
            await self.state.update_data(thumbnail=None)




