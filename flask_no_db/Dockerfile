# Utiliser une image Python légère comme base
FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
RUN pip install flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]