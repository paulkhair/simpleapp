# Use a light version of Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements first (Better for Docker caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ENTIRE app folder into the container
COPY app/ ./app/

# Tell Flask where the app variable is
# It is inside the 'app' folder, in 'main.py'
ENV FLASK_APP=app/main.py

EXPOSE 5000

# Run the app using the python module path
CMD ["python", "-m", "app.main"]