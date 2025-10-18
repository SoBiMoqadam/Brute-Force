FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_RUN_HOST=127.0.0.1
CMD ["python", "vuln_app.py"]
