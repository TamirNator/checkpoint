FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the project to the container
COPY app.py requirements.txt ./

# Install the dependencies and the `services` package
RUN pip install --no-cache-dir -r requirements.txt

# Add a non-root user for security
RUN useradd -m appuser
USER appuser

# Set PYTHONPATH to include /app so the `services` package is discoverable
ENV PYTHONPATH=/app

# Expose the port for the microservice
EXPOSE 5000

# Run the microservice
CMD ["python", "app.py"]