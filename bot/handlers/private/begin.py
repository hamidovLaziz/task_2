from aiogram import F
from aiogram.fsm.state import StatesGroup
from aiogram.types import Message, CallbackQuery

from bot.buttons.reply import begin_button, main_button, women_button, man_button
from bot.states.dispatcher import dp



@dp.message(F.text == 'Start')
async def begin_handler(message: Message):
    await message.answer("Quydagilardan birortasini tanlang", reply_markup=begin_button())


@dp.callback_query(F.data.startswith(' '))
async def chose(query: CallbackQuery):
    value = query.data
    if value == ' Back':
        await query.answer('Back', reply_markup=main_button())
    elif value == ' Woman':
        await query.answer('Woman', reply_markup=women_button())
    else:
        await query.answer('Start', reply_markup=man_button())