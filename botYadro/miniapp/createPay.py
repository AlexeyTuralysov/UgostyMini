from aiogram import Router, F

from aiogram import Router
from aiogram.filters import Command

from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, ContentType, message
from aiogram import types

router = Router()
PAYMENT_PROVIDER_TOKEN = '381764678:TEST:108057'




""" 
@router.message(Command("pay"))
async def process_payment(message: Message):
    # Цены на товары
   
    prices = [
        LabeledPrice(label="Бургер", amount=50000),  # 50000 копеек = 500 рублей
        LabeledPrice(label="Картофель фри", amount=30000)
    ]


    prices = [
        LabeledPrice(label="Бургер", amount=77700),  # 50000 копеек = 500 рублей

        ]

    # Отправка счета на оплату
    await message.bot.send_invoice(
        chat_id=message.chat.id,
        title="Угощение",
        description="Угощение автору",
        payload="donate-order-001",  # Идентификатор заказа
        provider_token=PAYMENT_PROVIDER_TOKEN,
        currency="RUB",
        prices=prices,
        start_parameter="kofeyechek-order",
        photo_url="https://i.pinimg.com/736x/61/e2/7a/61e27aacc4df27348955c275add51384.jpg",  # Картинка товара
        photo_width=512,
        photo_height=512,
        photo_size=512,
    )


"""
@router.pre_checkout_query()
async def pre_checkout_query(query: PreCheckoutQuery) -> Message:
    await query.answer(ok=True)


@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("прошел")
    #await message.bot.send_message(message.chat.id,f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")




