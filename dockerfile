# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything from current folder into container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
