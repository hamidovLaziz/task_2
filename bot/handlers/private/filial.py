from aiogram import F
from aiogram.types import Message
from bot.buttons.reply import main_button
from bot.states.dispatcher import dp


@dp.message(F.text == 'Filial')
async def filial_handler(message: Message):
    await message.answer_location(
        longitude=41.304476, latitude=69.253043, reply_markup=main_button())
