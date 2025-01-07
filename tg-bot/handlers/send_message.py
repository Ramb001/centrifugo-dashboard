from telegram import Update
from telegram.ext import ContextTypes

from src.constants import BotReplies


async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        BotReplies.ON_BOARDING,
    )
