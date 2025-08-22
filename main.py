import asyncio
from aiogram import Bot, Dispatcher
import logging
from run import register_handlers
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)
admin_ids_str = os.getenv('ADMIN_IDS', '')
admins = list(map(int, admin_ids_str.split(','))) if admin_ids_str else []
DB_PATH = os.getenv('DATABASE_PATH', '/tmp/Form.db')
logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    dp = Dispatcher()
    register_handlers(dp)
    print('Bot is started')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())