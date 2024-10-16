# Use a base image with Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Define the command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
