# 根据目标平台选择基础镜像
FROM --platform=$TARGETPLATFORM python:3.9.18-slim-bullseye as builder

# 安装编译依赖
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    git \
    build-essential \
    rustc \
    cargo \
    cmake \
    pkg-config \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# 创建虚拟环境
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 设置pip配置
RUN pip config set global.progress_bar off && \
    pip config set global.no-cache-dir true

# 设置 Rust 环境变量
ENV CARGO_NET_GIT_FETCH_WITH_CLI=true
ENV RUSTFLAGS="-C target-feature=-crt-static"
ENV PIP_DEFAULT_TIMEOUT=300

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

# 第四阶段：安装 md2tgmd
RUN pip install --no-cache-dir md2tgmd

# 第五阶段：预安装 duckduckgo-search 的依赖
RUN pip install --no-cache-dir \
    requests==2.31.0 \
    click==8.1.7 \
    lxml==5.1.0 \
    beautifulsoup4==4.12.3 \
    typing-extensions==4.9.0 \
    httpx==0.26.0

# 尝试降级安装特定版本的 duckduckgo-search
RUN pip install --no-cache-dir duckduckgo-search==4.1.1

# 最终阶段：使用精简镜像
FROM --platform=$TARGETPLATFORM python:3.9.18-slim-bullseye

# 从构建阶段复制必要的系统库
COPY --from=builder /usr/lib/aarch64-linux-gnu/libssl.so* /usr/lib/aarch64-linux-gnu/ || true
COPY --from=builder /usr/lib/aarch64-linux-gnu/libcrypto.so* /usr/lib/aarch64-linux-gnu/ || true
COPY --from=builder /usr/lib/x86_64-linux-gnu/libssl.so* /usr/lib/x86_64-linux-gnu/ || true
COPY --from=builder /usr/lib/x86_64-linux-gnu/libcrypto.so* /usr/lib/x86_64-linux-gnu/ || true

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
