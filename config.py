conf = {
    "error_info":           "⚠️⚠️⚠️\nSomething went wrong !\nplease try to change your prompt or contact the admin !",
    "before_generate_info": "🤖Generating🤖",
    "download_pic_notify":  "🤖Loading picture🤖",
    "model_1":              "gemini-2.0-flash",
    "model_2":              "gemini-1.5-pro-latest",
    "n": 30,  # Number of historical records to keep
    "search_result_count": 5,  # 搜索结果数量
    "search_summary_prompt": """请根据搜索结果提供一个清晰简洁的总结:
1. 提取主要信息点
2. 保持客观准确
3. 说明信息来源于搜索结果
4. 如有争议要说明不同观点""",
    "search_timeout": 10      # 搜索超时时间(秒)
}

generation_config = {
    "temperature": 1,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 1024,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {   
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]