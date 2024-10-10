# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the kitchen.py file into the container
COPY kitchen.py .

# Install Flask (if necessary)
RUN pip install flask

# Expose the port your application runs on (if using Flask's default port)
EXPOSE 5001

# Command to run the kitchen.py script
CMD ["python", "kitchen.py"]
