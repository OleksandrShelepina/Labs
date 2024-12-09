from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привіт! Я ехо-бот. Напиши щось, і я повторю.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def main():
    
    BOT_TOKEN = "ВАШ_ТОКЕН_БОТА"

    
    app = ApplicationBuilder().token(BOT_TOKEN).build()


    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    
    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()
