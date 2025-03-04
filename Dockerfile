# 根据目标平台选择基础镜像
FROM --platform=$TARGETPLATFORM python:3.9.18-slim-bullseye as builder

# 安装编译依赖，为 ARM64 添加额外的依赖
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    git \
    build-essential \
    rustc \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# 创建虚拟环境
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 设置pip配置
RUN pip config set global.progress_bar off && \
    pip config set global.no-cache-dir true

# 设置环境变量以支持跨平台编译
ENV CARGO_NET_GIT_FETCH_WITH_CLI=true
ENV RUSTFLAGS="-C target-feature=-crt-static"

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

# 第四阶段：分开安装其他依赖并添加错误处理
RUN pip install --no-cache-dir --verbose md2tgmd || (echo "Failed to install md2tgmd" && exit 1)
RUN pip install --no-cache-dir --verbose duckduckgo-search || (echo "Failed to install duckduckgo-search" && exit 1)

# 最终阶段：使用精简镜像
FROM --platform=$TARGETPLATFORM python:3.9.18-slim-bullseye

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
