import asyncio
import os

from aiogram import Bot, Dispatcher

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from core.logger import get_logger, setup_logging
from handlers.user_private import user_private_router


ALLOWED_UPDATES = ["message", "edited_message", "callback_query"]

setup_logging()
logger = get_logger(__name__)

token = os.getenv("TOKEN")
if not token:
    logger.critical("Environment variable TOKEN is not set")
    raise RuntimeError("TOKEN environment variable is required")

bot = Bot(token=token)
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    logger.info("Starting Telegram dice bot")
    logger.info("Allowed updates: %s", ", ".join(ALLOWED_UPDATES))

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        logger.info("Webhook deleted, pending updates dropped")
        await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    except Exception:
        logger.exception("Bot stopped because of an unexpected error")
        raise
    finally:
        await bot.session.close()
        logger.info("Bot session closed")


asyncio.run(main())
