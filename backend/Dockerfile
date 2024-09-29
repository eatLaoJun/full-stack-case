# 使用官方的 Python 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制 backend 文件到工作目录
COPY backend/ .

# 安装依赖包
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用运行的端口
EXPOSE 3434

# 启动应用程序
CMD ["python", "app.py"]

# 打印.env
CMD ["cat", "/app/.env"]
