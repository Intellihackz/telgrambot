from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = "our Token here"


async def start(update: Update, context):
    await update.message.reply_text("Hello! I can handle different types of messages.")


async def handle_text(update: Update, context):
    text = update.message.text
    await update.message.reply_text(f"You said: {text}")


async def handle_photo(update: Update, context):
    await update.message.reply_text("I received your photo!")
    # You can access the photo file using:
    # photo_file = await update.message.photo[-1].get_file()


async def handle_document(update: Update, context):
    await update.message.reply_text("I received your document!")
    # You can access the document file using:
    # doc_file = await update.message.document.get_file()


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text)
    )
    application.add_handler(MessageHandler(filters.USER_ATTACHMENT, handle_document))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    application.run_polling()


if __name__ == "__main__":
    main()
