# Gemini-Bot

A Telegram bot based on Google Gemini.

## Features

- [X] Basic conversation
- [X] Context memory
- [X] Image recognition
- [X] Different modes for private/group chat
- [X] Web search and summarization

## Commands

• `/start` - Start using the bot
• `/gemini` - Chat using gemini-2.0-flash model
• `/gemini_pro` - Chat using gemini-1.5-pro model
• `/clear` - Clear conversation history
• `/switch` - Switch default model (private chat only)
• `/search` - Search and summarize content in Chinese

## Search Feature

Using the `/search` command, you can:

1. Input Chinese search terms, which will be automatically translated to English
2. Search using DuckDuckGo to get relevant results
3. Have Gemini analyze and summarize results in Chinese
4. Get key points summary

Example:
```
/search controlled nuclear fusion latest progress
```

# Installation
## (1) Linux System
1. Install dependencies
```
pip install -r requirements.txt
```
2. Get Telegram Bot API Token from [BotFather](https://t.me/BotFather)
3. Get Gemini API keys from [Google AI Studio](https://makersuite.google.com/app/apikey)
4. Run the bot with command:
```

## (2) Deploy with Docker
### Using pre-built image (x86 only)
```
docker run -d --restart=always -e TELEGRAM_BOT_API_KEY={Telegram Bot API} -e GEMINI_API_KEYS={Gemini API Keys} qwqhthqwq/gemini-telegram-bot:main
```
### Build yourself
1. Get Telegram Bot API from [BotFather](https://t.me/BotFather)
2. Get Gemini API keys from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. Clone project
```
git clone https://github.com/H-T-H/Gemini-Telegram-Bot.git
```
4. Enter project directory
```
cd Gemini-Telegram-Bot
```
5. Build image
```
docker build -t gemini_tg_bot .
```
6. Run image
```
docker run -d --restart=always -e TELEGRAM_BOT_API_KEY={Telegram Bot API} -e GEMINI_API_KEYS={Gemini API Keys} gemini_tg_bot
```

# Usage
1. In private chat, directly send your questions
2. In group chat, use **/gemini** or **/gemini_pro** + your question
3. Use **/clear** to delete conversation history
4. Use **/switch** to change default model in private chat

# References
1. [https://github.com/yihong0618/tg_bot_collections](https://github.com/yihong0618/tg_bot_collections)
2. [https://github.com/yym68686/md2tgmd](https://github.com/yym68686/md2tgmd)
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=H-T-H/Gemini-Telegram-Bot&type=Date)](https://star-history.com/#H-T-H/Gemini-Telegram-Bot&Date)
