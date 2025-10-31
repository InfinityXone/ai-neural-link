FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=8080
RUN pip install --no-cache-dir fastapi uvicorn[standard]
COPY app ./app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8080"]
