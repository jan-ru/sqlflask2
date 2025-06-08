# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000
EXPOSE 5000

# Run Flask
CMD ["flask", "run"]

