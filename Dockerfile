# 使用多阶段构建来减小最终镜像大小
FROM --platform=linux/amd64 python:3.9.18-slim-bullseye as builder

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

# 第一阶段：基础工具
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir wheel setuptools

# 第二阶段：安装主要依赖
RUN pip install --no-cache-dir pyTelegramBotAPI && \
    pip install --no-cache-dir aiohttp

# 第三阶段：安装 Google 相关依赖
RUN pip install --no-cache-dir google-generativeai && \
    pip install --no-cache-dir google-api-python-client

# 第四阶段：安装其他依赖
RUN pip install --no-cache-dir md2tgmd && \
    pip install --no-cache-dir duckduckgo-search

# 第二阶段：最终镜像
FROM --platform=linux/amd64 python:3.9.18-slim-bullseye

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
