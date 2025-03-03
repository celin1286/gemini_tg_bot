# Gemini-TG-Bot

一个功能强大的 Telegram 机器人,基于 Google Gemini AI 模型打造。

## ✨ 主要特性

- 支持 gemini-2.0-flash 和 gemini-1.5-pro 两种模型
- 智能上下文记忆,对话更连贯
- 支持图片识别和分析
- 私聊/群聊场景智能适配
- 集成网络搜索与中文总结功能
- Docker 容器化部署

## 🤖 命令列表

| 命令 | 说明 |
|------|------|
| `/start` | 初始化并开始使用机器人 |
| `/gemini` | 使用 gemini-2.0-flash 模型对话 |
| `/gemini_pro` | 使用 gemini-1.5-pro 模型对话 |
| `/clear` | 清空当前对话历史记录 |
| `/switch` | 切换默认对话模型(仅私聊可用) |
| `/search` | 进行网络搜索并获取中文总结 |

## 🔍 搜索功能

通过 `/search` 命令可以:
- 自动将中文关键词翻译成英文搜索
- 调用 DuckDuckGo 获取搜索结果
- 使用 Gemini 进行智能总结
- 以清晰要点形式展示结论

示例: `/search 2024年AI发展趋势`

## 🚀 部署指南

### 方式一：直接部署

1. 克隆项目
```bash
git clone https://github.com/celin1286/gemini_tg_bot.git
cd gemini_tg_bot
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置密钥
- 从 [BotFather](https://t.me/BotFather) 获取 Telegram Bot Token
- 从 [Google AI Studio](https://makersuite.google.com/app/apikey) 获取 Gemini API Key

4. 启动服务
```bash
export TELEGRAM_BOT_API_KEY="你的TG机器人Token"
export GEMINI_API_KEYS="你的Gemini API密钥"
python bot.py
```

### 方式二：Docker 部署

```bash
# 构建镜像
docker build -t gemini_tg_bot .

# 运行容器
docker run -d --restart=always \
  -e TELEGRAM_BOT_API_KEY="你的TG机器人Token" \
  -e GEMINI_API_KEYS="你的Gemini API密钥" \
  gemini_tg_bot
```

## 💬 使用说明

- 私聊模式：直接发送消息即可对话
- 群聊模式：需要使用 `/gemini` 或 `/gemini_pro` 命令
- 使用 `/clear` 清除对话历史
- 使用 `/switch` 切换默认模型(仅限私聊)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request!

## 📚 参考项目

- [Gemini-Telegram-Bot](https://github.com/H-T-H/Gemini-Telegram-Bot)
- [tg_bot_collections](https://github.com/yihong0618/tg_bot_collections)
- [md2tgmd](https://github.com/yym68686/md2tgmd)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=H-T-H/Gemini-Telegram-Bot&type=Date)](https://star-history.com/#H-T-H/Gemini-Telegram-Bot&Date)
