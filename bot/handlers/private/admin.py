from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.states.dispatcher import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer_media_group("https://telegra.ph/file/f187c078ceedf3f554c37.jpg",
                               caption="Assalomu alaykum ! Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi")
