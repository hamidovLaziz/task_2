import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from bot.states.dispatcher import *
from bot.handlers import *


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
