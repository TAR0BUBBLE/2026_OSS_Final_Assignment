# syntax=docker/dockerfile:1

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY back/requirements.txt /app/back/requirements.txt

RUN python -m pip install --upgrade pip \
    && python -m pip install -r /app/back/requirements.txt

COPY back /app/back
COPY front/assets/heroes /app/front/assets/heroes

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "back.main:app", "--host", "0.0.0.0", "--port", "8000"]
