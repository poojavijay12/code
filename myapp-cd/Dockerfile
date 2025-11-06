FROM python:3.11-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app/ /app
ENV PORT=8080
EXPOSE 8080
CMD ["python", "main.py"]
