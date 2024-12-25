# Use python:3.11-slim as the base image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install dependencies using pip install -r requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Set the command to run the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
