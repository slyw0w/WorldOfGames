FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl chromium-driver chromium \
    && pip install flask selenium

# Copy source code
COPY . /app
WORKDIR /app

EXPOSE 8777

CMD ["python", "MainScores.py"]
