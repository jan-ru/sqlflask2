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
ENV PORT=5000

# Expose the port Railway will use
EXPOSE 5000

# Use Gunicorn to serve the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Copy entrypoint script and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set default environment variable (optional)
ENV FLASK_ENV=production

# Use the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]