# Use the official Python image as a base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . /app/

# Collect static files (if you have any)
RUN python manage.py collectstatic --no-input

#Make migrations
RUN python manage.py collectstatic --no-input
RUN python manage.py collectstatic --no-input

# Expose the port your Django app runs on
EXPOSE 8000

# Command to make migrations, run migrations, and start the app
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:$PORT"]
