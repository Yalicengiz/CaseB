# Dockerfile
FROM python:3.8

WORKDIR /app

COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/btc_monitor.py ./

CMD ["python", "btc_monitor.py"]

