import aiohttp

from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction

from src.constants import PB, PocketbaseCollections, BotReplies, CENTRIFUGO
from helpers.jwt import generate_jwt_token


async def onboarding(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)

    async with aiohttp.ClientSession() as client:
        user_ = await PB.fetch_records(
            PocketbaseCollections.USERS,
            client,
            filter=f"tg_id=(tg_id='{update.effective_user.id}')",
        )

        if len(user_["items"]) == 0:
            user = await PB.add_record(
                PocketbaseCollections.USERS,
                client,
                tg_id=update.effective_user.id,
                username=update.effective_user.username,
                chat_id=update.effective_chat.id,
                jwt=generate_jwt_token(update.effective_user.id),
            )

            await CENTRIFUGO.subscribe(client, "general", user["jwt"], {})

    await update.message.reply_text(
        BotReplies.ON_BOARDING,
    )
