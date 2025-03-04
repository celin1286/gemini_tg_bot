# 使用 Python 3.9.18 slim 镜像作为基础镜像
FROM python:3.9.18-slim-bullseye

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 更新 pip 并安装依赖
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 复制其他项目文件
COPY . .

# 设置环境变量
ENV TELEGRAM_BOT_API_KEY=""
ENV GEMINI_API_KEYS=""

# 启动命令
CMD ["sh", "-c", "python main.py ${TELEGRAM_BOT_API_KEY} ${GEMINI_API_KEYS}"]
