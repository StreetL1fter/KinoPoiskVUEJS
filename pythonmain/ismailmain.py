
from aiogram import Bot, Dispatcher 
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.enums.dice_emoji import DiceEmoji
from config_reader import config
import logging
import asyncio
from app.handlers import router


bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)






async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    


asyncio.run(main())