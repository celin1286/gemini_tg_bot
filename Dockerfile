# 使用多阶段构建来减小最终镜像大小
FROM python:3.9.18-slim-bullseye as builder

# 安装编译依赖
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# 创建虚拟环境
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 设置pip配置
RUN pip config set global.progress_bar off && \
    pip config set global.no-cache-dir true

# 安装依赖
WORKDIR /app
COPY requirements.txt .

# 分步安装依赖，设置具体版本号以提高稳定性
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir wheel setuptools && \
    pip install --no-cache-dir pyTelegramBotAPI==4.14.0 && \
    pip install --no-cache-dir google-generativeai==0.3.2 && \
    pip install --no-cache-dir aiohttp==3.9.1 && \
    pip install --no-cache-dir md2tgmd==1.0.2 && \
    pip install --no-cache-dir google-api-python-client==2.114.0 && \
    pip install --no-cache-dir "duckduckgo-search>=4.1.1"

# 第二阶段：最终镜像
FROM python:3.9.18-slim-bullseye

# 复制虚拟环境
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 设置工作目录和复制应用文件
WORKDIR /app
COPY . .

# 设置环境变量
ENV TELEGRAM_BOT_API_KEY=""
ENV GEMINI_API_KEYS=""

# 启动命令
CMD ["sh", "-c", "python main.py ${TELEGRAM_BOT_API_KEY} ${GEMINI_API_KEYS}"]
