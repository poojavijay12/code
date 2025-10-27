# Use a small official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app


# Copy requirements and installdoc
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (change if you plan a different port)


# Run the app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8007"]
