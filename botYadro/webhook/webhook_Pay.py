
from fastapi import APIRouter
from pydantic import BaseModel
from aiogram.types import LabeledPrice
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, ContentType, message
from aiogram import Router, F
from aiogram import Bot
#from botYadro.main import bot
webhookPay = APIRouter(tags=["Payment"])
router = Router()

bot = Bot(token="7234999279:AAEA9-jkBBk7GQ66kGuDVeaLLC983MaQIz0")
class InvoiceRequest(BaseModel):
    user_id: int
    pay_total: int


@router.pre_checkout_query()
async def pre_checkout_query(query: PreCheckoutQuery) -> Message:
    #await query.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)
    await query.answer(ok=True)

@router.message(F.successful_payment)
async def successful_payment(message: Message):
    payment = message.successful_payment

    amount = payment.total_amount #Сумма в копейах

    amount_normalized = amount / 100 # из клпеек в рубли
    await message.answer(f"Спасибо за оплату. Сумма: {amount_normalized}")



@webhookPay.post("/bot/create-invoice")
async def create_invoice(data: InvoiceRequest):
    #prices = [LabeledPrice(label="Угощение", amount=10000)]  # 100.00 RUB
    prices = [LabeledPrice(label="Угощение", amount=data.pay_total)]

    await bot.send_invoice(
        chat_id=data.user_id,
        title="Угощение",
        photo_url="https://i.pinimg.com/736x/61/e2/7a/61e27aacc4df27348955c275add51384.jpg",
        description="Это угощение",
        payload="зфн",
        provider_token="381764678:TEST:108057",
        currency="RUB",
        prices=prices,
        start_parameter="ugosty-param",
        need_email=True,
    )

    return {"ok": True}