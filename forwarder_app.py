import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

print("Forwarder service started...")

SOURCE_CHANNEL = "matchpredictioncricket"
DESTINATION_CHANNEL = "@SessionKingTejasvi"

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not found")

async def auto_forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.chat.username:
        if update.channel_post.chat.username.lower() == SOURCE_CHANNEL.lower():
            await context.bot.copy_message(
                chat_id=DESTINATION_CHANNEL,
                from_chat_id=update.channel_post.chat.id,
                message_id=update.channel_post.message_id
            )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, auto_forward))
app.run_polling()
