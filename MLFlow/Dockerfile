# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update -y && apt-get install -y --no-install-recommends

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY web_service.py ./
COPY script_training.py ./

EXPOSE 8000

ENV MLFLOW_TRACKING_URI=http://127.0.0.1:8080

CMD ["uvicorn", "web_service:app", "--host", "0.0.0.0", "--port", "8000"]

