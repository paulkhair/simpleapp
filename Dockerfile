# Use a light version of Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app and install Flask
COPY app.py .
RUN pip install flask

# Expose the port and run the app
EXPOSE 5000
CMD ["python", "app.py"]