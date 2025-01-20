FROM python:3.9-slim
WORKDIR /app
COPY ./app_red /app
RUN pip install -r requirements.txt
ENV COLOR=red
CMD ["python", "app.py"]

