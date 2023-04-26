# Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /test1

# Copy the Flask app code
COPY app.py .

# Install Gunicorn
RUN pip install flask gunicorn

# Expose port 8000
EXPOSE 8000

# Set the default command to run Gunicorn with the Flask app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
