# Stage 1: Build
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Set environment variables
ENV FLASK_APP=app/main.py

EXPOSE 5000

# Start the application
CMD ["python", "app/main.py"]