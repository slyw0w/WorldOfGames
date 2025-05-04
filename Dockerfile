FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget unzip curl chromium-driver chromium

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8777

CMD ["python", "main.py"]
