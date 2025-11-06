# Dockerfile (recommended)
FROM python:3.10-slim

# Avoid Python writing .pyc files and enable simple logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (if needed) and pip dependencies
# adjust packages if your app needs build tools
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements first for layer caching
COPY app/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app

# Expose port
EXPOSE 8080

# (Optional) create a non-root user (comment out if you prefer root)
# RUN useradd -m myuser && chown -R myuser:myuser /app
# USER myuser

# Run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
