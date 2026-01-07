from telegram import Update
from telegram.ext import ApplicationBuilder , CommandHandler , ContextTypes , MessageHandler , filters


TOKEN = "6912062316:AAEZcZHOu8RgIAapevtloxfQ_7DU5gzxSHA"

async def start(update: Update , contex: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("robot telegramet dare kar mikone")

async def echo(update : Update , contex : ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,echo))

app.run_polling()