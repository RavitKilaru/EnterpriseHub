###########################################################
# EnterpriseHub Docker Image
###########################################################

FROM python:3.12.11-slim

###########################################################
# Environment Variables
###########################################################

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

###########################################################
# Working Directory
###########################################################

WORKDIR /app

###########################################################
# Install Linux Packages
###########################################################

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

###########################################################
# Install Python Dependencies
###########################################################

COPY backend/requirements/base.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r base.txt

###########################################################
# Copy Django Project
###########################################################

COPY backend/ /app/

###########################################################
# Copy Docker Files
###########################################################

COPY docker/entrypoint.sh /app/entrypoint.sh

COPY docker/gunicorn.conf.py /app/gunicorn.conf.py

###########################################################
# Make Entrypoint Executable
###########################################################

RUN chmod +x /app/entrypoint.sh

###########################################################
# Create Non Root User
###########################################################

RUN useradd -m appuser && \
    chown -R appuser:appuser /app

USER appuser

###########################################################
# Expose Port
###########################################################

EXPOSE 8000

###########################################################
# Health Check
###########################################################

HEALTHCHECK --interval=30s --timeout=5s CMD curl --fail http://localhost:8000/health/ || exit 1

###########################################################
# Start Container
###########################################################

ENTRYPOINT ["/app/entrypoint.sh"]