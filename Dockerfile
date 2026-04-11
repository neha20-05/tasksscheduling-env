FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn openai pydantic

ENV PYTHONPATH=/app

CMD ["uvicorn", "server.app:main", "--host", "0.0.0.0", "--port", "7860"]
