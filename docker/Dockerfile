############################################################
# Stage 1 - Builder
############################################################
FROM python:3.12.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /build

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements/base.txt .

RUN python -m pip install --upgrade pip

RUN pip wheel \
    --no-cache-dir \
    --wheel-dir /wheels \
    -r base.txt

############################################################
# Stage 2 - Runtime
############################################################
FROM python:3.12.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /wheels /wheels

COPY backend/requirements/base.txt .

RUN python -m pip install --upgrade pip && \
    pip install \
    --no-cache-dir \
    --no-index \
    --find-links=/wheels \
    -r base.txt && \
    rm -rf /wheels

RUN useradd --create-home --shell /bin/bash appuser

COPY --chown=appuser:appuser backend/ /app/

COPY --chown=appuser:appuser docker/entrypoint.sh /app/entrypoint.sh

COPY --chown=appuser:appuser docker/gunicorn.conf.py /app/gunicorn.conf.py

RUN chmod +x /app/entrypoint.sh

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
CMD curl --fail http://localhost:8000/health/ || exit 1

ENTRYPOINT ["/app/entrypoint.sh"]