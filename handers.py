from telebot import TeleBot
from telebot.types import Message
from md2tgmd import escape
import traceback
import google.generativeai as genai
from duckduckgo_search import DDGS

from config import conf
import gemini

error_info              =       conf["error_info"]
before_generate_info    =       conf["before_generate_info"]
download_pic_notify     =       conf["download_pic_notify"]
model_1                 =       conf["model_1"]
model_2                 =       conf["model_2"]

gemini_player_dict = gemini.gemini_player_dict
gemini_pro_player_dict = gemini.gemini_pro_player_dict
default_model_dict = gemini.default_model_dict

async def start(message: Message, bot: TeleBot) -> None:
    try:
        await bot.reply_to(message , escape("Welcome, you can ask me questions now. \nFor example: `Who is john lennon?`"), parse_mode="MarkdownV2")
    except IndexError:
        await bot.reply_to(message, error_info)

async def gemini_handler(message: Message, bot: TeleBot) -> None:
    try:
        m = message.text.strip().split(maxsplit=1)[1].strip()
    except IndexError:
        await bot.reply_to( message , escape("Please add what you want to say after /gemini. \nFor example: `/gemini Who is john lennon?`"), parse_mode="MarkdownV2")
        return
    await gemini.gemini(bot,message,m,model_1)

async def gemini_pro_handler(message: Message, bot: TeleBot) -> None:
    try:
        m = message.text.strip().split(maxsplit=1)[1].strip()
    except IndexError:
        await bot.reply_to( message , escape("Please add what you want to say after /gemini_pro. \nFor example: `/gemini_pro Who is john lennon?`"), parse_mode="MarkdownV2")
        return
    await gemini.gemini(bot,message,m,model_2)

async def clear(message: Message, bot: TeleBot) -> None:
    # Check if the player is already in gemini_player_dict.
    if (str(message.from_user.id) in gemini_player_dict):
        del gemini_player_dict[str(message.from_user.id)]
    if (str(message.from_user.id) in gemini_pro_player_dict):
        del gemini_pro_player_dict[str(message.from_user.id)]
    await bot.reply_to(message, "Your history has been cleared")

async def switch(message: Message, bot: TeleBot) -> None:
    if message.chat.type != "private":
        await bot.reply_to( message , "This command is only for private chat !")
        return
    # Check if the player is already in default_model_dict.
    if str(message.from_user.id) not in default_model_dict:
        default_model_dict[str(message.from_user.id)] = False
        await bot.reply_to( message , "Now you are using "+model_2)
        return
    if default_model_dict[str(message.from_user.id)] == True:
        default_model_dict[str(message.from_user.id)] = False
        await bot.reply_to( message , "Now you are using "+model_2)
    else:
        default_model_dict[str(message.from_user.id)] = True
        await bot.reply_to( message , "Now you are using "+model_1)

async def gemini_private_handler(message: Message, bot: TeleBot) -> None:
    m = message.text.strip()
    if str(message.from_user.id) not in default_model_dict:
        default_model_dict[str(message.from_user.id)] = True
        await gemini.gemini(bot,message,m,model_1)
    else:
        if default_model_dict[str(message.from_user.id)]:
            await gemini.gemini(bot,message,m,model_1)
        else:
            await gemini.gemini(bot,message,m,model_2)

async def gemini_photo_handler(message: Message, bot: TeleBot) -> None:
    if message.chat.type != "private":
        s = message.caption
        if not s or not (s.startswith("/gemini")):
            return
        try:
            prompt = s.strip().split(maxsplit=1)[1].strip() if len(s.strip().split(maxsplit=1)) > 1 else ""
            file_path = await bot.get_file(message.photo[-1].file_id)
            sent_message = await bot.reply_to(message, download_pic_notify)
            downloaded_file = await bot.download_file(file_path.file_path)
        except Exception:
            traceback.print_exc()
            await bot.reply_to(message, error_info)
        model = genai.GenerativeModel(model_1)
        contents = {
            "parts": [{"mime_type": "image/jpeg", "data": downloaded_file}, {"text": prompt}]
        }
        try:
            await bot.edit_message_text(before_generate_info, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
            response = await gemini.async_generate_content(model, contents)
            await bot.edit_message_text(response.text, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
        except Exception:
            traceback.print_exc()
            await bot.edit_message_text(error_info, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
    else:
        s = message.caption if message.caption else ""
        try:
            prompt = s.strip()
            file_path = await bot.get_file(message.photo[-1].file_id)
            sent_message = await bot.reply_to(message, download_pic_notify)
            downloaded_file = await bot.download_file(file_path.file_path)
        except Exception:
            traceback.print_exc()
            await bot.reply_to(message, error_info)
        model = genai.GenerativeModel(model_1)
        contents = {
            "parts": [{"mime_type": "image/jpeg", "data": downloaded_file}, {"text": prompt}]
        }
        try:
            await bot.edit_message_text(before_generate_info, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
            response = await gemini.async_generate_content(model, contents)
            await bot.edit_message_text(response.text, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
        except Exception:
            traceback.print_exc()
            await bot.edit_message_text(error_info, chat_id=sent_message.chat.id, message_id=sent_message.message_id)

async def search_handler(message: Message, bot: TeleBot) -> None:
    try:
        query = message.text.strip().split(maxsplit=1)[1].strip()
    except IndexError:
        await bot.reply_to(message, escape("请在 /search 后输入要搜索的内容"), parse_mode="MarkdownV2")
        return
        
    try:
        sent_message = await bot.reply_to(message, "🔍 正在搜索并分析结果...")

        model = genai.GenerativeModel(model_1)
        translate_prompt = f"""请将以下中文搜索词翻译成英文,只需要返回翻译结果,不要添加任何额外解释:
{query}"""
        
        translate_response = await gemini.async_generate_content(model, translate_prompt)
        english_query = translate_response.text.strip()
        
        await bot.edit_message_text(f"🔍 正在搜索: {english_query}", chat_id=sent_message.chat.id, message_id=sent_message.message_id)

        search_results = []
        with DDGS() as ddgs:
            results = ddgs.text(english_query, max_results=conf["search_result_count"])
            search_results.extend(results)
                
        if not search_results:
            await bot.edit_message_text("没有找到相关结果", chat_id=sent_message.chat.id, message_id=sent_message.message_id)
            return

        search_content = f"Results for '{english_query}':\n\n"
        for item in search_results:
            search_content += f"Title: {item.get('title', 'No Title')}\n"
            search_content += f"Summary: {item.get('body', 'No Content')}\n\n"

        await bot.edit_message_text("🤖 正在总结分析并翻译...", chat_id=sent_message.chat.id, message_id=sent_message.message_id)
        
        summary_prompt = f"""请用中文总结以下英文搜索结果。要求:
1. 提取关键信息并翻译成中文
2. 保持客观准确
3. 如有不同观点要兼顾
4. 指出信息来源于网络搜索

搜索结果:
{search_content}
"""
        response = await gemini.async_generate_content(model, summary_prompt)

        summary = f"📝 总结分析:\n{response.text}"
            
        try:
            await bot.edit_message_text(escape(summary), chat_id=sent_message.chat.id, message_id=sent_message.message_id, parse_mode="MarkdownV2", disable_web_page_preview=True)
        except:
            await bot.edit_message_text(summary, chat_id=sent_message.chat.id, message_id=sent_message.message_id, disable_web_page_preview=True)
            
    except Exception as e:
        traceback.print_exc()
        await bot.edit_message_text(error_info, chat_id=sent_message.chat.id, message_id=sent_message.message_id)