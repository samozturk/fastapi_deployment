FROM python:3.8

WORKDIR /usr/local/src/app

COPY . .

RUN pip install --no-cache-dir -r  requirements.txt

EXPOSE 80


CMD ["python", "app/main.py"]