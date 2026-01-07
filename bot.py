from telegram import Update , MessageEntity
from telegram.ext import ApplicationBuilder , CommandHandler , ContextTypes , MessageHandler , filters
import os 

TOKEN = os.environ['TOKEN']

async def start(update: Update , contex: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("robot telegramet dare kar mikone")

async def echo(update : Update , contex : ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(text)

def extract_links(message):
    links = []

    if message.entities:
        for entity in message.entities:
            if entity.type in [MessageEntity.URL, MessageEntity.TEXT_LINK]:
                if entity.type == MessageEntity.URL:
                   

                    start = entity.offset
                    end = start + entity.length
                    links.append(message.text[start:end])

                elif entity.type == MessageEntity.TEXT_LINK:
                   
                    links.append(entity.url)

    return links

async def link_in_message(update, context):
    message = update.message
    links = extract_links(message)

    if links:
        await message.reply_text("لینک‌ها پیدا شد 👇")
        for link in links:
            await message.reply_text(link)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,echo))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,link_in_message))

app.run_polling()