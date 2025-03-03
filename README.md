# Gemini-Bot

一个基于 Google Gemini 的 Telegram 机器人。

## 功能

- [X] 基础对话功能 
- [X] 记忆上下文
- [X] 图片识别
- [X] 私聊/群聊不同模式
- [X] 网络搜索与总结

## 命令说明

• `/start` - 开始使用机器人
• `/gemini` - 使用 gemini-2.0-flash 模型对话
• `/gemini_pro` - 使用 gemini-1.5-pro 模型对话 
• `/clear` - 清除对话历史
• `/switch` - 切换默认模型(仅私聊)
• `/search` - 搜索相关内容并用中文总结

## 搜索功能说明

通过 `/search` 命令,可进行以下操作:

1. 输入中文搜索词,机器人会自动翻译成英文进行搜索
2. 使用 DuckDuckGo 进行搜索,获取相关结果
3. 由 Gemini 对结果进行中文总结和分析
4. 返回要点总结

使用示例:
```
/search 可控核聚变最新进展
```

# 如何安装
## (1) Linux系统
1. 安装依赖
```
pip install -r requirements.txt
```
2. 在[BotFather](https://t.me/BotFather)获取Telegram Bot API Token
3. 在[Google AI Studio](https://makersuite.google.com/app/apikey)获取Gemini API keys
4. 运行机器人，执行以下命令：
```

## (2)使用 Docker 部署
### 使用构建好的镜像(x86 only)
```
docker run -d --restart=always -e TELEGRAM_BOT_API_KEY={Telegram 机器人 API} -e GEMINI_API_KEYS={Gemini API 密钥} qwqhthqwq/gemini-telegram-bot:main
```
### 自行构建
1. 在[BotFather](https://t.me/BotFather)获取Telegram Bot API
2. 在[Google AI Studio](https://makersuite.google.com/app/apikey)获取Gemini API keys
3. 克隆项目
```
git clone https://github.com/celin1286/gemini_tg_bot.git
```
4. 进入项目目录
```
cd Gemini-Telegram-Bot
```
5. 构建镜像
```
docker build -t gemini_tg_bot .
```
6. 运行镜像
```
docker run -d --restart=always -e TELEGRAM_BOT_API_KEY={Telegram 机器人 API} -e GEMINI_API_KEYS={Gemini API 密钥} gemini_tg_bot
```

# 使用方法
1. 私聊中直接发送你的问题即可
2. 群组中使用 **/gemini** 或者 **/gemini_pro** +你的问题
3. 删除对话的历史记录请使用 **/clear**
4. 切换私聊中默认调用的模型请使用 **/switch**

# 参考信息
1. [https://github.com/yihong0618/tg_bot_collections](https://github.com/yihong0618/tg_bot_collections)
2. [https://github.com/yym68686/md2tgmd](https://github.com/yym68686/md2tgmd)
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=H-T-H/Gemini-Telegram-Bot&type=Date)](https://star-history.com/#H-T-H/Gemini-Telegram-Bot&Date)
