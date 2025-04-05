FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl chromium-driver chromium \
    && pip install flask selenium

# Copy source files
COPY . /app
WORKDIR /app

# Expose port and run the app
EXPOSE 8777
CMD ["python", "main.py"]
