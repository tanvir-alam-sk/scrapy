# Use an official Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Scrapy project into the container
COPY . .

# Expose a port (optional, if you want to access the container remotely)
EXPOSE 8080

# Set the default command to run Scrapy spider
CMD ["scrapy", "crawl", "trip_spider"]
