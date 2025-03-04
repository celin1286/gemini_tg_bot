# 使用更完整的 Python 镜像
FROM python:3.9-buster

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

# 安装依赖，并保留 pip 日志以便调试
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt 2>&1 | tee pip_install.log

COPY . .
ENV TELEGRAM_BOT_API_KEY=""
ENV GEMINI_API_KEYS=""
CMD ["sh", "-c", "python main.py ${TELEGRAM_BOT_API_KEY} ${GEMINI_API_KEYS}"]
