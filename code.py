

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import os
import re

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # First message
    await update.message.reply_text("Hello Dear 🥰! Welcome to Phantom AI Trading with Coach Jessica. I’m excited to help you achieve your financial dreams💸🤑😊")

    # Wait 6 seconds
    await asyncio.sleep(6)

    # Second message with community button
    community_keyboard = [[InlineKeyboardButton("Join Free Community", url="https://t.me/financialfreedom_OfurePhantomAI")]]
    await update.message.reply_text(
        "Here's a link to join my free community. Once you join, come back here and I will send you a free video that gives you all the tantalizing information you need to start making passive income with Phantom AI.",
        reply_markup=InlineKeyboardMarkup(community_keyboard)
    )

    # Wait 15 seconds
    await asyncio.sleep(15)

    # Third message with video button
    video_keyboard = [[InlineKeyboardButton("Watch Video Guide", url="https://tinyurl.com/Trading-Bot-Video")]]
    await update.message.reply_text(
        "Here's a link to the video guide as promised🤝. Be sure to watch it to the end as there's a giveaway at the end. Don't miss it😜. \n\n Send me the phrase \"ready to install\" after watching. Use the next link i will send to messsage me directly, I'd be waiting here for you 🫵 " ,
        reply_markup=InlineKeyboardMarkup(video_keyboard)
    )
    asyncio.create_task(send_final_message_after_delay(update))

async def send_final_message_after_delay(update: Update):
    await asyncio.sleep(60)
    video_coach = [[
        InlineKeyboardButton("Ready to Install", url="https://t.me/PhantomAITrader")
    ]]
    await update.message.reply_text(
        "🎉 Ready or not, you can chat with Coach Jessica here:",
        reply_markup=InlineKeyboardMarkup(video_coach)
    )

async def handle_ready(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    video_coach = [[InlineKeyboardButton("Ready to Install", url="https://t.me/PhantomAITrader")]]
    await update.message.reply_text("🎉 Chat with Coach Jessica",
    reply_markup =InlineKeyboardMarkup(video_coach)
    )


def main() -> None:
    # Replace with your bot token
    app = Application.builder().token("7907539051:AAGbKDCs6oyFlWc53yGaTRW8j2NHmG1Akrg").build()

    # Add handlers
    pattern = re.compile(r'\b(ready|install)\b', re.IGNORECASE)

# Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex(pattern), handle_ready))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
