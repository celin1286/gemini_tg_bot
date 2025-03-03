import argparse
import os
import traceback
import asyncio
import google.generativeai as genai
import re
import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from md2tgmd import escape
import handers
from config import conf, generation_config, safety_settings

async def main():
    bot_token = os.getenv('TELEGRAM_BOT_API_KEY')
    gemini_key = os.getenv('GEMINI_API_KEYS')

    if not bot_token or not gemini_key:
        # Init args
        parser = argparse.ArgumentParser()
        parser.add_argument("tg_token", help="telegram token (格式: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11)")
        parser.add_argument("GOOGLE_GEMINI_KEY", help="Google Gemini API key")
        options = parser.parse_args()
        bot_token = options.tg_token
        gemini_key = options.GOOGLE_GEMINI_KEY

    if ':' not in bot_token:
        raise ValueError("Telegram Bot Token 格式错误！正确格式应该类似：123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")

    print("Arg parse done.")

    genai.configure(api_key=gemini_key)

    # Init bot
    bot = AsyncTeleBot(bot_token)
    await bot.delete_my_commands(scope=None, language_code=None)
    await bot.set_my_commands(
        commands=[
            telebot.types.BotCommand("start", "Start"),
            telebot.types.BotCommand("gemini", "using gemini-2.0-flash"),
            telebot.types.BotCommand("gemini_pro", "using gemini-1.5-pro"),
            telebot.types.BotCommand("clear", "Clear all history"),
            telebot.types.BotCommand("switch","switch default model"),
            telebot.types.BotCommand("search", "Search the web"),
        ],
    )
    print("Bot init done.")

    # Init commands
    bot.register_message_handler(handers.start,                 commands=['start'],         pass_bot=True)
    bot.register_message_handler(handers.gemini_handler,        commands=['gemini'],        pass_bot=True)
    bot.register_message_handler(handers.gemini_pro_handler,    commands=['gemini_pro'],    pass_bot=True)
    bot.register_message_handler(handers.clear,                 commands=['clear'],         pass_bot=True)
    bot.register_message_handler(handers.switch,                commands=['switch'],        pass_bot=True)
    bot.register_message_handler(handers.gemini_photo_handler,  content_types=["photo"],    pass_bot=True)
    bot.register_message_handler(handers.search_handler,        commands=['search'],        pass_bot=True)
    bot.register_message_handler(
        handers.gemini_private_handler,
        func=lambda message: message.chat.type == "private",
        content_types=['text'],
        pass_bot=True)

    # Start bot
    print("Starting Gemini_Telegram_Bot.")
    await bot.polling(none_stop=True)

if __name__ == '__main__':
    asyncio.run(main())
