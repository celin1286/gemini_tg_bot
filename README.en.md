# Gemini-TG-Bot

A powerful Telegram bot powered by Google Gemini AI models.

## ✨ Key Features

- Support for both gemini-2.0-flash and gemini-1.5-pro models
- Intelligent context memory for coherent conversations
- Image recognition and analysis
- Smart adaptation for private/group chat scenarios
- Integrated web search with summarization
- Containerized deployment with Docker

## 🤖 Commands

| Command | Description |
|---------|-------------|
| `/start` | Initialize and start using the bot |
| `/gemini` | Chat using gemini-2.0-flash model |
| `/gemini_pro` | Chat using gemini-1.5-pro model |
| `/clear` | Clear current conversation history |
| `/switch` | Switch default model (private chat only) |
| `/search` | Search and get summarized content |

## 🔍 Search Feature

The `/search` command enables you to:
- Input search terms in any language
- Get results via DuckDuckGo search
- Receive AI-powered summaries
- View key points in a clear format

Example: `/search latest AI developments 2024`

## 🚀 Deployment Guide

### Method 1: Direct Deployment

1. Clone the repository
```bash
git clone https://github.com/celin1286/gemini_tg_bot.git
cd gemini_tg_bot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure API Keys
- Get Telegram Bot Token from [BotFather](https://t.me/BotFather)
- Get Gemini API Key from [Google AI Studio](https://makersuite.google.com/app/apikey)

4. Start the service
```bash
export TELEGRAM_BOT_API_KEY="Your_TG_Bot_Token"
export GEMINI_API_KEYS="Your_Gemini_API_Key"
python bot.py
```

### Method 2: Docker Deployment

```bash
# Run container AMD64
docker run -d --restart=always \
  -e TELEGRAM_BOT_API_KEY="Your_TG_Bot_Token" \
  -e GEMINI_API_KEYS="Your_Gemini_API_Key" \
  celin1286/gemini_tg_bot:latest
```

## 💬 Usage Guide

- Private Chat: Send messages directly
- Group Chat: Use `/gemini` or `/gemini_pro` + your message
- Use `/clear` to reset conversation history
- Use `/switch` to change default model (private chat only)

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📚 References

- [Gemini-Telegram-Bot](https://github.com/H-T-H/Gemini-Telegram-Bot)
- [tg_bot_collections](https://github.com/yihong0618/tg_bot_collections)
- [md2tgmd](https://github.com/yym68686/md2tgmd)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=H-T-H/Gemini-Telegram-Bot&type=Date)](https://star-history.com/#H-T-H/Gemini-Telegram-Bot&Date)
