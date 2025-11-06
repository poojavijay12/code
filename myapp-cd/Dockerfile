# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app


# Copy application code
COPY app/ ./app

# Expose port (FastAPI default: 8080)
EXPOSE 8080

# Command to run the app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
