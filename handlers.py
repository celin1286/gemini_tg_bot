from duckduckgo_search import AsyncDDGS
from googleapiclient.discovery import build

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

        async with AsyncDDGS() as ddgs:
            search_results = []
            async for r in ddgs.text(english_query, max_results=conf["search_result_count"]):
                search_results.append(r)
                
        if not search_results:
            await bot.edit_message_text("没有找到相关结果", chat_id=sent_message.chat.id, message_id=sent_message.message_id)
            return
            
        # 准备搜索结果文本
        search_content = f"Results for '{english_query}':\n\n"
        for item in search_results:
            search_content += f"Title: {item['title']}\n"
            search_content += f"Summary: {item['body']}\n\n"
            
        # 让Gemini总结搜索结果并翻译成中文
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

        summary = f"🔍 搜索词: {query}\n" \
                 f"🌐 英文搜索词: {english_query}\n\n" \
                 f"📝 总结分析:\n{response.text}\n\n"

        summary += "\n原始链接:\n"
        for item in search_results[:3]:
            summary += f"• {item['link']}\n"
            
        try:
            await bot.edit_message_text(escape(summary), chat_id=sent_message.chat.id, message_id=sent_message.message_id, parse_mode="MarkdownV2", disable_web_page_preview=True)
        except:
            await bot.edit_message_text(summary, chat_id=sent_message.chat.id, message_id=sent_message.message_id, disable_web_page_preview=True)
            
    except Exception as e:
        traceback.print_exc()
        await bot.edit_message_text(error_info, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
