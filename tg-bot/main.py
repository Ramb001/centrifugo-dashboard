import logging

from telegram.ext import ApplicationBuilder, CommandHandler

from src.constants import BOT_TOKEN

from handlers.onboarding import onboarding

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", onboarding))

    while True:
        app.run_polling()


if __name__ == "__main__":
    main()
