import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

print("Forwarder service started...")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

SOURCE_CHANNEL = "matchpredictioncricket"   # @ ke bina
DEST_CHANNEL = "@SessionKingTejasvi"

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN missing")

async def forward_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        chat = update.channel_post.chat
        if chat.username and chat.username.lower() == SOURCE_CHANNEL.lower():
            await context.bot.copy_message(
                chat_id=DEST_CHANNEL,
                from_chat_id=chat.id,
                message_id=update.channel_post.message_id
            )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_post))
app.run_polling()
