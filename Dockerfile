# 使用 AMD64 平台的基础镜像
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

# 安装所有依赖
RUN pip install --no-cache-dir -r requirements.txt

# 最终阶段：使用精简镜像
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
